import copy
import sys
import parser

def resolveExpression(exp, varMap):
    match exp:
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            #print(type(lvalue))
            if type(lvalue) != parser.Var_Expression:
                print("Invalid lvalue!")
                sys.exit(1)
            left = resolveExpression(lvalue, varMap)
            right = resolveExpression(exp, varMap)
            return parser.Assignment_Expression(left, right)
        
        case parser.Var_Expression(identifier=id):
            if id in varMap:
                return parser.Var_Expression(varMap[id][0])
            else:
                print("Undeclared Variable!")
                sys.exit(1)

        case parser.Constant_Expression(intValue=intValue):
            return parser.Constant_Expression(intValue)

        case parser.Unary_Expression(operator=op, expression=exp):
            #print(type(exp))
            e = resolveExpression(exp, varMap)
            return parser.Unary_Expression(op, e)
            
        case parser.Binary_Expression(operator=op, left=left, right=right):
            l = resolveExpression(left, varMap)
            r = resolveExpression(right, varMap)

            return parser.Binary_Expression(op, l, r)
            pass            
        
        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            print(type(elseExp))
            c = resolveExpression(condExp, varMap)
            t = resolveExpression(thenExp, varMap)
            e = resolveExpression(elseExp, varMap)

            return parser.Conditional_Expression(c, t, e)
            

        case _:
            print("Invalid expression type.")
            sys.exit(1)

global_value = 0

def makeTemporary(id):
    global global_value
    name = "{0}.{1}".format(id, global_value)
    #print(name)
    global_value += 1
    return name

def resolveDeclaration(dec, varMap):
    if dec.identifier in varMap and varMap[dec.identifier][1]:
        print("Variable is already declared.")
        sys.exit(1)

    #asi esta bien!
    uniqueName = makeTemporary(dec.identifier)
    varMap[dec.identifier] = [uniqueName, True]

    if dec.exp:
        exp = resolveExpression(dec.exp, varMap)
        return parser.Declaration(uniqueName, exp)
    
    return parser.Declaration(uniqueName)

def copyVarMap(varMap):
    print("VAR map: ", varMap)
    
    newMap = copy.deepcopy(varMap)
    for i in newMap.values():
        i[1] = False
    
    print("NEW map: ", newMap)

    return newMap

def resolveForInit(forInit, varMap):
    print(type(forInit))

    match forInit:
        case parser.InitDecl(decl=decl):
            d = resolveDeclaration(decl, varMap)
            return parser.InitDecl(d)
        
        case parser.InitExp(exp=exp):
            e = None
            if exp:
                e = resolveExpression(exp, varMap)

            return parser.InitExp(e)
            

def resolveStatement(statement, varMap):
    match statement:
        case parser.BreakStatement():
            return parser.BreakStatement()
        
        case parser.ContinueStatement():
            return parser.ContinueStatement()

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=identifier):
            newVarMap = copyVarMap(varMap)

            f = resolveForInit(forInit, newVarMap)
            
            c = None
            if condExp:
                c = resolveExpression(condExp, newVarMap)

            p = None
            if postExp:
                p = resolveExpression(postExp, newVarMap)

            s = resolveStatement(statement, newVarMap)

            return parser.ForStatement(f, s, c, p)
            

        case parser.DoWhileStatement(statement=statement, condExp=condExp, identifier=id):
            s = resolveStatement(statement, varMap)
            c = resolveExpression(condExp, varMap)
            return parser.DoWhileStatement(s, c)

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):
            c = resolveExpression(condExp, varMap)
            s = resolveStatement(statement, varMap)
            return parser.WhileStatement(c, s)
            
        case parser.ExpressionStmt(exp=exp):
            return parser.ExpressionStmt(resolveExpression(exp, varMap))
        
        case parser.ReturnStmt(expression=exp):
            return parser.ReturnStmt(resolveExpression(exp, varMap))
        
        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            #print(type(exp))
            p = resolveExpression(exp, varMap)

            t = resolveStatement(thenS, varMap)
            e = resolveStatement(elseS, varMap)

            return parser.IfStatement(p, t, e)
        
        case parser.CompoundStatement(block=block):
            newVarMap = copyVarMap(varMap)
            return parser.CompoundStatement(resolveBlock(block, newVarMap))
            
        case parser.NullStatement():
            return parser.NullStatement()
            
def resolveBlock(block, varMap):
    blockItemList = []

    for i in block.blockItemList:
        match i:
            case parser.D(declaration=dec):
                Decl = resolveDeclaration(dec, varMap)
                blockItemList.append(parser.D(Decl))

            case parser.S(statement=statement):
                s = resolveStatement(statement, varMap)
                blockItemList.append(parser.S(s))

    return parser.Block(blockItemList)
    

def variableResolution(pro):
    
    varMap = {}
    block = resolveBlock(pro.function.block, varMap)
    pro.function.block = block

    return pro

