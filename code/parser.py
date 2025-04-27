import sys
from ctoken import TokenType
from enum import Enum

class Program:

    def __init__(self, function):
        self.function = function
    
    def __str__(self):
        return "AST Program:\n\t{self.function}".format(self=self)

class Function:
    
    def __init__(self, iden, blockItemList):
        self.iden = iden
        self.blockItemList = blockItemList
    
    def __str__(self):

        return "Function: {self.iden}\n\t\tList: {self.blockItemList}".format(self=self)

class BlockItem:
    pass

class S(BlockItem):
    def __init__(self, statement):
        self.statement = statement
    
    def __str__(self):
        return "Statement: {self.statement}".format(self=self)

    def __repr__(self):
        return self.__str__()
        
class D(BlockItem):
    def __init__(self, declaration):
        self.declaration = declaration
    
    def __str__(self):
        return "Declaration: {self.declaration}".format(self=self)

    def __repr__(self):
        return self.__str__()

class Statement:
    pass

class ReturnStmt(Statement):
    def __init__(self, exp):
        self.expression = exp

    def __str__(self):
        #super().__str__()
        return "return {self.expression}".format(self=self)

class ExpressionStmt(Statement):
    def __init__(self, exp):
        self.exp = exp
    
    def __str__(self):
        return "{self.exp}".format(self=self)

class NullStatement(Statement):
    def __init__(self):
        pass

class Decl:
    pass

class Declaration(Decl):
    def __init__(self, identifier, exp=None):
        self.identifier = identifier
        self.exp = exp
    
    def __str__(self):
        return "{self.identifier} = {self.exp}".format(self=self)

class Expression:
    pass

class Null_Expression(Expression):
    pass

class Constant_Expression(Expression):
    def __init__(self, intValue):
        self.intValue = intValue
    
    def __str__(self):
        #super().__str__()
        return "{self.intValue}".format(self=self)

class Unary_Expression(Expression):
    def __init__(self, operator, expression):
        self.operator = operator
        self.expression = expression

    def __str__(self):
        #super().__str__()
        return "Unary Expression: Operator: {self.operator} Expression: {self.expression}".format(self=self)

class Binary_Expression:
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        #super().__str__()
        return "Binary Expression: Operator: {self.operator} Left: {self.left} Right: {self.right}".format(self=self)

class Var_Expression:
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "{self.identifier}".format(self=self)

class Assignment_Expression:
    def __init__(self, lvalue, exp):
        self.lvalue = lvalue
        self.exp = exp

    def __str__(self):
        return "{self.lvalue} = {self.exp}".format(self=self)

class UnopType(Enum):
    NEGATE = 1
    COMPLEMENT = 2
    NOT = 3

class BinopType(Enum):
    SUBTRACT = 1
    ADD = 2
    MULTIPLY = 3
    DIVIDE = 4
    MODULO = 5
    AND = 6
    OR = 7
    EQUAL = 8
    NOTEQUAL = 9
    LESSTHAN = 10
    LESSOREQUAL = 11
    GREATERTHAN = 12
    GREATEROREQUAL = 13

class Operator:
    pass

class UnaryOperator(Operator):
    def __init__(self, operator):
        self.operator = operator
    
    def __str__(self):
        #super().__str__()
        return "{self.operator}".format(self=self) 

class BinaryOperator(Operator):
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        #super().__str__()
        return "{self.operator}".format(self=self) 

def takeToken(tokenList):
    if(tokenList != []):
        return tokenList.pop(0)
    return ()

def peek(tokenList):
    return tokenList[0]

def expect(expected, tokenList):
    actual = takeToken(tokenList)
    
    #print("actual: ", actual)
    if actual != ():
        if actual[1] != expected:
            print("Syntax Error Expected: {0} got: {1} at Line {2}.".format(expected, actual[0], actual[2]))
            sys.exit(1)
    else:
        print("Syntax Error Expected: {0} but there are no more tokens.".format(expected))
        sys.exit(1)
    
    
    
def parseInt(tokenList):
    actual = takeToken(tokenList)
    if actual != ():
        if actual[1] == TokenType.CONSTANT:
            return actual[0]
        
        print("Syntax Error Expected TokenType.CONSTANT but got {0} at Line {1}.".format(actual[1], actual[2]))
        sys.exit(1)    
    
    print("Syntax Error Expected an int value but there are no more tokens.")
    sys.exit(1)



def parseUnop(tokenList):
    actual = takeToken(tokenList)
    if actual != ():
        match actual[1]:
            case TokenType.HYPHEN:
                return UnaryOperator(UnopType.NEGATE)
            case TokenType.TILDE:
                return UnaryOperator(UnopType.COMPLEMENT)
            case TokenType.EXCLAMATION:
                return UnaryOperator(UnopType.NOT)
            case _:
                print("Syntax Error Expected an Unary Operator but: {0} at Line {1}".format(actual[0], actual[2]))
                sys.exit(1)            
        
    print("Syntax Error Expected an Unary Operator but there are no more tokens.")
    sys.exit(1)

def parseBinop(tokenList):
    actual = takeToken(tokenList)
    if actual != ():
        match actual[1]:
            case TokenType.HYPHEN:
                return BinaryOperator(BinopType.SUBTRACT)
            case TokenType.PLUS:
                return BinaryOperator(BinopType.ADD)
            case TokenType.FORWARD_SLASH:
                return BinaryOperator(BinopType.DIVIDE)
            case TokenType.ASTERISK:
                return BinaryOperator(BinopType.MULTIPLY)
            case TokenType.PERCENT:
                return BinaryOperator(BinopType.MODULO)
            case TokenType.LESST:
                return BinaryOperator(BinopType.LESSTHAN)
            case TokenType.GREATERT:
                return BinaryOperator(BinopType.GREATERTHAN)
            case TokenType.LESSTEQUALT:
                return BinaryOperator(BinopType.LESSOREQUAL)
            case TokenType.GREATERTEQUALT:
                return BinaryOperator(BinopType.GREATEROREQUAL)
            case TokenType.TEQUALS:
                return BinaryOperator(BinopType.EQUAL)
            case TokenType.EXCLAMATIONEQUAL:
                return BinaryOperator(BinopType.NOTEQUAL)
            case TokenType.TAMPERSANDS:
                return BinaryOperator(BinopType.AND)
            case TokenType.TVERTICALB:
                return BinaryOperator(BinopType.OR)
            case _:
                print("Syntax Error Expected a Binary Operator but: {0} at Line {1}".format(actual[0], actual[2]))
                sys.exit(1)            
    
    
def parseFactor(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.CONSTANT:
        intValue = parseInt(tokenList)
        return Constant_Expression(intValue)
    
    elif token[1] == TokenType.IDENTIFIER:
        id = parseIdentifier(tokenList)
        return Var_Expression(id)

    elif token[1] == TokenType.TILDE or token[1] == TokenType.HYPHEN or token[1] == TokenType.EXCLAMATION:
        operator = parseUnop(tokenList)
        inner_exp = parseFactor(tokenList)
        return Unary_Expression(operator, inner_exp)
        
    elif token[1] == TokenType.OPEN_PAREN:
        takeToken(tokenList)
        inner_exp = parseExp(tokenList, 0)
        expect(TokenType.CLOSE_PAREN, tokenList)
        return inner_exp
        
    else:
        print("Malformed expression at Line {0}.".format(token[2]))
        sys.exit(1)


precTable = {
    TokenType.ASTERISK : 50, 
    TokenType.FORWARD_SLASH : 50,
    TokenType.PERCENT : 50,
    TokenType.PLUS : 45,
    TokenType.HYPHEN : 45,
    TokenType.LESST : 35,
    TokenType.LESSTEQUALT : 35,
    TokenType.GREATERT : 35,
    TokenType.GREATERTEQUALT : 35,
    TokenType.TEQUALS : 30,
    TokenType.EXCLAMATIONEQUAL : 30,
    TokenType.TAMPERSANDS : 10,
    TokenType.TVERTICALB : 5,
    TokenType.EQUAL : 1
    }

def precedence(token):
    if token != ():
        return precTable[token[1]]
    
    print("Syntax Error Expected a token but there are no more tokens.")
    sys.exit(1)


def BinaryOperatorToken(token):
    if token != ():
        
        if token[1] == TokenType.ASTERISK or token[1] == TokenType.PLUS or token[1] == TokenType.FORWARD_SLASH or token[1] == TokenType.PERCENT or token[1] == TokenType.HYPHEN or token[1] == TokenType.TAMPERSANDS or token[1] == TokenType.TVERTICALB or token[1] == TokenType.TEQUALS or token[1] == TokenType.EXCLAMATIONEQUAL or token[1] == TokenType.LESSTEQUALT or token[1] == TokenType.GREATERTEQUALT or token[1] == TokenType.GREATERT or token[1] == TokenType.LESST or token[1] == TokenType.EQUAL:
            return True
        
    return False

def parseExp(tokenList, min_prec):
    #breakpoint()
    left = parseFactor(tokenList)
    next_token = peek(tokenList)
    while BinaryOperatorToken(next_token) and precedence(next_token) >= min_prec:
        if next_token[1] == TokenType.EQUAL:
            takeToken(tokenList)
            right = parseExp(tokenList, precedence(next_token))
            left = Assignment_Expression(left, right)
        else:
            op = parseBinop(tokenList)
            right = parseExp(tokenList, precedence(next_token) + 1)
            left = Binary_Expression(op, left, right)
        next_token = peek(tokenList)
    return left


def parseIdentifier(tokenList):
    actual = takeToken(tokenList)
    
    if actual != ():
        if actual[1] == TokenType.IDENTIFIER:
            return actual[0]
        
        print("Syntax Error Expected TokenType.IDENTIFIER but got {0} at Line {1}.".format(actual[1], actual[2]))
        sys.exit(1)    
    
    
    print("Syntax Error Expected an identifier but there are no more tokens.")
    sys.exit(1)

def parseStatement(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.RETURN_KW:
        takeToken(tokenList)
        retVal = parseExp(tokenList, 0)
        expect(TokenType.SEMICOLON, tokenList)
        return ReturnStmt(retVal) 
    elif token[1] == TokenType.SEMICOLON:
        takeToken(tokenList)
        return NullStatement()
    else:
        #breakpoint()
        retVal = parseExp(tokenList, 0)
        expect(TokenType.SEMICOLON, tokenList)
        return ExpressionStmt(retVal)

def parseDeclaration(tokenList):
    #we are not parsing the type
    takeToken(tokenList)
    id = parseIdentifier(tokenList)
    token = peek(tokenList)
    if token[1] == TokenType.EQUAL:
        takeToken(tokenList)
        exp = parseExp(tokenList, 0)
        expect(TokenType.SEMICOLON, tokenList)
        return Declaration(id, exp)
    
    expect(TokenType.SEMICOLON, tokenList)
    return Declaration(id) 

def parseBlockItem(tokenList):
    token = peek(tokenList)
    if token[1] == TokenType.INT_KW:
        declaration = parseDeclaration(tokenList)
        return D(declaration)
    else:
        statement = parseStatement(tokenList)
        return S(statement)

def parseFunction(tokenList):
    expect(TokenType.INT_KW, tokenList)
    
    iden = parseIdentifier(tokenList)
    expect(TokenType.OPEN_PAREN, tokenList)
    expect(TokenType.VOID_KW, tokenList)
    expect(TokenType.CLOSE_PAREN, tokenList)
    expect(TokenType.OPEN_BRACE, tokenList)
    

    #statement = parseStatement(tokenList)
    #expect(TokenType.CLOSE_BRACE, tokenList)

    BlockItems = []

    #TODO: ADD elements
    while peek(tokenList)[1] != TokenType.CLOSE_BRACE:
        BlockItem = parseBlockItem(tokenList)
        BlockItems.append(BlockItem)
        
    takeToken(tokenList)

    return Function(iden, BlockItems)

def parseProgram(tokenList):
    fun = parseFunction(tokenList)
    return Program(fun)
    

def printAST(pro):
    output = 'Program AST:\n\tfunction: {0}\n'.format(pro.function.iden)

    Level = 2
    match pro.function.statement:
        case ReturnStmt(expression=exp):
            match exp:
                case Unary_Expression():
                    i = 0
                    while i < Level:
                        output += '\t'
                        i += 1

                    output += 'Unary_Expression'
                    pass
                case Binary_Expression(operator=op, left=left, right=right):
                    i = 0
                    while i < Level:
                        output += '\t'
                        i += 1
                    
                    output += 'Binary_Expression'

                    match op:
                        case BinopType.SUBTRACT:
                            pass

                

    print(output)
    