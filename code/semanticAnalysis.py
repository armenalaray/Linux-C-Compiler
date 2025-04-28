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
                return parser.Var_Expression(varMap[id])
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
    if dec.identifier in varMap:
        print("Variable is already declared.")
        sys.exit(1)

    #asi esta bien!
    uniqueName = makeTemporary(dec.identifier)
    varMap[dec.identifier] = uniqueName

    if dec.exp:
        exp = resolveExpression(dec.exp, varMap)
        return parser.Declaration(uniqueName, exp)
    
    return parser.Declaration(uniqueName)

def resolveStatement(statement, varMap):
    match statement:
        case parser.ExpressionStmt(exp=exp):
            return parser.ExpressionStmt(resolveExpression(exp, varMap))
        case parser.ReturnStmt(expression=exp):
            return parser.ReturnStmt(resolveExpression(exp, varMap))
        case parser.NullStatement():
            return parser.NullStatement()
            

def variableResolution(pro):
    
    varMap = {}
    for i in pro.function.blockItemList:
        match i:
            case parser.D(declaration=dec):
                Decl = resolveDeclaration(dec, varMap)
                i.declaration = Decl
            case parser.S(statement=statement):
                s = resolveStatement(statement, varMap)
                i.statement = s
                
                
            
    return pro

