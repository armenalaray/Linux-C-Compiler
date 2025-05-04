import sys
from ctoken import TokenType
from enum import Enum

class Program:

    def __init__(self, funcDeclList):
        self.funcDeclList = funcDeclList
    
    def __str__(self):
        return "AST Program: {self.funcDeclList}".format(self=self)

class Block():
    def __init__(self, blockItemList):
        self.blockItemList = blockItemList
    
    def __str__(self):
        return "{self.blockItemList}".format(self=self)

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

class Decl:
    pass

class VarDecl(Decl):
    def __init__(self, variableDecl):
        self.variableDecl = variableDecl
    
    def __str__(self):
        return "{self.variableDecl}".format(self=self)
    
class FunDecl(Decl):
    def __init__(self, funDecl):
        self.funDecl = funDecl
    
    def __str__(self):
        return "{self.funDecl}".format(self=self)

class VariableDecl:
    def __init__(self, identifier, exp=None):
        self.identifier = identifier
        self.exp = exp
    
    def __str__(self):
        return "{self.identifier} = {self.exp}".format(self=self)

class FunctionDecl:    
    def __init__(self, iden, paramList, block=None):
        self.iden = iden
        self.paramList = paramList
        self.block = block
    
    def __str__(self):

        return "Function: {self.iden} ({self.paramList}) Block: {self.block}".format(self=self)

    def __repr__(self):
        return self.__str__()

class ForInit:
    pass

class InitDecl(ForInit):
    def __init__(self, varDecl):
        self.varDecl = varDecl
        
    def __str__(self):
        return "Declaration: {self.varDecl}".format(self=self)


class InitExp(ForInit):
    def __init__(self, exp=None):
        self.exp = exp
    
    def __str__(self):
        return "InitExp: {self.exp}".format(self=self)

class Statement:
    pass

class IfStatement(Statement):
    def __init__(self, expCond, thenS, elseS=None):
        self.exp = expCond
        self.thenS = thenS
        self.elseS = elseS
    
    def __str__(self):
        return "if ({self.exp}) thenS: {self.thenS} elseS: {self.elseS}".format(self=self)


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

class BreakStatement(Statement):
    def __init__(self, identifier=None):
        self.identifier = identifier
    
    def __str__(self):
        return "break loopOwner: {self.identifier}".format(self=self)

class ContinueStatement(Statement):
    def __init__(self, identifier=None):
        self.identifier = identifier
    
    def __str__(self):
        return "continue loopOwner: {self.identifier}".format(self=self)

class WhileStatement(Statement):
    def __init__(self, condExp, statement, identifier=None):
        self.condExp = condExp
        self.statement = statement
        self.identifier = identifier
    
    def __str__(self):
        return "while {self.identifier} ({self.condExp}) thenS: {self.statement}".format(self=self)

class DoWhileStatement(Statement):
    def __init__(self, statement, condExp, identifier=None):
        self.statement = statement
        self.condExp = condExp
        self.identifier = identifier
    
    def __str__(self):
        return "do {self.identifier} thenS: {self.statement} while ({self.condExp})".format(self=self)

class ForStatement(Statement):
    def __init__(self, forInit, statement, condExp=None, postExp=None, identifier=None):
        self.forInit = forInit
        self.condExp = condExp
        self.postExp = postExp
        self.statement = statement
        self.identifier = identifier
    
    def __str__(self):
        return "for {self.identifier} ({self.forInit} ; {self.condExp} ; {self.postExp}) thenS: {self.statement}".format(self=self)


class CompoundStatement(Statement):
    def __init__(self, block):
        self.block = block
    
    def __str__(self):
        return "Block: {self.block}".format(self=self)


class NullStatement(Statement):
    def __init__(self):
        pass

class Expression:
    def __repr__(self):
        return self.__str__()
    

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
        return "Unary Expression: Operator: {self.operator}Expression: {self.expression}".format(self=self)

class Binary_Expression(Expression):
    def __init__(self, operator, left, right):
        self.operator = operator
        self.left = left
        self.right = right

    def __str__(self):
        #super().__str__()
        return "Binary Expression: Operator: {self.operator} Left: {self.left} Right: {self.right}".format(self=self)
    

class Conditional_Expression(Expression):
    def __init__(self, condExp, thenExp, elseExp):
        self.condExp = condExp
        self.thenExp = thenExp
        self.elseExp = elseExp
    
    def __str__(self):
        return "{self.condExp} ? {self.thenExp} : {self.elseExp}".format(self=self)
        pass

class Var_Expression(Expression):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "{self.identifier}".format(self=self)

class Assignment_Expression(Expression):
    def __init__(self, lvalue, exp):
        self.lvalue = lvalue
        self.exp = exp

    def __str__(self):
        return "{self.lvalue} = {self.exp}".format(self=self)

class FunctionCall_Exp(Expression):
    def __init__(self, identifer, argumentList):
        self.identifier = identifer
        self.argumentList = argumentList
    
    def __str__(self):
        return "{self.identifier}({self.argumentList})".format(self=self)

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
    
    print("No more tokens.")
    sys.exit(1)

def peek(tokenList, index=None):
    if(tokenList != []):
        if index:
            return tokenList[index]
        else:
            return tokenList[0]
    
    print("No more tokens.")
    sys.exit(1)

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
    
    
def parseArgumentList(tokenList):
    expList = []

    while True:
        token = peek(tokenList)
        match token[1]:
            case TokenType.CLOSE_PAREN:
                break
            case TokenType.COMMA:
                takeToken(tokenList)
                pass
            case _:
                exp = parseExp(tokenList, 0)
                #print(exp)
                expList.append(exp)
                

    #print(expList)

    return expList
    

def parseFactor(tokenList):

    token = peek(tokenList, 1)

    #print(token)

    if token[1] == TokenType.OPEN_PAREN:
        iden = parseIdentifier(tokenList)
        expect(TokenType.OPEN_PAREN, tokenList)
        expList = parseArgumentList(tokenList)
        expect(TokenType.CLOSE_PAREN, tokenList)
        return FunctionCall_Exp(iden, expList)
        

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
    TokenType.QUESTION_MARK : 3,
    TokenType.EQUAL : 1
    }

def precedence(token):
    if token != ():
        return precTable[token[1]]
    
    print("Syntax Error Expected a token but there are no more tokens.")
    sys.exit(1)


def BinaryOperatorToken(token):
    if token != ():
        
        if token[1] == TokenType.ASTERISK or token[1] == TokenType.PLUS or token[1] == TokenType.FORWARD_SLASH or token[1] == TokenType.PERCENT or token[1] == TokenType.HYPHEN or token[1] == TokenType.TAMPERSANDS or token[1] == TokenType.TVERTICALB or token[1] == TokenType.TEQUALS or token[1] == TokenType.EXCLAMATIONEQUAL or token[1] == TokenType.LESSTEQUALT or token[1] == TokenType.GREATERTEQUALT or token[1] == TokenType.GREATERT or token[1] == TokenType.LESST or token[1] == TokenType.EQUAL or token[1] == TokenType.QUESTION_MARK:
            return True
        
    return False

def parseConditionalMiddle(tokenList):
    expect(TokenType.QUESTION_MARK, tokenList)
    middle = parseExp(tokenList, 0)
    expect(TokenType.COLON, tokenList)
    return middle

def parseExp(tokenList, min_prec):
    #breakpoint()
    left = parseFactor(tokenList)
    next_token = peek(tokenList)
    while BinaryOperatorToken(next_token) and precedence(next_token) >= min_prec:
        if next_token[1] == TokenType.EQUAL:
            takeToken(tokenList)
            right = parseExp(tokenList, precedence(next_token))
            left = Assignment_Expression(left, right)

        elif next_token[1] == TokenType.QUESTION_MARK:
            middle = parseConditionalMiddle(tokenList)
            right = parseExp(tokenList, precedence(next_token))
            left = Conditional_Expression(left, middle, right)
            
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

def parseForInit(tokenList):
    token = peek(tokenList)
    if token[1] == TokenType.SEMICOLON:
        takeToken(tokenList)
        return InitExp()
    
    if token[1] == TokenType.INT_KW:
        v = parseVarDecl(tokenList)
        return InitDecl(v)
    else:
        exp = parseExp(tokenList, 0)
        expect(TokenType.SEMICOLON, tokenList)
        return InitExp(exp)

    

def parseStatement(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.FOR_KW:
        print(token)
        takeToken(tokenList)
        expect(TokenType.OPEN_PAREN, tokenList)

        forInit = parseForInit(tokenList)
        
        token = peek(tokenList)

        condExp = None

        if token[1] != TokenType.SEMICOLON:
            condExp = parseExp(tokenList, 0)

        expect(TokenType.SEMICOLON, tokenList)

        token = peek(tokenList)

        postExp = None

        if token[1] != TokenType.CLOSE_PAREN:
            postExp = parseExp(tokenList, 0)

        expect(TokenType.CLOSE_PAREN, tokenList)
        
        thenS = parseStatement(tokenList)

        return ForStatement(forInit, thenS, condExp, postExp)
        
    if token[1] == TokenType.DO_KW:
        takeToken(tokenList)
        thenS = parseStatement(tokenList)
        #print(thenS)

        expect(TokenType.WHILE_KW, tokenList)
        expect(TokenType.OPEN_PAREN, tokenList)
        
        expCond = parseExp(tokenList, 0)

        expect(TokenType.CLOSE_PAREN, tokenList)

        expect(TokenType.SEMICOLON, tokenList)
        return DoWhileStatement(thenS, expCond)

    if token[1] == TokenType.WHILE_KW:
        #print(token)
        takeToken(tokenList)
        expect(TokenType.OPEN_PAREN, tokenList)
        #breakpoint()
        expCond = parseExp(tokenList, 0)
        expect(TokenType.CLOSE_PAREN, tokenList)

        thenS = parseStatement(tokenList)

        return WhileStatement(expCond, thenS)
    
    if token[1] == TokenType.BREAK_KW:
        takeToken(tokenList)
        expect(TokenType.SEMICOLON, tokenList)

        return BreakStatement()
    
    if token[1] == TokenType.CONTINUE_KW:
        takeToken(tokenList)
        expect(TokenType.SEMICOLON, tokenList)

        return ContinueStatement()

    if token[1] == TokenType.OPEN_BRACE:
        #breakpoint()
        block = parseBlock(tokenList)
        return CompoundStatement(block)
    
    elif token[1] == TokenType.IF_KW:
        takeToken(tokenList)
        expect(TokenType.OPEN_PAREN, tokenList)

        #var expression 
        expCond = parseExp(tokenList, 0)

        #breakpoint()
        expect(TokenType.CLOSE_PAREN, tokenList)

        thenS = parseStatement(tokenList)

        token = peek(tokenList)
        #print(token)
        if token[1] == TokenType.ELSE_KW:
            takeToken(tokenList)
            elseS = parseStatement(tokenList)
            #breakpoint()
            return IfStatement(expCond, thenS, elseS)    

        return IfStatement(expCond, thenS)
        
    elif token[1] == TokenType.RETURN_KW:
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

def parseVarDecl(tokenList):
    takeToken(tokenList)

    id = parseIdentifier(tokenList)
    
    token = peek(tokenList)
    if token[1] == TokenType.EQUAL:
        takeToken(tokenList)
        exp = parseExp(tokenList, 0)
        expect(TokenType.SEMICOLON, tokenList)
        return VariableDecl(id, exp)

    expect(TokenType.SEMICOLON, tokenList)
    return VariableDecl(id) 


def parseDeclaration(tokenList):
    #we are not parsing the type

    token = peek(tokenList, 2)
    #print(token)
    
    if token[1] == TokenType.OPEN_PAREN:
        f = parseFunctionDecl(tokenList)
        return FunDecl(f)
    else:
        v = parseVarDecl(tokenList)
        return VarDecl(v)

def parseBlockItem(tokenList):
    token = peek(tokenList)
    if token[1] == TokenType.INT_KW:
        declaration = parseDeclaration(tokenList)
        return D(declaration)
    else:
        statement = parseStatement(tokenList)
        return S(statement)

def parseBlock(tokenList):
    
    BlockItemList = []

    expect(TokenType.OPEN_BRACE, tokenList)
    
    while peek(tokenList)[1] != TokenType.CLOSE_BRACE:
        BlockItem = parseBlockItem(tokenList)
        #print(BlockItem)
        BlockItemList.append(BlockItem)
        
    takeToken(tokenList)

    return Block(BlockItemList)

def parseParamList(tokenList):
    paramList = []

    token = peek(tokenList)

    if token[1] == TokenType.VOID_KW:
        takeToken(tokenList)
        return paramList
    
    expect(TokenType.INT_KW, tokenList)

    iden = parseIdentifier(tokenList)
    paramList.append(iden)

    token = peek(tokenList)

    while token[1] == TokenType.COMMA:
        takeToken(tokenList)
        #print(tokenList)
        expect(TokenType.INT_KW, tokenList)

        iden = parseIdentifier(tokenList)
        paramList.append(iden)

        token = peek(tokenList)

    #   print(paramList)

    return paramList
    

def parseFunctionDecl(tokenList):
    
    expect(TokenType.INT_KW, tokenList)
    
    iden = parseIdentifier(tokenList)

    expect(TokenType.OPEN_PAREN, tokenList)

    paramList = parseParamList(tokenList)
    
    expect(TokenType.CLOSE_PAREN, tokenList)

    token = peek(tokenList)

    block = None

    if token[1] == TokenType.SEMICOLON:
        takeToken(tokenList)
    else:
        block = parseBlock(tokenList)

    return FunctionDecl(iden, paramList, block)

def parseProgram(tokenList):
    funDeclList = []
    while tokenList != []:
        funDecl = parseFunctionDecl(tokenList)
        funDeclList.append(funDecl)

    return Program(funDeclList)
    

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
    