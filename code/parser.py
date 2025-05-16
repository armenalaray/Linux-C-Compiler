import sys
import numpy

import re

from lexer import TokenType
from enum import Enum

class Program:

    def __init__(self, declList=None):
        self.declList = declList
    
    def __str__(self):
        return "AST Program: {self.declList}".format(self=self)

class Block():
    def __init__(self, blockItemList=None):
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
    
    def __repr__(self):
        return self.__str__()
    
class FunDecl(Decl):
    def __init__(self, funDecl):
        self.funDecl = funDecl
    
    def __str__(self):
        return "{self.funDecl}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class VariableDecl:
    def __init__(self, identifier, varType, exp=None, storageClass=None):
        self.identifier = identifier
        self.varType = varType 
        self.exp = exp
        self.storageClass = storageClass    

    def __str__(self):
        return "{self.storageClass} {self.varType} {self.identifier} = {self.exp}".format(self=self)

class FunctionDecl:    
    def __init__(self, iden, funType, paramNames, block=None, storageClass=None):
        self.iden = iden
        self.funType = funType
        self.paramNames = paramNames
        self.block = block
        self.storageClass = storageClass
    
    def __str__(self):

        return "Function: {self.storageClass} {self.funType} {self.iden} ({self.paramNames}) Block: {self.block}".format(self=self)

    def __repr__(self):
        return self.__str__()

class Type:
    def __repr__(self):
        return self.__str__()

class IntType(Type):
    def __str__(self):
        return "int"

class LongType(Type):
    def __str__(self):
        return "long"

class FunType(Type):
    def __init__(self, paramTypes, retType):
        self.paramTypes = paramTypes
        self.retType = retType
    
    def __str__(self):
        return "FunType: ParamTypes: {self.paramTypes} Return Type: {self.retType}".format(self=self)


class StorageType(Enum):
    NULL = 1
    STATIC = 2
    EXTERN = 3

class StorageClass:
    def __init__(self, storageClass):
        self.storageClass = storageClass

    def __str__(self):
        return "{self.storageClass}".format(self=self)

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
    retType = None
    def __repr__(self):
        return self.__str__()
    

class Null_Expression(Expression):
    pass

class Constant_Expression(Expression):
    def __init__(self, const, retType = None):
        self.const = const
        self.retType = retType
    
    def __str__(self):
        #super().__str__()
        return "({self.const} RetType: {self.retType})".format(self=self)

class Cast_Expression(Expression):
    def __init__(self, targetType, exp, retType = None):
        self.targetType = targetType
        self.exp = exp
        self.retType = retType


    def __str__(self):
        return "(({self.targetType}) {self.exp} RetType: {self.retType})".format(self=self)

class Unary_Expression(Expression):
    def __init__(self, operator, expression, retType = None):
        self.operator = operator
        self.expression = expression
        self.retType = retType

    def __str__(self):
        #super().__str__()
        return "(Unary Expression: Operator: {self.operator}Expression: {self.expression} RetType: {self.retType})".format(self=self)

class Binary_Expression(Expression):
    def __init__(self, operator, left, right, retType = None):
        self.operator = operator
        self.left = left
        self.right = right
        self.retType = retType

    def __str__(self):
        #super().__str__()
        return "(Binary Expression: Operator: {self.operator} Left: {self.left} Right: {self.right} RetType: {self.retType})".format(self=self)
    

class Conditional_Expression(Expression):
    def __init__(self, condExp, thenExp, elseExp, retType = None):
        self.condExp = condExp
        self.thenExp = thenExp
        self.elseExp = elseExp
        self.retType = retType
    
    def __str__(self):
        return "({self.condExp} ? {self.thenExp} : {self.elseExp} RetType: {self.retType})".format(self=self)
        pass

class Var_Expression(Expression):
    def __init__(self, identifier, retType = None):
        self.identifier = identifier
        self.retType = retType

    def __str__(self):
        return "({self.identifier} RetType: {self.retType})".format(self=self)

class Assignment_Expression(Expression):
    def __init__(self, lvalue, exp, retType = None):
        self.lvalue = lvalue
        self.exp = exp
        self.retType = retType

    def __str__(self):
        return "({self.lvalue} = {self.exp} RetType: {self.retType})".format(self=self)

class FunctionCall_Exp(Expression):
    def __init__(self, identifer, argumentList=None, retType = None):
        self.identifier = identifer
        self.argumentList = argumentList
        self.retType = retType
    
    def __str__(self):
        return "({self.identifier}({self.argumentList}) RetType: {self.retType})".format(self=self)

class Const:
    pass

class ConstInt(Const):
    def __init__(self, int):
        self.int = int

    def __str__(self):
        return "{self.int}".format(self=self)
    

class ConstLong(Const):
    def __init__(self, int):
        self.int = int
    
    def __str__(self):
        return "{self.int}L".format(self=self)

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


def parseConstant(tokenList):
    token = takeToken(tokenList)

    digitString = ""
    match token[1]:
        case TokenType.INT_CONSTANT:
            digitString = token[0]
        
        case TokenType.LONG_CONSTANT:
            #Se quita el Ll
            regex = "[0-9]+"
            result = re.match(regex, token[0])
            if result:
                digitString = result.group()

        case _:
            print("Invalid Constant type. {0}".format(token[1]))
            sys.exit(1)
        
    v = int(digitString)
    #print(v)

    if v > pow(2, 63) - 1:
        print("Constant is too large to represent as an int or long")
        sys.exit(1)
        pass

    if token[1] == TokenType.INT_CONSTANT and v <= pow(2, 31) - 1:
        return ConstInt(v)

    return ConstLong(v)
    

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

    exp = parseExp(tokenList, 0)

    expList.append(exp)

    token = peek(tokenList)

    while token[1] == TokenType.COMMA:
        takeToken(tokenList)
        exp = parseExp(tokenList, 0)
        expList.append(exp)
        token = peek(tokenList)
        

    return expList

def isConstant(token):
    if token[1] == TokenType.INT_CONSTANT or token[1] == TokenType.LONG_CONSTANT: 
        return True
    return False
    

def parseFactor(tokenList):

    token = peek(tokenList, 1)

    #print(token)

    if isTypeSpecifier(token):

        expect(TokenType.OPEN_PAREN, tokenList)

        token = peek(tokenList)

        types = []
        while isTypeSpecifier(token):
            types.append(takeToken(tokenList))
            token = peek(tokenList)

        type = parseTypes(types)

        expect(TokenType.CLOSE_PAREN, tokenList)

        exp = parseFactor(tokenList)

        return Cast_Expression(type, exp)
        

    if token[1] == TokenType.OPEN_PAREN:
        iden = parseIdentifier(tokenList)
        expect(TokenType.OPEN_PAREN, tokenList)

        token = peek(tokenList)
        if token[1] == TokenType.CLOSE_PAREN:
            expect(TokenType.CLOSE_PAREN, tokenList)
            return FunctionCall_Exp(iden)
            
        expList = parseArgumentList(tokenList)

        expect(TokenType.CLOSE_PAREN, tokenList)
        return FunctionCall_Exp(iden, expList)



    token = peek(tokenList)

    if isConstant(token):
        const = parseConstant(tokenList)
        #print(const)
        return Constant_Expression(const)
    
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

#ERROR: Esta mal por que tiene int kw cuando puede no ser asi tienes que 
#parsear con parsetypeandstorageclass

def parseForInit(tokenList):
    
    #v = parseVarDecl(tokenList, typeAndStorage)
    
    isValid, Decl = parseDeclaration(tokenList)

    if isValid:
        #print(type(Decl))
        if type(Decl) == FunDecl:
            print("Invalid function declaration in for Initializer.")
            sys.exit(1)

        return InitDecl(Decl.variableDecl)
    
    token = peek(tokenList)
    
    if token[1] == TokenType.SEMICOLON:
        takeToken(tokenList)
        return InitExp()
    else:
        exp = parseExp(tokenList, 0)
        expect(TokenType.SEMICOLON, tokenList)
        return InitExp(exp)

        

def parseStatement(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.FOR_KW:
        
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

        expCond = parseExp(tokenList, 0)

        expect(TokenType.CLOSE_PAREN, tokenList)

        thenS = parseStatement(tokenList)

        token = peek(tokenList)
        
        if token[1] == TokenType.ELSE_KW:
            takeToken(tokenList)
            elseS = parseStatement(tokenList)
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

def parseTypes(types):
    #print(types)

    if len(types) == 1 and types[0][1] == TokenType.INT_KW:
        return IntType()
    
    if len(types) == 2 and types[0][1] == TokenType.INT_KW and types[1][1] == TokenType.LONG_KW:
        return LongType()
    
    if len(types) == 2 and types[0][1] == TokenType.LONG_KW and types[1][1] == TokenType.INT_KW:
        return LongType()
    
    if len(types) == 1 and types[0][1] == TokenType.LONG_KW:
        return LongType()
    
    print("Invalid Type Specifier.")
    sys.exit(1)
    

def parseTypeAndStorageClass(specifierList):
    types = []
    storageClasses = []
    for specifier in specifierList:
        if specifier[1] ==  TokenType.INT_KW or specifier[1] == TokenType.LONG_KW:
            types.append(specifier)
        else:
            storageClasses.append(specifier)
            
    type = parseTypes(types)

    if len(storageClasses) > 1:
        print("Invalid Storage Class.")
        sys.exit(1)

    storageClass = StorageClass(StorageType.NULL)

    if len(storageClasses) == 1:
        s = storageClasses[0]
        if s[1] == TokenType.EXTERN_KW:
            storageClass = StorageClass(StorageType.EXTERN)
            
        elif s[1] == TokenType.STATIC_KW:
            storageClass = StorageClass(StorageType.STATIC)

        else:
            print("Error: Invalid Storage Class: {0}".format(s[0]))
            
    return type, storageClass
    
def isSpecifier(token):
    if token[1] == TokenType.EXTERN_KW or token[1] == TokenType.STATIC_KW or isTypeSpecifier(token): 
        return True
    return False

def parseDeclaration(tokenList):
    #we are not parsing the type

    token = peek(tokenList)
    if isSpecifier(token) == False:
        return False, None
    
    specifierList = []
    while isSpecifier(token):
        specifierList.append(takeToken(tokenList))
        token = peek(tokenList)
        
    #print(specifierList)
    type, storageClass = parseTypeAndStorageClass(specifierList)

    token = peek(tokenList, 1)

    if token[1] == TokenType.OPEN_PAREN:
        f = parseFunctionDecl(tokenList, type, storageClass)
        return True, FunDecl(f)
    else:
        v = parseVarDecl(tokenList, type, storageClass)
        return True, VarDecl(v)
    

#ERROR: Esta mal por que tiene int kw cuando puede no ser asi tienes que 
#parsear con parsetypeandstorageclass

def parseBlockItem(tokenList):
    
    isValid, decl = parseDeclaration(tokenList)
    
    if isValid:
        if type(decl) == FunDecl:
            #print(type(decl.funDecl.block))
            if decl.funDecl.block:
                print("Invalid Nested function definition in block.")
                sys.exit(1)

        return D(decl)

    statement = parseStatement(tokenList)
    return S(statement)

def parseBlock(tokenList):
    

    expect(TokenType.OPEN_BRACE, tokenList)
    
    token = peek(tokenList)

    if token[1] == TokenType.CLOSE_BRACE:
        takeToken(tokenList)
        return Block()

    BlockItemList = []
    
    while peek(tokenList)[1] != TokenType.CLOSE_BRACE:
        BlockItem = parseBlockItem(tokenList)
        BlockItemList.append(BlockItem)
        
    takeToken(tokenList)

    return Block(BlockItemList)

def isTypeSpecifier(token):
    if token[1] == TokenType.INT_KW or token[1] == TokenType.LONG_KW: 
        return True
    return False

def parseParamList(tokenList):
    paramNames = []
    paramTypes = []

    token = peek(tokenList)

    if token[1] == TokenType.VOID_KW:
        takeToken(tokenList)
        return paramTypes, paramNames
    
    #parseTypeSpecifier(tokenList, paramTypes)
    
    types = []
    while isTypeSpecifier(token):
        types.append(takeToken(tokenList))
        token = peek(tokenList)

    type = parseTypes(types)
    paramTypes.append(type)

    iden = parseIdentifier(tokenList)
    paramNames.append(iden)

    token = peek(tokenList)


    while token[1] == TokenType.COMMA:
        takeToken(tokenList)
        
        types = []
        token = peek(tokenList)

        while isTypeSpecifier(token):
            types.append(takeToken(tokenList))
            token = peek(tokenList)

        type = parseTypes(types)
        paramTypes.append(type)
        

        iden = parseIdentifier(tokenList)
        paramNames.append(iden)

        token = peek(tokenList)

    #print(paramTypes)

    return paramTypes, paramNames
    
def parseVarDecl(tokenList, type, storageClass):

    #expect(TokenType.INT_KW, tokenList)

    id = parseIdentifier(tokenList)
    
    token = peek(tokenList)

    exp = None
    if token[1] == TokenType.EQUAL:
        takeToken(tokenList)
        exp = parseExp(tokenList, 0)

    expect(TokenType.SEMICOLON, tokenList)
    return VariableDecl(id, type, exp, storageClass) 


def parseFunctionDecl(tokenList, retType, storageClass):
    
    #expect(TokenType.INT_KW, tokenList)
    
    iden = parseIdentifier(tokenList)

    expect(TokenType.OPEN_PAREN, tokenList)

    paramTypes, paramNames = parseParamList(tokenList)

    #print(paramTypes)
    
    expect(TokenType.CLOSE_PAREN, tokenList)

    token = peek(tokenList)

    block = None

    if token[1] == TokenType.SEMICOLON:
        takeToken(tokenList)
    else:
        block = parseBlock(tokenList)

    funType = FunType(paramTypes, retType)
    return FunctionDecl(iden, funType, paramNames, block, storageClass)

def parseProgram(tokenList):
    
    if tokenList == []:
        return Program()
    
    funDeclList = []
    while tokenList != []:
        isValid, decl = parseDeclaration(tokenList)

        if isValid == False:
            print("Invalid Declaration.")
            sys.exit(1)

        funDeclList.append(decl)

    return Program(funDeclList)
    