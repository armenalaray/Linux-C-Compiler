import sys
from enum import Enum

import parser

class IDType(Enum):
    INT = 1

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

def typeCheckVarDeclaration(VarDecl, symbolTable):
    pass


def typeCheckDeclaration(dec, symbolTable):
    match dec:
        case parser.VarDecl(variableDecl = variableDecl):
            typeCheckVarDeclaration(variableDecl, symbolTable)
            
        case parser.FunDecl(funDecl = funDecl):
            typeCheckFunctionDeclaration(funDecl, symbolTable)

def typeCheckBlock(block, symbolTable):
    if block.blockItemList:
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    typeCheckDeclaration(dec, symbolTable)
                    
                case parser.S(statement=statement):
                    pass
                    #resolveStatement(statement, idMap)
                    
        
def typeCheckFunctionDeclaration(funDec, symbolTable):
    funType = FunType(len(funDec.paramList))
    hasBody = funDec.block is not None
    #print(hasBody)

    alreadyDefined = False

    if funDec.iden in symbolTable:
        oldDecl = symbolTable[funDec.iden]
        #print(funDec.iden, oldDecl[0])
        if oldDecl[0] != funType:
            print("Error: Incompatible function declarations.")
            sys.exit(1)
        alreadyDefined = oldDecl[1]
        if alreadyDefined and hasBody:
            print("Error: function is defined more than once.")
            sys.exit(1)

    symbolTable[funDec.iden] = (funType, alreadyDefined or hasBody)

    if hasBody:
        for param in funDec.paramList:
            #print(type(param))
            symbolTable[param] = (IDType.INT)
        
        typeCheckBlock(funDec.block, symbolTable)
    

def typeCheckProgram(pro):

    symbolTable = {}
    
    if pro.funcDeclList:
        
        for funDec in pro.funcDeclList:
            typeCheckFunctionDeclaration(funDec, symbolTable)

    return pro, symbolTable

    pass