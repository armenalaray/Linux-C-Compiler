import parser

def printVarDecl(variableDecl, output, level):
    output += "{self.storageClass} {self.varType} {self.identifier} = {self.exp}".format(variableDecl.storageClass, variableDecl.varType, variableDecl.identifier, variableDecl.exp)
    

def printDeclaration(decl, output, level):

    match decl:
        case parser.VarDecl(variableDecl = variableDecl):
            output += "VarDecl: \n"
            printVarDecl(variableDecl, output, level)
            pass
        case parser.FunDecl(funDecl = funDecl):
            pass
    
    return output

def printProgram(pro):
    output = 'AST Program:\n'

    level = 1
    for decl in pro.declList:
        output = printDeclaration(decl, output, level)

    print(output)
    
    