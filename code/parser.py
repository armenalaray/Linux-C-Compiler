import sys
from token import TokenType

class Program:

    def __init__(self, function):
        self.function = function

class Function:
    
    def __init__(self, iden, stment):
        self.iden = iden
        self.statement = stment
        
class ReturnStmt:
    def __init__(self, retVal):
        self.expression = retVal

class Expression:
    intValue = 0
    def __init__(self, intValue):
        self.intValue = intValue
        

def takeToken(tokenList):
    return tokenList.pop(0)

def expect(expected, tokenList):
    actual = takeToken(tokenList)[1]
    print(actual)
    if actual != expected:
        print("Syntax Error Expected: {0} got: {1}".format(expected, actual))
        sys.exit(1)
    
def parseInt(tokenList):
    return int(takeToken(tokenList)[0])
    
def parseExp(tokenList):
    intValue = parseInt(tokenList)
    return Expression(intValue)
    
def parseStatement(tokenList):
    expect(TokenType.RETURN_KW, tokenList)
    retVal = parseExp(tokenList)
    expect(TokenType.SEMICOLON, tokenList)
    return ReturnStmt(retVal) 

def parseIdentifier(tokenList):
    return takeToken(tokenList)[0]

def parseFunction(tokenList):
    expect(TokenType.INT_KW, tokenList)
    iden = parseIdentifier(tokenList)
    expect(TokenType.OPEN_PAREN, tokenList)
    expect(TokenType.VOID_KW, tokenList)
    expect(TokenType.CLOSE_PAREN, tokenList)
    expect(TokenType.OPEN_BRACE, tokenList)
    stment = parseStatement(tokenList)
    expect(TokenType.CLOSE_BRACE, tokenList)
    return Function(iden, stment)

def parseProgram(tokenList):
    fun = parseFunction(tokenList)
    return Program(fun)
    

