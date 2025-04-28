import sys
import parser

def resolveExpression(exp, varMap):
    pass

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
        sys.exit(0)

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
            pass
        case parser.ReturnStmt():
            pass
        case parser.NullStatement():
            pass

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

