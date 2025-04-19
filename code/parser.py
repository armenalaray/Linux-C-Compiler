import sys
from ctoken import TokenType

class Program:

    def __init__(self, function):
        self.function = function

class Function:
    
    def __init__(self, iden, statement):
        self.iden = iden
        self.statement = statement
        
class Statement:
    pass

class ReturnStmt(Statement):
    def __init__(self, retVal):
        self.expression = retVal

class Expression:
    pass

class Null_Expression(Expression):
    pass

class Constant_Expression(Expression):
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
        if actual[1] == TokenType.CONSTANT:
            return actual[0]
        
        print("Syntax Error Expected TokenType.CONSTANT but got {0}.".format(actual[1]))
        sys.exit(1)    
    
    print("Syntax Error Expected an int value but there are no more tokens.")
    sys.exit(1)
    
    
def parseExp(tokenList):
    intValue = parseInt(tokenList)
    return Constant_Expression(intValue)
    
def parseStatement(tokenList):
    expect(TokenType.RETURN_KW, tokenList)
    retVal = parseExp(tokenList)
    expect(TokenType.SEMICOLON, tokenList)
    return ReturnStmt(retVal) 

def parseIdentifier(tokenList):
    actual = takeToken(tokenList)
    
    if actual != ():
        if actual[1] == TokenType.IDENTIFIER:
            return actual[0]
        
        print("Syntax Error Expected TokenType.IDENTIFIER but got {0}.".format(actual[1]))
        sys.exit(1)    
    
    
    print("Syntax Error Expected an identifier but there are no more tokens.")
    sys.exit(1)


def parseFunction(tokenList):
    expect(TokenType.INT_KW, tokenList)
    iden = parseIdentifier(tokenList)
    expect(TokenType.OPEN_PAREN, tokenList)
    expect(TokenType.VOID_KW, tokenList)
    expect(TokenType.CLOSE_PAREN, tokenList)
    expect(TokenType.OPEN_BRACE, tokenList)
    statement = parseStatement(tokenList)
    expect(TokenType.CLOSE_BRACE, tokenList)
    return Function(iden, statement)

def parseProgram(tokenList):
    fun = parseFunction(tokenList)
    return Program(fun)
    

