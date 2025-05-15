import copy
import sys
import parser

def resolveExpression(exp, idMap):
    match exp:        
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            #print(type(lvalue))
            if type(lvalue) != parser.Var_Expression:
                print("Invalid lvalue!")
                sys.exit(1)
            left = resolveExpression(lvalue, idMap)
            right = resolveExpression(exp, idMap)
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
                        expList.append(resolveExpression(exp, idMap))
                    
                    #print(expList)

                    return parser.FunctionCall_Exp(newName, expList)

                return parser.FunctionCall_Exp(newName)
                
            else:
                print("Undeclared function {0}.".format(id))
                sys.exit(1)

            #return parser.FunctionCall_Exp(id, argumentList)
        
        case parser.Cast_Expression(targetType = targetType, exp = exp):
            e = resolveExpression(exp, idMap)
            return parser.Cast_Expression(targetType, e)

        case parser.Unary_Expression(operator=op, expression=exp):
            #print(type(exp))
            e = resolveExpression(exp, idMap)
            return parser.Unary_Expression(op, e)
            
        case parser.Binary_Expression(operator=op, left=left, right=right):
            l = resolveExpression(left, idMap)
            r = resolveExpression(right, idMap)

            return parser.Binary_Expression(op, l, r)
            pass            
        
        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            print(type(elseExp))
            c = resolveExpression(condExp, idMap)
            t = resolveExpression(thenExp, idMap)
            e = resolveExpression(elseExp, idMap)

            return parser.Conditional_Expression(c, t, e)

        case _:
            #print(type(exp))
            print("Invalid expression type: {0}".format(type(exp)))
            sys.exit(1)

global_value = 0

def makeTemporary(id):
    global global_value
    name = "{0}.{1}".format(id, global_value)
    #print(name)
    global_value += 1
    return name


def resolveFunctionDeclaration(funDecl, idMap):
    #print(funDecl)
    #YOUAREHERE!
    if funDecl.iden in idMap:
        prev_Entry = idMap[funDecl.iden]
        if prev_Entry[1]['from_current_scope'] and not prev_Entry[2]['has_linkage']:
            print("Duplicate Declaration of {0}".format(funDecl.iden))
            sys.exit(1)
            
    idMap[funDecl.iden] = [{'new_name':funDecl.iden}, {'from_current_scope':True}, {'has_linkage':True}]
    #print(idMap)

    newParams = []
    innerMap = copyidMap(idMap)
    for id in funDecl.paramNames:
        #ERROR: Change this to resolveVarLocalDeclaration
        newParams.append(resolveID(id, innerMap))

    
    block = None
    if funDecl.block:
        block = resolveBlock(funDecl.block, innerMap)
        
    return parser.FunctionDecl(funDecl.iden, funDecl.funType, newParams, block, funDecl.storageClass)
    


def resolveID(id, idMap):

    if id in idMap and idMap[id][1]['from_current_scope']:
        print("Variable '{0}' is already declared.".format(id))
        sys.exit(1)


    #asi esta bien!
    uniqueName = makeTemporary(id)

    idMap[id] = [{'new_name':uniqueName}, {'from_current_scope':True}, {'has_linkage':False}]

    return uniqueName

def resolveFileScopeVarDecl(dec, idMap):
    idMap[dec.identifier] = [{'new_name':dec.identifier}, {'from_current_scope':True}, {'has_linkage':True}]

    return dec

def resolveLocalVarDecl(dec, idMap):

    if dec.identifier in idMap:
        prevEntry = idMap[dec.identifier]
        if prevEntry[1]['from_current_scope']:
            if dec.storageClass.storageClass != parser.StorageType.EXTERN or not prevEntry[2]['has_linkage']:
                print("Conflicting declarations.".format(dec.identifier))
                sys.exit(1)

    if dec.storageClass.storageClass == parser.StorageType.EXTERN:
        return resolveFileScopeVarDecl(dec, idMap)
    else:
        uniqueName = resolveID(dec.identifier, idMap)
        if dec.exp:
            exp = resolveExpression(dec.exp, idMap)
            return parser.VariableDecl(uniqueName, dec.varType, exp, dec.storageClass)
    
        return parser.VariableDecl(uniqueName, dec.varType, None, dec.storageClass)


def resolveVarDeclaration(dec, idMap, isBlockVar):
    if isBlockVar == False:
        return resolveFileScopeVarDecl(dec, idMap)
    else:
        return resolveLocalVarDecl(dec, idMap)

def resolveDeclaration(dec, idMap, isBlockDecl):

    match dec:
        case parser.VarDecl(variableDecl = variableDecl):
            v = resolveVarDeclaration(variableDecl, idMap, isBlockDecl)
            return parser.VarDecl(v)
            
        case parser.FunDecl(funDecl = funDecl):
            
            if isBlockDecl and funDecl.storageClass.storageClass == parser.StorageType.STATIC:
                print("Error cannot declare static function in block scope.")
                sys.exit(1)

            f = resolveFunctionDeclaration(funDecl, idMap)
            return parser.FunDecl(f)
            

def copyidMap(idMap):
    #print("VAR map: ", idMap)
    
    newMap = copy.deepcopy(idMap)

    for i in newMap.values():
        i[1] = {'from_current_scope':False}
    
    #print("NEW map: ", newMap)

    return newMap

def resolveForInit(forInit, idMap):
    #print(type(forInit))

    match forInit:
        case parser.InitDecl(varDecl = varDecl):
            #print(type(varDecl))
            d = resolveVarDeclaration(varDecl, idMap, True)
            return parser.InitDecl(d)
        
        case parser.InitExp(exp=exp):
            e = None
            if exp:
                e = resolveExpression(exp, idMap)

            return parser.InitExp(e)
            

def resolveStatement(statement, idMap):
    match statement:
        case parser.BreakStatement():
            return parser.BreakStatement()
        
        case parser.ContinueStatement():
            return parser.ContinueStatement()

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=identifier):
            newidMap = copyidMap(idMap)

            f = resolveForInit(forInit, newidMap)
            
            c = None
            if condExp:
                c = resolveExpression(condExp, newidMap)

            p = None
            if postExp:
                p = resolveExpression(postExp, newidMap)

            s = resolveStatement(statement, newidMap)

            return parser.ForStatement(f, s, c, p)
            

        case parser.DoWhileStatement(statement=statement, condExp=condExp, identifier=id):
            s = resolveStatement(statement, idMap)
            c = resolveExpression(condExp, idMap)
            return parser.DoWhileStatement(s, c)

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):
            c = resolveExpression(condExp, idMap)
            s = resolveStatement(statement, idMap)
            return parser.WhileStatement(c, s)
            
        case parser.ExpressionStmt(exp=exp):
            return parser.ExpressionStmt(resolveExpression(exp, idMap))
        
        case parser.ReturnStmt(expression=exp):
            return parser.ReturnStmt(resolveExpression(exp, idMap))
        
        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            #print(type(exp))
            p = resolveExpression(exp, idMap)

            t = resolveStatement(thenS, idMap)
            e = resolveStatement(elseS, idMap)

            return parser.IfStatement(p, t, e)
        
        case parser.CompoundStatement(block=block):
            newidMap = copyidMap(idMap)
            return parser.CompoundStatement(resolveBlock(block, newidMap))
            
        case parser.NullStatement():
            return parser.NullStatement()
            
def resolveBlock(block, idMap):

    if block.blockItemList:
        blockItemList = []
        
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    Decl = resolveDeclaration(dec, idMap, True)
                    blockItemList.append(parser.D(Decl))

                case parser.S(statement=statement):
                    s = resolveStatement(statement, idMap)
                    blockItemList.append(parser.S(s))
        
        return parser.Block(blockItemList)

    return parser.Block()
    

def IdentifierResolution(pro):
    
    if pro.declList:
        idMap = {}
        funcDecList = []
        for decl in pro.declList:
            f = resolveDeclaration(decl, idMap, False)
            funcDecList.append(f)
            
        return parser.Program(funcDecList)

    return parser.Program()

