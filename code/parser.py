import sys
from ctoken import TokenType
from enum import Enum

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

class Unary_Expression(Expression):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

class OperatorType(Enum):
    NEGATE = 1
    COMPLEMENT = 2

class Operator:
    pass

class UnaryOperator(Operator):
    def __init__(self, operator):
        self.operator = operator
    

def takeToken(tokenList):
    if(tokenList != []):
        return tokenList.pop(0)
    return ()

def peek(tokenList):
    return tokenList[0]

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



def parseUnop(tokenList):
    actual = takeToken(tokenList)
    if actual != ():
        match actual[1]:
            case TokenType.HYPHEN:
                return UnaryOperator(OperatorType.NEGATE)
            case TokenType.TILDE:
                return UnaryOperator(OperatorType.COMPLEMENT)
            case _:
                print("Syntax Error Expected an Unary Operator but: {0}".format(actual))
                sys.exit(1)            
        
    print("Syntax Error Expected an Unary Operator but there are no more tokens.")
    sys.exit(1)

    
    
def parseExp(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.CONSTANT:
        intValue = parseInt(tokenList)
        return Constant_Expression(intValue)
    
    elif token[1] == TokenType.TILDE or token[1] == TokenType.HYPHEN:
        operator = parseUnop(tokenList)
        inner_exp = parseExp(tokenList)
        return Unary_Expression(operator, inner_exp)
        
    elif token[1] == TokenType.OPEN_PAREN:
        takeToken(tokenList)
        inner_exp = parseExp(tokenList)
        expect(TokenType.CLOSE_PAREN, tokenList)
        return inner_exp
        
    else:
        print("Malformed expression.")
        sys.exit(1)

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
    

