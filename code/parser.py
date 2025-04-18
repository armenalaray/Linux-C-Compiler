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
    if(tokenList != []):
        return tokenList.pop(0)
    return ()

def expect(expected, tokenList):
    actual = takeToken(tokenList)
    
    print("actual: ", actual)
    if actual != ():
        if actual[1] != expected:
            print("Syntax Error Expected: {0} got: {1}.".format(expected, actual))
            sys.exit(1)
    else:
        print("Syntax Error Expected: {0} but there are no more tokens.".format(expected))
        sys.exit(1)
    
    
    
def parseInt(tokenList):
    actual = takeToken(tokenList)
    if actual != ():
        return int(actual[0])
    
    print("Syntax Error Expected an int value but there are no more tokens.")
    sys.exit(1)
    
    
def parseExp(tokenList):
    intValue = parseInt(tokenList)
    return Expression(intValue)
    
def parseStatement(tokenList):
    expect(TokenType.RETURN_KW, tokenList)
    retVal = parseExp(tokenList)
    expect(TokenType.SEMICOLON, tokenList)
    return ReturnStmt(retVal) 

def parseIdentifier(tokenList):
    actual = takeToken(tokenList)
    if actual != ():
        return actual[0]
    
    print("Syntax Error Expected an identifier but there are no more tokens.")
    sys.exit(1)


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
    

