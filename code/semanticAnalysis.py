import copy
import sys
import traceback
import parser

def resolveExpression(expression, idMap, structMap):
    match expression:        
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            left = resolveExpression(lvalue, idMap, structMap)
            right = resolveExpression(exp, idMap, structMap)
            return parser.Assignment_Expression(left, right)
        
        case parser.Var_Expression(identifier=id):
            if id in idMap:
                return parser.Var_Expression(idMap[id][0]['new_name'])
            else:
                print("Undeclared Variable {0}".format(id))
                sys.exit(1)

        case parser.Constant_Expression(const = const):
            return parser.Constant_Expression(const)

        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            #print(id)
            if id in idMap:
                newName = idMap[id][0]['new_name']

                expList = []
                if argumentList:
                    for exp in argumentList:
                        #print(i)
                        expList.append(resolveExpression(exp, idMap, structMap))
                    
                    #print(expList)

                    return parser.FunctionCall_Exp(newName, expList)

                return parser.FunctionCall_Exp(newName)
                
            else:
                print("Undeclared function {0}.".format(id))
                sys.exit(1)

            #return parser.FunctionCall_Exp(id, argumentList)
        
        case parser.Cast_Expression(targetType = targetType, exp = exp):
            newType = resolveTypeSpecifier(targetType, structMap)
            e = resolveExpression(exp, idMap, structMap)
            return parser.Cast_Expression(newType, e)

        case parser.Unary_Expression(operator=op, expression=exp):
            e = resolveExpression(exp, idMap, structMap)
            return parser.Unary_Expression(op, e)
            
        case parser.Binary_Expression(operator=op, left=left, right=right):
            l = resolveExpression(left, idMap, structMap)
            r = resolveExpression(right, idMap, structMap)

            return parser.Binary_Expression(op, l, r)
                   
        
        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            print(type(elseExp))
            c = resolveExpression(condExp, idMap, structMap)
            t = resolveExpression(thenExp, idMap, structMap)
            e = resolveExpression(elseExp, idMap, structMap)

            return parser.Conditional_Expression(c, t, e)
        
        case parser.AddrOf(exp = exp):
            e = resolveExpression(exp, idMap, structMap)
            return parser.AddrOf(e)

        case parser.Dereference(exp = exp):
            e = resolveExpression(exp, idMap, structMap)
            return parser.Dereference(e)            

        case parser.Subscript(ptrExp = ptrExp, indexExp = indexExp):
            ptrExp = resolveExpression(ptrExp, idMap, structMap)
            indexExp = resolveExpression(indexExp, idMap, structMap)
            return parser.Subscript(ptrExp, indexExp)

        case parser.StringExpression(string = string):
            return parser.StringExpression(string)

        case parser.SizeOf(exp = exp):
            exp = resolveExpression(exp, idMap, structMap)
            return parser.SizeOf(exp)

        case parser.SizeOfT(typeName = typeName):
            newType = resolveTypeSpecifier(typeName, structMap)
            return parser.SizeOfT(newType)

        case parser.Dot():
            pass

        case parser.Arrow():
            pass

        case _:
            traceback.print_stack()
            print("Invalid expression type: {0}".format(type(expression)))
            sys.exit(1)

global_value = 0

def makeTemporary(id):
    global global_value
    name = "{0}.{1}".format(id, global_value)
    global_value += 1
    return name


def resolveFunctionDeclaration(funDecl, idMap, structMap):

    if funDecl.iden in idMap:
        prev_Entry = idMap[funDecl.iden]
        if prev_Entry[1]['from_current_scope'] and not prev_Entry[2]['has_linkage']:
            print("Duplicate Declaration of {0}".format(funDecl.iden))
            sys.exit(1)
            
    idMap[funDecl.iden] = [{'new_name':funDecl.iden}, {'from_current_scope':True}, {'has_linkage':True}]
    

    newParams = []
    innerMap = copyidMap(idMap)
    for id in funDecl.paramNames:
        newParams.append(resolveID(id, innerMap))

    
    block = None
    if funDecl.block:
        block = resolveBlock(funDecl.block, innerMap, structMap)
        
    type_ = resolveTypeSpecifier(funDecl.funType, structMap)
    return parser.FunctionDecl(funDecl.iden, type_, newParams, block, funDecl.storageClass)
    


def resolveID(id, idMap):

    if id in idMap and idMap[id][1]['from_current_scope']:
        print("Variable '{0}' is already declared.".format(id))
        sys.exit(1)


    #asi esta bien!
    uniqueName = makeTemporary(id)

    idMap[id] = [{'new_name':uniqueName}, {'from_current_scope':True}, {'has_linkage':False}]

    return uniqueName

def resolveFileScopeVarDecl(dec, idMap, structMap):

    type = resolveTypeSpecifier(dec.varType, structMap)

    idMap[dec.identifier] = [{'new_name':dec.identifier}, {'from_current_scope':True}, {'has_linkage':True}]

    return parser.VariableDecl(dec.identifier, type, dec.initializer)

def resolveInitializer(initializer, idMap):
    match initializer:
        case parser.SingleInit(exp=exp):
            exp = resolveExpression(exp, idMap)
            return parser.SingleInit(exp)
            
        case parser.CompoundInit(initializerList = initializerList):
            initList = []
            for i in initializerList:
                init = resolveInitializer(i, idMap)
                initList.append(init)
    
            #print(initList)
            return parser.CompoundInit(initList)
        
        case _:
            print("Invalid initializer type: {0}".format(type(initializer)))
            sys.exit(1)

def resolveTypeSpecifier(type_, structMap):
    match type_:
        case parser.StuctureType(tag = tag):
            if tag in structMap:
                #print("Ale: ", tag)
                uniqueTag = structMap[tag].newTag
                return parser.StuctureType(uniqueTag)
            
            else:
                print("Error: Specified an undeclared structure type.")
                sys.exit(1)

        case parser.PointerType(referenceType = referenceType):
            newType = resolveTypeSpecifier(referenceType, structMap)
            return parser.PointerType(newType)

        case parser.ArrayType(elementType = elementType, size = size):
            newType = resolveTypeSpecifier(elementType, structMap)
            return parser.ArrayType(newType, size)

        case parser.FunType(paramTypes = paramTypes, retType = retType):
            
            newParamTypes = []
            for i in paramTypes:
                newType = resolveTypeSpecifier(i, structMap)
                newParamTypes.append(newType)
            
            newRetType = resolveTypeSpecifier(retType, structMap)

            return parser.FunType(newParamTypes, newRetType)

        case _:
            return type_
            
    

def resolveLocalVarDecl(dec, idMap, structMap):
    if dec.identifier in idMap:
        prevEntry = idMap[dec.identifier]
        if prevEntry[1]['from_current_scope']:
            if dec.storageClass.storageClass != parser.StorageType.EXTERN or not prevEntry[2]['has_linkage']:
                print("Conflicting declarations.".format(dec.identifier))
                sys.exit(1)

    if dec.storageClass.storageClass == parser.StorageType.EXTERN:
        return resolveFileScopeVarDecl(dec, idMap)
    else:
        type = resolveTypeSpecifier(dec.varType, structMap)

        uniqueName = resolveID(dec.identifier, idMap)
        
        if dec.initializer:
            init = resolveInitializer(dec.initializer, idMap)
            return parser.VariableDecl(uniqueName, type, init, dec.storageClass)
    
        return parser.VariableDecl(uniqueName, type, None, dec.storageClass)


def resolveVarDeclaration(dec, idMap, structMap, isBlockVar):
    if isBlockVar == False:
        return resolveFileScopeVarDecl(dec, idMap, structMap)
    else:
        return resolveLocalVarDecl(dec, idMap, structMap)

class MapEntry():
    def __init__(self, newTag, fromCurrentScope):
        self.newTag = newTag
        self.fromCurrentScope = fromCurrentScope

def resolveStructDeclaration(structDecl, structMap):
    uniqueTag = None

    if not (structDecl.tag in structMap) or not structMap[structDecl.tag].fromCurrentScope:
        uniqueTag = makeTemporary(structDecl.tag)
        structMap[structDecl.tag] = MapEntry(uniqueTag, True)
    else:
        uniqueTag = structMap[structDecl.tag].newTag
    
    processedMembers = []

    for member in structDecl.members:
        processedType = resolveTypeSpecifier(member.memberType, structMap)
        processedMembers.append(parser.MemberDecl(member.name, processedType))

    return parser.StructDeclaration(uniqueTag, processedMembers)

    


def resolveDeclaration(dec, idMap, structMap, isBlockDecl):

    match dec:
        case parser.VarDecl(variableDecl = variableDecl):
            v = resolveVarDeclaration(variableDecl, idMap, structMap, isBlockDecl)
            return parser.VarDecl(v)
            
        case parser.FunDecl(funDecl = funDecl):
            
            if isBlockDecl and funDecl.storageClass.storageClass == parser.StorageType.STATIC:
                print("Error cannot declare static function in block scope.")
                sys.exit(1)

            f = resolveFunctionDeclaration(funDecl, idMap, structMap)
            return parser.FunDecl(f)
        
        case parser.StructDecl(structDecl = structDecl):
            s = resolveStructDeclaration(structDecl, structMap)
            return parser.StructDecl(s)

        case _:
            print("Error: Declaration not resolved. {0}".format(dec))
            sys.exit(1)
            

def copyidMap(idMap):
    #print("VAR map: ", idMap)
    
    newMap = copy.deepcopy(idMap)

    for i in newMap.values():
        i[1] = {'from_current_scope':False}
    
    #print("NEW map: ", newMap)

    return newMap

def resolveForInit(forInit, idMap, structMap):
    #print(type(forInit))

    match forInit:
        case parser.InitDecl(varDecl = varDecl):
            d = resolveVarDeclaration(varDecl, idMap, structMap, True)
            return parser.InitDecl(d)
        
        case parser.InitExp(exp=exp):
            e = None
            if exp:
                e = resolveExpression(exp, idMap)

            return parser.InitExp(e)
            

def resolveStatement(statement, idMap, structMap):
    match statement:
        case parser.BreakStatement():
            return parser.BreakStatement()
        
        case parser.ContinueStatement():
            return parser.ContinueStatement()

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=identifier):
            newidMap = copyidMap(idMap)

            f = resolveForInit(forInit, newidMap, structMap)
            
            c = None
            if condExp:
                c = resolveExpression(condExp, newidMap, structMap)

            p = None
            if postExp:
                p = resolveExpression(postExp, newidMap, structMap)

            s = resolveStatement(statement, newidMap, structMap)

            return parser.ForStatement(f, s, c, p)
            

        case parser.DoWhileStatement(statement=statement, condExp=condExp, identifier=id):
            s = resolveStatement(statement, idMap, structMap)
            c = resolveExpression(condExp, idMap, structMap)
            return parser.DoWhileStatement(s, c)

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):
            c = resolveExpression(condExp, idMap, structMap)
            s = resolveStatement(statement, idMap, structMap)
            return parser.WhileStatement(c, s)
            
        case parser.ExpressionStmt(exp=exp):
            return parser.ExpressionStmt(resolveExpression(exp, idMap, structMap))
        
        case parser.ReturnStmt(expression=exp):
            if exp: 
                return parser.ReturnStmt(resolveExpression(exp, idMap, structMap))
            
            return parser.ReturnStmt()
        
        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            p = resolveExpression(exp, idMap, structMap)

            t = resolveStatement(thenS, idMap, structMap)
            e = resolveStatement(elseS, idMap, structMap)

            return parser.IfStatement(p, t, e)
        
        case parser.CompoundStatement(block=block):
            newidMap = copyidMap(idMap)
            return parser.CompoundStatement(resolveBlock(block, newidMap, structMap))
            
        case parser.NullStatement():
            return parser.NullStatement()
            
def resolveBlock(block, idMap, structMap):

    if block.blockItemList:
        blockItemList = []
        
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    Decl = resolveDeclaration(dec, idMap, structMap, True)
                    blockItemList.append(parser.D(Decl))

                case parser.S(statement=statement):
                    s = resolveStatement(statement, idMap, structMap)
                    blockItemList.append(parser.S(s))
        
        return parser.Block(blockItemList)

    return parser.Block()
    

def IdentifierResolution(pro):
    
    if pro.declList:
        structureTypeMap = {}
        idMap = {}
        funcDecList = []
        for decl in pro.declList:
            f = resolveDeclaration(decl, idMap, structureTypeMap, False)
            funcDecList.append(f)
            
        return parser.Program(funcDecList)

    return parser.Program()

