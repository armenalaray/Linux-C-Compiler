import sys
from enum import Enum

import parser

class IDType(Enum):
    FUNCTION = 1
    INT = 2

class FunType:
    def __init__(self, paramCount):
        self.paramCount = paramCount
    
    def __ne__(self, value):
        #print(self, value)
        result = self.paramCount != value.paramCount
        #print(result)
        return result
    
    def __str__(self):
        return "FunType(int {self.paramCount})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

def typeCheckExpression(exp, symbolTable):
    match exp:
        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            
            if symbolTable[id][0] == IDType.INT:
                print("Error: Variable {0} used as function name.".format(id))
                sys.exit(1)

            #es una funcion, parametrizaje
            paramCount = 0
            if argumentList:
                paramCount = len(argumentList)

            if symbolTable[id][1].paramCount != paramCount:
                #print(paramCount)
                print("Error: Function {0}() called with the wrong number of arguments.".format(id))
                sys.exit(1)
            
            if argumentList:
                for exp in argumentList:
                    typeCheckExpression(exp, symbolTable)
                    

        case parser.Var_Expression(identifier=id):
            if symbolTable[id][0] != IDType.INT:
                #symbolTable[id][1]
                print("ERROR: Function {0}() used as variable.".format(id))
                sys.exit(1)
        
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            print(lvalue)
            typeCheckExpression(lvalue, symbolTable)
            typeCheckExpression(exp, symbolTable)

        case parser.Constant_Expression(intValue=intValue):
            pass 

        case parser.Unary_Expression(operator=op, expression=exp):
            pass               

        case parser.Binary_Expression(operator=op, left=left, right=right):
            pass

        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            pass

        case _:
            print(type(exp))
            print("Invalid expression type.")
            sys.exit(1)

def typeCheckVarDeclaration(VarDecl, symbolTable):
    symbolTable[VarDecl.identifier] = (IDType.INT,)
    if VarDecl.exp:
        typeCheckExpression(VarDecl.exp, symbolTable)
        #print(type(VarDecl.exp))
        

def typeCheckDeclaration(dec, symbolTable):
    match dec:
        case parser.VarDecl(variableDecl = variableDecl):
            typeCheckVarDeclaration(variableDecl, symbolTable)
            
        case parser.FunDecl(funDecl = funDecl):
            typeCheckFunctionDeclaration(funDecl, symbolTable)

def typeCheckStatement(statement, symbolTable):
    pass

def typeCheckBlock(block, symbolTable):
    if block.blockItemList:
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    typeCheckDeclaration(dec, symbolTable)
                    
                case parser.S(statement=statement):
                    typeCheckStatement(statement, symbolTable)
                    pass
                    #resolveStatement(statement, idMap)
                    
        
def typeCheckFunctionDeclaration(funDec, symbolTable):
    funType = FunType(len(funDec.paramList))
    hasBody = funDec.block is not None
    alreadyDefined = False

    if funDec.iden in symbolTable:
        oldDecl = symbolTable[funDec.iden]
        #print(funDec.iden, oldDecl[0])
        #tu ya checaste que no es una variable!
        #aqui si son funciones

        if oldDecl[0] != IDType.FUNCTION:
            print("Error: OldType was not a function.")
            sys.exit(1)

        if oldDecl[1] != funType:
            print("Error: Incompatible function declarations.")
            sys.exit(1)

        alreadyDefined = oldDecl[2]

        if alreadyDefined and hasBody:
            print("Error: function is defined more than once.")
            sys.exit(1)

    symbolTable[funDec.iden] = (IDType.FUNCTION, funType, alreadyDefined or hasBody)

    if hasBody:
        for param in funDec.paramList:
            #print(type(param))
            symbolTable[param] = (IDType.INT, )
        
        typeCheckBlock(funDec.block, symbolTable)
    

def typeCheckProgram(pro):

    symbolTable = {}
    
    if pro.funcDeclList:
        
        for funDec in pro.funcDeclList:
            typeCheckFunctionDeclaration(funDec, symbolTable)

    return pro, symbolTable

    pass