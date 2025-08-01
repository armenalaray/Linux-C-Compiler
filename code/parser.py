import sys
import re
import traceback
from lexer import TokenType
from enum import Enum

class Node:
    def printNode(self, level):
        return ""

class Program(Node):

    def __init__(self, declList=None):
        self.declList = declList

    def __str__(self):
        return "AST Program: {self.declList}".format(self=self)
    
    def printNode(self, level):
        #print("AST Program:")
        output = 'AST Program:\n'

        if self.declList:
            for i in self.declList:
                output += i.printNode(level) + "\n"
        
        return output

class Block(Node):
    def __init__(self, blockItemList=None):
        self.blockItemList = blockItemList
    
    def __str__(self):
        return "{self.blockItemList}".format(self=self)
    
    def printNode(self, level):
        print(level)
        output = ''
        if self.blockItemList:
            for i in self.blockItemList:
                l = level
                
                while l > 0:
                    output += '\t'
                    l -= 1

                output += i.printNode(level) + "\n"

        output = output[:-1]
        return output

class BlockItem:
    pass

class S(BlockItem, Node):
    def __init__(self, statement):
        self.statement = statement
    
    def __str__(self):
        return "Statement: {self.statement}".format(self=self)

    def __repr__(self):
        return self.__str__()
    
    def printNode(self, level):
        output = ''
        output += "Statement: " + self.statement.printNode(level)
        return output
        
        
class D(BlockItem, Node):
    def __init__(self, declaration):
        self.declaration = declaration
    
    def __str__(self):
        return "Declaration: {self.declaration}".format(self=self)

    def __repr__(self):
        return self.__str__()
    
    def printNode(self, level):
        output = ''
        output += "Declaration:\n" + self.declaration.printNode(level)
        return output

class Decl:
    pass

class StructDecl(Decl, Node):
    def __init__(self, structDecl):
        self.structDecl = structDecl

    def printNode(self, level):
        l = level
        output = ''
        while l > 0:
            output += '\t'
            l -= 1

        output += "StructDecl:\n" + self.structDecl.printNode(level)

        return output 

class VarDecl(Decl, Node):
    def __init__(self, variableDecl):
        self.variableDecl = variableDecl
    
    def __str__(self):
        return "{self.variableDecl}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
    def printNode(self, level):
        l = level
        output = ''
        while l > 0:
            output += '\t'
            l -= 1

        output += "VarDecl: " + self.variableDecl.printNode(level)

        return output

    
class FunDecl(Decl, Node):
    def __init__(self, funDecl):
        self.funDecl = funDecl
    
    def __str__(self):
        return "{self.funDecl}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
    def printNode(self, level):
        l = level
        output = ''
        while l > 0:
            output += '\t'
            l -= 1

        output += "FunDecl: " + self.funDecl.printNode(level)

        return output

class VariableDecl(Node):
    def __init__(self, identifier, varType, initializer=None, storageClass=None):
        self.identifier = identifier
        self.varType = varType 
        self.initializer = initializer
        self.storageClass = storageClass    

    def __str__(self):
        return "{self.storageClass} {self.varType} {self.identifier} = {self.exp}".format(self=self)
    
    def printNode(self, level):
        output = ''
        if self.storageClass:
            output += self.storageClass.printNode(level) + " "
            
        output += self.varType.printNode(level) + " "
        
        output += self.identifier

        if self.initializer:
            output +=  " = " + self.initializer.printNode(level)

        #output = "{self.storageClass} {self.varType} {self.identifier} = {self.exp}".format(self=self)

        return output


class StructDeclaration(Node):
    def __init__(self, tag, members):
        self.tag = tag 
        self.members = members

    def printNode(self, level):
        l = level
        output = ''
        while l > 0:
            output += '\t'
            l -= 1

        output += "struct " + self.tag + "\n"
        for i in self.members:
            output += i.printNode(level + 1) + "\n"

        return output

class MemberDecl(Node):
    def __init__(self, name, type):
        self.name = name
        self.memberType = type

    def printNode(self, level):
        l = level
        output = ''
        while l > 0:
            output += '\t'
            l -= 1

        output += self.memberType.printNode(level)
        output += " " + self.name

        return output


class FunctionDecl(Node):    
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
    
    def printNode(self, level):
        output = ''

        if self.storageClass:
            output += self.storageClass.printNode(level)    

        output += " " + self.iden

        output += ' ('
        for i in self.paramNames:
            output += i + ', '
        output += ') '

        output += self.funType.printNode(level)

        output += '\n'

        if self.block:
            output += self.block.printNode(level)

        return output

class Initializer(Node):
    pass

class SingleInit(Initializer, Node):
    def __init__(self, exp, retType=None):
        self.exp = exp
        self.retType = retType
    
    def __str__(self):
        return "SingleInit: {self.exp}".format(self=self)
    
    def printNode(self, level):
        output = ''
        output += "SI: " + self.exp.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        return output

def tabLevel(output, level):
    l = level
    while l > 0:
        output += '\t'
        l -= 1
    
    return output

class CompoundInit(Initializer, Node):
    def __init__(self, initializerList, retType=None):
        self.initializerList = initializerList 
        self.retType = retType

    def __str__(self):
        return ": {self.initializerList}".format(self=self)
    
    def printNode(self, level):
        output = '\n'
        
        output = tabLevel(output, level)

        output += "CI:["

        #output = tabLevel(output, level + 1)
        
        for i in self.initializerList:
            output += i.printNode(level + 1) + ", "
        
        output += "]"

        if self.retType:
            output += '\n'
            output = tabLevel(output, level)
            output +=  ': ' + self.retType.printNode(level)
        
        return output

class Type:
    def __init__(self):
        self.size = 0

    def checkType(self, other):
        traceback.print_stack()
        print("Not Overloaded.")
        sys.exit(1)

    def getBaseTypeSize(self, occupied, typeTable):
        pass

    def getSize():
        return self.size

    def __repr__(self):
        return self.__str__()

class VoidType(Type, Node):
    def __str__(self):
        return "void"
    
    def printNode(self, level):
        return "void"
    
    def getBaseTypeSize(self, occupied, typeTable):
        print("Error: Cannot get Size of void Type.")
        sys.exit(1)

    def getSize():
        print("Error: Cannot get Size of void Type.")
        sys.exit(1)

    def checkType(self, other):
        if type(other) == VoidType:
            return True

        return False
    
class CharType(Type, Node):
    
    def __init__(self):
        super().__init__()
        self.size = 1
        self.isSigned = True

    def getBaseTypeSize(self, occupied, typeTable):
        return self.size

    def __str__(self):
        return "char"
    
    def printNode(self, level):
        return "char"
    
    def checkType(self, other):
        if type(other) == CharType:
            return True

        return False
    

class SCharType(Type, Node):
    def __init__(self):
        super().__init__()
        self.size = 1
        self.isSigned = True

    def getBaseTypeSize(self, occupied, typeTable):
        return self.size

    def __str__(self):
        return "signed char"
    
    def printNode(self, level):
        return "signed char"
    
    def checkType(self, other):
        if type(other) == SCharType:
            return True

        return False
    

class UCharType(Type, Node):
    def __init__(self):
        super().__init__()
        self.size = 1
        self.isSigned = False

    def getBaseTypeSize(self, occupied, typeTable):
        return self.size

    def __str__(self):
        return "unsigned char"
    
    def printNode(self, level):
        return "unsigned char"
    
    def checkType(self, other):
        if type(other) == UCharType:
            return True

        return False
    

class IntType(Type, Node):
    def __init__(self):
        super().__init__()
        self.size = 4
        self.isSigned = True

    def getBaseTypeSize(self, occupied, typeTable):
        return self.size

    def __str__(self):
        return "int"
    
    def printNode(self, level):
        return "int"
    
    def checkType(self, other):
        if type(other) == IntType:
            return True

        return False
    

class LongType(Type, Node):
    def __init__(self):
        super().__init__()
        self.size = 8
        self.isSigned = True

    def getBaseTypeSize(self, occupied, typeTable):
        return self.size
    
    def __str__(self):
        return "long"
    
    def printNode(self, level):
        return "long"
    
    def checkType(self, other):
        if type(other) == LongType:
            return True

        return False
    
class UIntType(Type, Node):    
    def __init__(self):
        super().__init__()
        self.size = 4
        self.isSigned = False

    def getBaseTypeSize(self, occupied, typeTable):
        return self.size
    
    def __str__(self):
        return "uint"
    
    def printNode(self, level):
        return "uint"
    
    def checkType(self, other):
        if type(other) == UIntType:
            return True

        return False

class ULongType(Type, Node):
    def __init__(self):
        super().__init__()
        self.size = 8
        self.isSigned = False

    def getBaseTypeSize(self, occupied, typeTable):
        return self.size
    
    def __str__(self):
        return "ulong"
    
    def printNode(self, level):
        return "ulong"
    
    def checkType(self, other):
        if type(other) == ULongType:
            return True

        return False

class DoubleType(Type, Node):
    def __str__(self):
        return "double"
    
    def getBaseTypeSize(self, occupied, typeTable):
        return 8
    
    def printNode(self, level):
        return "double"
    
    def checkType(self, other):
        if type(other) == DoubleType:
            return True

        return False
        

class PointerType(Type, Node):
    def __init__(self, referenceType):
        self.referenceType = referenceType

    def getBaseTypeSize(self, occupied, typeTable):
        return 8
    
    def __str__(self):
        return "P{self.referenceType}".format(self=self)
    
    def checkType(self, other):
        
        if type(other) == PointerType:
            if self.referenceType.checkType(other.referenceType):
                return True
                
        return False

    def printNode(self, level):
        output = "P"
        output += self.referenceType.printNode(level)
        return output

class ArrayType(Type, Node):
    def __init__(self, elementType, size):
        self.elementType = elementType
        self.size = size
    
    def getBaseTypeSize(self, occupied, typeTable):
        return self.elementType.getBaseTypeSize(0, typeTable) * self.size - occupied * self.elementType.getBaseTypeSize(0, typeTable)
    
    def checkType(self, other):
        
        if type(other) == ArrayType:
            if self.elementType.checkType(other.elementType) and self.size == other.size:
                return True
        
        return False
            
    def __str__(self):
        return "ArrayType: {self.elementType} Size: {self.size}".format(self=self)
    
    def printNode(self, level):
        output = "ArrayType( "
        #print(self.size)
        output += self.elementType.printNode(level) + ", size: " + str(self.size)
        output += ")"
        return output
    
class StuctureType(Type, Node):

    def __init__(self, tag):
        self.tag = tag

    def getBaseTypeSize(self, occupied, typeTable):
        if not self.tag in typeTable:
            print("Error: Structure Type not found in type table: ", self.tag)
            sys.exit(1)

        structDef = typeTable[self.tag]
        return structDef.size

    def checkType(self, other):
        if type(other) == StuctureType and self.tag == other.tag:
            return True
        
        return False

    def __str__(self):
        return "StructType({self.tag})".format(self=self)
    
    def printNode(self, level):
        output = "StructType(" + self.tag + ")"
        return output
    
class FunType(Type, Node):
    def __init__(self, paramTypes, retType):
        self.paramTypes = paramTypes
        self.retType = retType

        #self.paramNames = paramNames
    
    def __str__(self):
        return "FunType: ParamTypes: {self.paramTypes} Return Type: {self.retType}".format(self=self)
    
    def printNode(self, level):
        output = ""

        output += "ParamTypes: ("
        for i in self.paramTypes:
            output += i.printNode(level) + ", "
            pass

        output += ") ReturnType: "

        output += self.retType.printNode(level)
        return output
        return super().printNode(level)


class StorageType(Enum):
    NULL = 1
    STATIC = 2
    EXTERN = 3

class StorageClass(Node):
    def __init__(self, storageClass):
        self.storageClass = storageClass

    def __str__(self):
        return "{self.storageClass}".format(self=self)
    
    def printNode(self, level):
        output = self.storageClass.name
        return output
        

class ForInit:
    pass

class InitDecl(ForInit, Node):
    def __init__(self, varDecl):
        self.varDecl = varDecl
        
    def __str__(self):
        return "Declaration: {self.varDecl}".format(self=self)

    def printNode(self, level):
        output = ""
        output += self.varDecl.printNode(level)
        return output
    
        return super().printNode(level)

class InitExp(ForInit, Node):
    def __init__(self, exp=None):
        self.exp = exp
    
    def __str__(self):
        return "InitExp: {self.exp}".format(self=self)
    
    def printNode(self, level):
        output = ""
        if self.exp:
            output += self.exp.printNode(level)

        return output
        
        return super().printNode(level)

class Statement:
    pass

class IfStatement(Statement, Node):
    def __init__(self, expCond, thenS, elseS=None):
        self.exp = expCond
        self.thenS = thenS
        self.elseS = elseS
    
    def __str__(self):
        return "if ({self.exp}) thenS: {self.thenS} elseS: {self.elseS}".format(self=self)

    def printNode(self, level):
        output = ""
        output += "if (" + self.exp.printNode(level) + ")"
        output += self.thenS.printNode(level)

        if self.elseS:
            output += self.elseS.printNode(level)

        return output
    
        #return super().printNode(level)


class ReturnStmt(Statement, Node):
    def __init__(self, exp = None):
        self.expression = exp

    def __str__(self):
        #super().__str__()
        return "return {self.expression}".format(self=self)
    
    def printNode(self, level):
        output = ""
        output += "return" 
        
        if self.expression:
            output += " " + self.expression.printNode(level)

        return output
    

class ExpressionStmt(Statement, Node):
    def __init__(self, exp):
        self.exp = exp
    
    def __str__(self):
        return "{self.exp}".format(self=self)
    
    def printNode(self, level):
        output = ""
        output += "Expression: " + self.exp.printNode(level)
        return output
    

class BreakStatement(Statement, Node):
    def __init__(self, identifier=None):
        self.identifier = identifier
    
    def __str__(self):
        return "break loopOwner: {self.identifier}".format(self=self)
    
    def printNode(self, level):
        output = "break "
        if self.identifier:
            output += "Loop Owner: " + self.identifier
        return output
    
    

class ContinueStatement(Statement, Node):
    def __init__(self, identifier=None):
        self.identifier = identifier
    
    def __str__(self):
        return "continue loopOwner: {self.identifier}".format(self=self)
    
    def printNode(self, level):
        output = "continue "
        if self.identifier:
            output += "Loop Owner: " + self.identifier
        return output

class WhileStatement(Statement, Node):
    def __init__(self, condExp, statement, identifier=None):
        self.condExp = condExp
        self.statement = statement
        self.identifier = identifier
    
    def __str__(self):
        return "while {self.identifier} ({self.condExp}) thenS: {self.statement}".format(self=self)
    
    def printNode(self, level):
        output = ""
        output += "while "

        if self.identifier:
            output += self.identifier

        output += " (" + self.condExp.printNode(level) + ")"
        output += self.statement.printNode(level)

        return output
    

class DoWhileStatement(Statement, Node):
    def __init__(self, statement, condExp, identifier=None):
        self.statement = statement
        self.condExp = condExp
        self.identifier = identifier
    
    def __str__(self):
        return "do {self.identifier} thenS: {self.statement} while ({self.condExp})".format(self=self)
    
    def printNode(self, level):
        output = "do while "

        if self.identifier:
            output += self.identifier

        output += " (" + self.condExp.printNode(level) + ")"
        output += self.statement.printNode(level)

        return output
        return super().printNode(level)

class ForStatement(Statement, Node):
    def __init__(self, forInit, statement, condExp=None, postExp=None, identifier=None):
        self.forInit = forInit
        self.condExp = condExp
        self.postExp = postExp
        self.statement = statement
        self.identifier = identifier
    
    def __str__(self):
        return "for {self.identifier} ({self.forInit} ; {self.condExp} ; {self.postExp}) thenS: {self.statement}".format(self=self)

    def printNode(self, level):
        output = ""
        output += "for "

        if self.identifier:
            output += self.identifier
        
        output += " (" + self.forInit.printNode(level) + ", "
        
        if self.condExp:
            output += self.condExp.printNode(level)
            
        output += ", " 
        
        if self.postExp:
            output += self.postExp.printNode(level) 
        
        output += ")"

        output += self.statement.printNode(level)

        return output
        

class CompoundStatement(Statement, Node):
    def __init__(self, block):
        self.block = block
    
    def __str__(self):
        return "Block: {self.block}".format(self=self)
    
    def printNode(self, level):
        output = ""
        output += "\n" + self.block.printNode(level + 1)
        return output


class NullStatement(Statement, Node):
    def __init__(self):
        pass

    def printNode(self, level):
        return "NullStatement;"

class Expression:
    retType = None
    def __repr__(self):
        return self.__str__()

class Dot(Expression, Node):

    def __init__(self, struct, member, retType = None):
        self.struct = struct
        self.member = member
        self.retType = retType

    def __str__(self):
        return "({self.struct}.{self.member} RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = "("
        output += self.struct.printNode(level) + " . " + self.member

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output

class Arrow(Expression, Node):
    def __init__(self, pointer, member, retType = None):
        self.pointer = pointer
        self.member = member
        self.retType = retType

    def __str__(self):
        return "({self.pointer}->{self.member} RetType: {self.retType})".format(self=self)

    def printNode(self, level):
        output = "("
        output += self.pointer.printNode(level) + " -> " + self.member

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output
 
class SizeOf(Expression, Node):
    def __init__(self, exp, retType = None):
        self.exp = exp
        self.retType = retType
    
    def __str__(self):
        return "sizeof {self.exp} RetType: {self.retType}".format(self=self)

    def printNode(self, level):
        output = "("
        output += "sizeof " + self.exp.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output    

class SizeOfT(Expression, Node):
    def __init__(self, typeName, retType = None):
        self.typeName = typeName
        self.retType = retType

    def __str__(self):
        return "sizeofType({self.typeName}) RetType: {self.retType}".format(self=self)
    
    def printNode(self, level):
        output = "("
        output += "sizeofType(" + self.typeName.printNode(level) + ")"

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output    

class StringExpression(Expression, Node):
    def __init__(self, string, retType = None):
        self.string = string
        self.retType = retType

    def __str__(self):
        return "{self.string} RetType: {self.retType}".format(self=self)
    
    def printNode(self, level):
        output = "("
        output += self.string

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output    

class Dereference(Expression, Node):
    def __init__(self, exp, retType = None):
        self.exp = exp
        self.retType = retType

    def __str__(self):
        return "*{self.exp} RetType: {self.retType}".format(self=self)
    
    def printNode(self, level):
        output = "(*"
        output += self.exp.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output

#&
class AddrOf(Expression, Node):
    def __init__(self, exp, retType = None):
        self.exp = exp
        self.retType = retType
    
    def __str__(self):
        return "&{self.exp} RetType: {self.retType}".format(self=self)
    
    def printNode(self, level):
        output = "(&"
        output += self.exp.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output

class Subscript(Expression, Node):
    def __init__(self, ptrExp, indexExp, retType = None):
        self.ptrExp = ptrExp
        self.indexExp = indexExp
        self.retType = retType
    
    def __str__(self):
        return "Ale"
    
    def printNode(self, level):
        output = "("
        
        output += self.ptrExp.printNode(level) + "[" + self.indexExp.printNode(level) + "]"

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"

        return output


class Null_Expression(Expression):
    pass

class Constant_Expression(Expression, Node):
    def __init__(self, const, retType = None):
        self.const = const
        self.retType = retType
    
    def __str__(self):
        #super().__str__()
        return "({self.const} RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = '('
        output += self.const.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"

        return output
    

class Cast_Expression(Expression, Node):
    def __init__(self, targetType, exp, retType = None):
        self.targetType = targetType
        self.exp = exp
        self.retType = retType


    def __str__(self):
        return "(({self.targetType}) {self.exp} RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = "("
        output += "(" + self.targetType.printNode(level) + ") "

        output += self.exp.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output
        #return super().printNode(level)

class Unary_Expression(Expression, Node):
    def __init__(self, operator, expression, retType = None):
        self.operator = operator
        self.expression = expression
        self.retType = retType

    def __str__(self):
        #super().__str__()
        return "(Unary Expression: Operator: {self.operator}Expression: {self.expression} RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = "("
        output += self.operator.printNode(level) + " "
        output += self.expression.printNode(level)
        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output

class Binary_Expression(Expression, Node):
    def __init__(self, operator, left, right, retType = None):
        self.operator = operator
        self.left = left
        self.right = right
        self.retType = retType

    def __str__(self):
        #super().__str__()
        return "(Binary Expression: Operator: {self.operator} Left: {self.left} Right: {self.right} RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = "("
        
        output += self.left.printNode(level) + " "

        output += self.operator.printNode(level) + " "
        
        output += self.right.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output
    

class Conditional_Expression(Expression, Node):
    def __init__(self, condExp, thenExp, elseExp, retType = None):
        self.condExp = condExp
        self.thenExp = thenExp
        self.elseExp = elseExp
        self.retType = retType
    
    def __str__(self):
        return "({self.condExp} ? {self.thenExp} : {self.elseExp} RetType: {self.retType})".format(self=self)
        pass

    def printNode(self, level):
        output = "("
        
        output += "(" + self.condExp.printNode(level) + ") ? "

        output += self.thenExp.printNode(level) + " : "
        
        output += self.elseExp.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output

class Var_Expression(Expression, Node):
    def __init__(self, identifier, retType = None):
        self.identifier = identifier
        self.retType = retType

    def __str__(self):
        return "({self.identifier} RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = "("
        
        output += self.identifier

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output
    

class Assignment_Expression(Expression, Node):
    def __init__(self, lvalue, exp, retType = None):
        self.lvalue = lvalue
        self.exp = exp
        self.retType = retType

    def __str__(self):
        return "({self.lvalue} = {self.exp} RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = "("
        
        output += self.lvalue.printNode(level) + " = "

        output += self.exp.printNode(level)

        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"

        return output
        

class FunctionCall_Exp(Expression, Node):
    def __init__(self, identifer, argumentList=None, retType = None):
        self.identifier = identifer
        self.argumentList = argumentList
        self.retType = retType
    
    def __str__(self):
        return "({self.identifier}({self.argumentList}) RetType: {self.retType})".format(self=self)
    
    def printNode(self, level):
        output = "("
        
        output += self.identifier

        output += "("
        if self.argumentList:
            for i in self.argumentList:
                output += i.printNode(level) + ", "

        output += ")"
                
        if self.retType:
            output +=  ' : ' + self.retType.printNode(level)

        output += ")"
        return output
    

class Const:
    pass

class ConstChar(Const, Node):
    def __init__(self, int):
        self.int = int
    
    def __str__(self):
        return "{self.int}".format(self=self)
    
    def printNode(self, level):
        return "{}".format(self.int)
    
    def __hash__(self):
        return hash((self.int))
    
    def __eq__(self, value):
        
        if not isinstance(value, ConstChar):
            return NotImplemented
        
        return self.int == value.int
    

class ConstUChar(Const, Node):
    def __init__(self, int):
        self.int = int
    
    def __str__(self):
        return "{self.int}".format(self=self)
    
    def printNode(self, level):
        return "{}".format(self.int)

    def __hash__(self):
        return hash((self.int))
    
    def __eq__(self, value):
        
        if not isinstance(value, ConstUChar):
            return NotImplemented
        
        return self.int == value.int
    
    """
    def __hash__(self):
        return 0
    
    def __eq__(self, value):
        print("EQUAL UCHAR")
        if type(value) == ConstUChar and self.int == value.int:
            return True
        
        return False
    """
    
class ConstInt(Const, Node):
    def __init__(self, int):
        self.int = int

    def __str__(self):
        return "{self.int}".format(self=self)
    
    def printNode(self, level):
        return "{}".format(self.int)
    
    def __hash__(self):
        return hash((self.int))
    
    def __eq__(self, value):
        
        if not isinstance(value, ConstInt):
            return NotImplemented
        
        return self.int == value.int

    """
    def __hash__(self):
        return 0
    
    def __eq__(self, value):
        print("EQUAL INT")
        if type(value) == ConstInt and self.int == value.int:
            return True
        
        return False
    """
    

class ConstLong(Const, Node):
    def __init__(self, int):
        self.int = int
    
    def __str__(self):
        return "{self.int}L".format(self=self)
    
    def printNode(self, level):
        return "{}".format(self.int)

    def __hash__(self):
        return hash((self.int))
    
    def __eq__(self, value):

        if not isinstance(value, ConstLong):
            return NotImplemented
        
        return self.int == value.int
    
    """
    def __hash__(self):
        return 0
    
    def __eq__(self, value):
        print("EQUAL LONG")
        if type(value) == ConstLong and self.int == value.int:
            return True
        
        return False
    """
    
class ConstUInt(Const, Node):
    def __init__(self, int):
        self.int = int

    def __str__(self):
        return "{self.int}U".format(self=self)
    
    def printNode(self, level):
        return "{}".format(self.int)
    
    def __hash__(self):
        return hash((self.int))
    
    def __eq__(self, value):
        
        if not isinstance(value, ConstUInt):
            return NotImplemented
        
        return self.int == value.int

    """
    def __hash__(self):
        return 0
    
    def __eq__(self, value):
        print("EQUAL UINT")
        if type(value) == ConstUInt and self.int == value.int:
            return True
        
        return False
    """

class ConstULong(Const, Node):
    def __init__(self, int):
        self.int = int
    
    def __str__(self):
        return "{self.int}UL".format(self=self)
    
    def printNode(self, level):
        return "{}".format(self.int)

    def __hash__(self):
        return hash((self.int))
    
    def __eq__(self, value):
        
        if not isinstance(value, ConstULong):
            return NotImplemented
        
        return self.int == value.int
    
    """
    def __hash__(self):
        return 0
    
    def __eq__(self, value):
        print("EQUAL ULONG")
        if type(value) == ConstULong and self.int == value.int:
            return True
        
        return False
    """
    
class ConstDouble(Const, Node):
    def __init__(self, double):
        self.double = double
    
    def __str__(self):
        return "{self.double}".format(self=self)
    
    def printNode(self, level):
        return "{}".format(self.double)
    
    def __hash__(self):
        return hash((self.double))
    
    def __eq__(self, value):
        
        if not isinstance(value, ConstDouble):
            return NotImplemented
        
        return self.double == value.double


class UnopType(Enum):
    NEGATE = 1
    COMPLEMENT = 2
    NOT = 3
    #DEREFERENCE = 4
    #ADDRESSOF = 5

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

class UnaryOperator(Operator, Node):
    def __init__(self, operator):
        self.operator = operator
    
    def __str__(self):
        #super().__str__()
        return "{self.operator}".format(self=self) 
    
    def printNode(self, level):
        return self.operator.name

class BinaryOperator(Operator, Node):
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        #super().__str__()
        return "{self.operator}".format(self=self) 
    
    def printNode(self, level):
        return self.operator.name

def takeToken(tokenList):
    if(tokenList != []):
        return tokenList.pop(0)
    
    print("No more tokens.")
    sys.exit(1)


def peek(tokenList, index=None):
    if(tokenList != []):  
        if index:
            if (len(tokenList) - 1) < index:
                return None
            else:
                return tokenList[index]
        else:
            return tokenList[0]
    
    return None
    print("No more tokens.")
    sys.exit(1)

def expect(expected, tokenList):
    actual = takeToken(tokenList)
    
    #print("actual: ", actual)
    if actual != ():
        if actual[1] != expected:
            traceback.print_stack()
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

def parseSignedInteger(token, v):
    if v > pow(2, 63) - 1:
        print("Constant is too large to represent as an int or long")
        sys.exit(1)
        pass

    if token[1] == TokenType.INT_CONSTANT and v <= pow(2, 31) - 1:
        return ConstInt(v)
    
    return ConstLong(v)

def parseUnsignedInteger(token, v):
    if v > pow(2, 64) - 1:
        print("Constant is too large to represent as an uint or ulong")
        sys.exit(1)
        

    if token[1] == TokenType.UINT_CONSTANT and v <= pow(2, 32) - 1:
        return ConstUInt(v)
    
    return ConstULong(v)

def parseConstant(tokenList):
    token = takeToken(tokenList)

    digitString = ""
    match token[1]:
        case TokenType.DOUBLE_CONSTANT:
            digitString = token[0]

        case TokenType.INT_CONSTANT:
            digitString = token[0]
        
        case _:
            #Se quita el Ll
            regex = "[0-9]+"
            result = re.match(regex, token[0])
            if result:
                digitString = result.group()

    match token[1]:
        case TokenType.DOUBLE_CONSTANT:
            v = float(digitString)
            #print(v)
            return ConstDouble(v)

        case _:
            v = int(digitString)

            match token[1]:
                case TokenType.INT_CONSTANT:
                    return parseSignedInteger(token, v)
                    
                case TokenType.LONG_CONSTANT:
                    return parseSignedInteger(token, v)
                    
                case TokenType.UINT_CONSTANT:
                    return parseUnsignedInteger(token, v)
                    
                case TokenType.ULONG_CONSTANT:
                    return parseUnsignedInteger(token, v)
            
    

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
            #case TokenType.AMPERSAND:
            #    return UnaryOperator(UnopType.ADDRESSOF)
            #case TokenType.ASTERISK:
            #    return UnaryOperator(UnopType.DEREFERENCE)
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
    if token[1] == TokenType.INT_CONSTANT or token[1] == TokenType.LONG_CONSTANT or token[1] == TokenType.UINT_CONSTANT or token[1] == TokenType.ULONG_CONSTANT or token[1] == TokenType.DOUBLE_CONSTANT: 
        return True
    
    return False
    

class AbstractDeclarator:
    pass

class AbstractPointer(AbstractDeclarator, Node):
    def __init__(self, abstractD):
        self.abstractD = abstractD
    
    def __str__(self):
        return "P{self.abstractD}".format(self=self)

class AbstractArray(AbstractDeclarator, Node):
    def __init__(self, abstractD, size):
        self.abstractD = abstractD
        self.size = size

    def __str__(self):
        return "Array({self.abstractD}, {self.size})".format(self=self)

class AbstractBase(AbstractDeclarator, Node):
    pass

    def __str__(self):
        return "".format(self=self)


def parseDirectAbstractDeclarator(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.OPEN_PAREN:
        takeToken(tokenList)
        abstractD = parseAbstractDeclarator(tokenList)
        expect(TokenType.CLOSE_PAREN, tokenList)

        token = peek(tokenList)

        if token[1] == TokenType.OPEN_BRACKET:
            arrayD = parseAbstractArrayDeclarator(tokenList, abstractD)

            token = peek(tokenList)

            while token[1] == TokenType.OPEN_BRACKET:
                arrayD = parseAbstractArrayDeclarator(tokenList, arrayD)
                token = peek(tokenList)
            
            return arrayD    

        return abstractD
    
    if token[1] == TokenType.OPEN_BRACKET:
        declarator = parseAbstractArrayDeclarator(tokenList, AbstractBase())

        token = peek(tokenList)

        while token[1] == TokenType.OPEN_BRACKET:
            declarator = parseAbstractArrayDeclarator(tokenList, declarator)
            token = peek(tokenList)
        
        return declarator
        
    print("Error: Invalid Direct Abstract Declaration.")
    sys.exit(1)
    
        

def parseAbstractDeclarator(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.ASTERISK:
        takeToken(tokenList)

        token = peek(tokenList)

        if token[1] == TokenType.ASTERISK or token[1] == TokenType.OPEN_PAREN or token[1] == TokenType.OPEN_BRACKET:

            abstractD = parseAbstractDeclarator(tokenList)
            return AbstractPointer(abstractD)
        
        return AbstractPointer(AbstractBase())

    return parseDirectAbstractDeclarator(tokenList)

    #direct abstract declarator
    if token[1] == TokenType.OPEN_PAREN:
        takeToken(tokenList)
        abstractD = parseAbstractDeclarator(tokenList)
        expect(TokenType.CLOSE_PAREN, tokenList)
        return abstractD

def processAbstractDeclarator(abstractD, baseType):

    match abstractD:
        case AbstractBase():
            return baseType

        case AbstractPointer(abstractD = abstractD):
            derivedType = PointerType(baseType)
            return processAbstractDeclarator(abstractD, derivedType)
        
        case AbstractArray(abstractD = abstractD, size = size):
            aT = ArrayType(baseType, size)
            return processAbstractDeclarator(abstractD, aT)

        case _:
            print("Error: Invalid Abstract Declarator.")
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


def UnaryOperatorToken(token):
    if token != ():
        if token[1] == TokenType.TILDE or token[1] == TokenType.HYPHEN or token[1] == TokenType.EXCLAMATION or token[1] == TokenType.ASTERISK or token[1] == TokenType.AMPERSAND:
            return True

    return False

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

def parsePrimaryExp(tokenList):

    nextT = peek(tokenList, 1)
    token = peek(tokenList)

    if token[1] == TokenType.IDENTIFIER and nextT[1] == TokenType.OPEN_PAREN:
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
        return Constant_Expression(const)
    
    elif token[1] == TokenType.IDENTIFIER:
        id = parseIdentifier(tokenList)
        return Var_Expression(id)

    elif token[1] == TokenType.OPEN_PAREN:
        takeToken(tokenList)
        inner_exp = parseExp(tokenList, 0)
        expect(TokenType.CLOSE_PAREN, tokenList)
        return inner_exp
    
    elif token[1] == TokenType.STRING_LITERAL:
        sLL = []
        sLL.append(takeToken(tokenList)[0])
        
        token = peek(tokenList)
        while token[1] == TokenType.STRING_LITERAL:
            sLL.append(takeToken(tokenList)[0])
            token = peek(tokenList)
        
        result = "".join(sLL)
        #print(result)
        return StringExpression(result)
        
    else:
        print("Malformed expression at Line {0}.".format(token[2]))
        sys.exit(1)

def parseSubscript(tokenList, ptrExp):
    takeToken(tokenList)
    indexExp = parseExp(tokenList, 0)
    expect(TokenType.CLOSE_BRACKET, tokenList)

    return Subscript(ptrExp, indexExp)

def parseDotOperator(tokenList, struct):
    takeToken(tokenList)
    member = parseIdentifier(tokenList)
    return Dot(struct, member)

def parseArrowOperator(tokenList, pointer):
    takeToken(tokenList)
    member = parseIdentifier(tokenList)
    return Arrow(pointer, member)

def parsePostFixOp(tokenList, primaryExp):

    token = peek(tokenList)

    match token[1]:
        case TokenType.OPEN_BRACKET:
            return parseSubscript(tokenList, primaryExp)
        
        case TokenType.PERIOD:
            return parseDotOperator(tokenList, primaryExp)
        
        case TokenType.ARROW:
            return parseArrowOperator(tokenList, primaryExp)
            
    

def parsePostfixExp(tokenList):

    primaryExp = parsePrimaryExp(tokenList)

    #op = parsePostFixOp(tokenList)

    token = peek(tokenList)

    def isPostFixOpToken(token):
        if token[1] == TokenType.OPEN_BRACKET or token[1] == TokenType.PERIOD or token[1] == TokenType.ARROW:
            return True
        
        return False
    
    if isPostFixOpToken(token):

        sS = parsePostFixOp(tokenList, primaryExp)
        #sS = parseSubscript(tokenList, primaryExp)

        token = peek(tokenList)
        #while token[1] == TokenType.OPEN_BRACKET:
        while isPostFixOpToken(token):
            sS = parsePostFixOp(tokenList, sS)
            #sS = parseSubscript(tokenList, sS)
            token = peek(tokenList)
                 
        return sS
    
    """
    if token[1] == TokenType.PERIOD:
        takeToken(tokenList)
        exp = parsePostfixExp(tokenList)
        #member = parseIdentifier(tokenList)
        return Dot(primaryExp, exp)
    
    if token[1] == TokenType.ARROW:
        takeToken(tokenList)
        exp = parsePostfixExp(tokenList)
        #member = parseIdentifier(tokenList)
        return Arrow(primaryExp, exp)
    """
        

    return primaryExp
    

def parseUnaryExp(tokenList):
    
    token = peek(tokenList)

    if UnaryOperatorToken(token):
        if token[1] == TokenType.ASTERISK:
            takeToken(tokenList)
            inner_exp = parseCastExp(tokenList)
            return Dereference(inner_exp)
        
        elif token[1] == TokenType.AMPERSAND:
            takeToken(tokenList)
            inner_exp = parseCastExp(tokenList)
            return AddrOf(inner_exp)
        
        else:
            unop = parseUnop(tokenList)
            inner_exp = parseCastExp(tokenList)
            return Unary_Expression(unop, inner_exp)
        
    if token[1] == TokenType.SIZEOF_KW:
        takeToken(tokenList)

        nextToken = peek(tokenList, 1)
        token = peek(tokenList)

        if token[1] == TokenType.OPEN_PAREN and isTypeSpecifier(nextToken):
            takeToken(tokenList)
            type = parseTypeName(tokenList)
            expect(TokenType.CLOSE_PAREN, tokenList)
            return SizeOfT(type)
            
        exp = parseUnaryExp(tokenList)
        return SizeOf(exp)
        
    return parsePostfixExp(tokenList)
        

def parseTypeName(tokenList):
    
    token = peek(tokenList)

    types = []
    while isTypeSpecifier(token):
        typeSpec = parseTypeSpecifier(tokenList)
        types.append(typeSpec)
        token = peek(tokenList)

    type = parseTypes(types)

    token = peek(tokenList)

    if token[1] == TokenType.ASTERISK or token[1] == TokenType.OPEN_PAREN or token[1] == TokenType.OPEN_BRACKET:

        abstractD = parseAbstractDeclarator(tokenList)
        type = processAbstractDeclarator(abstractD, type)

        return type

    return type


def parseCastExp(tokenList):
    token = peek(tokenList)
    nextToken = peek(tokenList, 1)

    if token[1] == TokenType.OPEN_PAREN and isTypeSpecifier(nextToken):
        takeToken(tokenList)
        type = parseTypeName(tokenList)
        print(type)
        expect(TokenType.CLOSE_PAREN, tokenList)
        exp = parseCastExp(tokenList)
        return Cast_Expression(type, exp)
        
    return parseUnaryExp(tokenList)

def parseExp(tokenList, min_prec):
    #left = parseUnaryExp(tokenList)
    left = parseCastExp(tokenList)
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
        
        token = peek(tokenList)

        if token[1] == TokenType.SEMICOLON:
            expect(TokenType.SEMICOLON, tokenList)
            return ReturnStmt() 
        else:
            retVal = parseExp(tokenList, 0)
            expect(TokenType.SEMICOLON, tokenList)
            return ReturnStmt(retVal) 

    
    elif token[1] == TokenType.SEMICOLON:
        #breakpoint()
        takeToken(tokenList)
        return NullStatement()
    else:
        #breakpoint()
        retVal = parseExp(tokenList, 0)
        expect(TokenType.SEMICOLON, tokenList)
        return ExpressionStmt(retVal)

def parseTypes(rawTypes):

    types = [type(x) for x in rawTypes]

    print(types)

    if types == []:
        traceback.print_stack()
        print("Invalid Type Specifier Empty list.")
        sys.exit(1)

    if types == [Struct]:
        print(rawTypes[0].identifier)
        return StuctureType(rawTypes[0].identifier)
    
    if Struct in types:
        print("Error: Can't combine Struct type with other type specifiers.")
        sys.exit(1)

    if types == [Void]:
        return VoidType()
    
    if Void in types:
        print("Error: Can't combine void with other type specifiers.")
        sys.exit(1)

    if types == [Double]:
        return DoubleType()
                
    if Double in types:
        print("Error: Can't combine double with other type specifiers.")
        sys.exit(1)

    setTypes = set(types)

    if len(setTypes) != len(types):
        traceback.print_stack()
        print("Invalid Type Specifier.")
        sys.exit(1)
    
    if Unsigned in setTypes and Signed in setTypes:
        print("Invalid Type Specifier signed and unsigned.")
        sys.exit(1)

    if len(setTypes) == 2 and Unsigned in setTypes and Char in setTypes:
        return UCharType()
    
    if len(setTypes) == 2 and Signed in setTypes and Char in setTypes:
        return SCharType()

    if len(setTypes) == 1 and Char in setTypes:
        return CharType()
    
    if Char in setTypes:
        print("Error: Can't combine char with other type specifiers.")
        sys.exit(1)

    if Unsigned in setTypes and Long in setTypes:
        return ULongType()
        
    if Unsigned in setTypes:
        return UIntType()
    
    if Long in setTypes:
        return LongType()
    
    return IntType()
    
"""
Osea esos no tienen orden pero esos si!
"""
def parseTypeAndStorageClass(specifierList):
    print(specifierList)

    types = []
    storageClasses = []
    
    for specifier in specifierList:
        if type(specifier) == TypeS:
            types.append(specifier.typeSpec)

        #if specifier[1] ==  TokenType.INT_KW or specifier[1] == TokenType.LONG_KW:
        else:
            storageClasses.append(specifier)
            
    type_ = parseTypes(types)

    print(type_)

    if len(storageClasses) > 1:
        print("Invalid Storage Class.")
        sys.exit(1)

    storageClass = StorageClass(StorageType.NULL)

    if len(storageClasses) == 1:
        s = type(storageClasses[0])
        if s == Extern:
            storageClass = StorageClass(StorageType.EXTERN)

        elif s == Static:
            storageClass = StorageClass(StorageType.STATIC)

        else:
            print("Error: Invalid Storage Class: {0}".format(s[0]))
            
    return type_, storageClass

class Specifier():
    pass

class TypeS(Specifier, Node):
    def __init__(self, typeSpec):
        self.typeSpec = typeSpec
    
class Extern(Specifier, Node):
    pass

class Static(Specifier, Node):
    pass

def parseSpecifier(tokenList):
    token = peek(tokenList)

    match token[1]:
        case TokenType.EXTERN_KW:
            takeToken(tokenList)
            return Extern()
        
        case TokenType.STATIC_KW:
            takeToken(tokenList)
            return Static()
        
        case _:
            typeSpec = parseTypeSpecifier(tokenList)
            print(typeSpec)
            return TypeS(typeSpec)

def isSpecifier(token):
    if token[1] == TokenType.EXTERN_KW or token[1] == TokenType.STATIC_KW or isTypeSpecifier(token): 
        return True
    return False

def parseSimpleDeclarator(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.IDENTIFIER:
        token = takeToken(tokenList)
        return Ident(token[0])
        
    if token[1] == TokenType.OPEN_PAREN:
        token = takeToken(tokenList)
        declarator = parseDeclarator(tokenList)
        expect(TokenType.CLOSE_PAREN, tokenList)
        return declarator
        
    print("Error: Invalid Simple Declarator.")
    sys.exit(1)

def parseAbstractArrayDeclarator(tokenList, sDeclarator):

    takeToken(tokenList)

    constant = parseExp(tokenList, 0)
    
    if type(constant) != Constant_Expression:
        print("Error: Array size must be a constant expression.")
        sys.exit(1)
    
    constant = constant.const

    if type(constant) == ConstDouble:
        print("Error: Array size can't be a double constant.")
        sys.exit(1)
    
    if constant.int < 1:
        print("Error: Array size must be greater than 0.")
        sys.exit(1)

    expect(TokenType.CLOSE_BRACKET, tokenList)

    return AbstractArray(sDeclarator, constant.int)

def parseArrayDeclarator(tokenList, sDeclarator):

    takeToken(tokenList)

    constant = parseExp(tokenList, 0)
    
    if type(constant) != Constant_Expression:
        print("Error: Array size must be a constant expression.")
        sys.exit(1)
    
    constant = constant.const

    if type(constant) == ConstDouble:
        print("Error: Array size can't be a double constant.")
        sys.exit(1)
    
    if constant.int < 1:
        print("Error: Array size must be greater than 0.")
        sys.exit(1)

    expect(TokenType.CLOSE_BRACKET, tokenList)

    return ArrayDeclarator(sDeclarator, constant.int)

def parseDirectDeclarator(tokenList):

    sDeclarator = parseSimpleDeclarator(tokenList)
    
    token = peek(tokenList)

    if token[1] == TokenType.OPEN_PAREN:
        paramInfos = parseParamList(tokenList) 
        return FunDeclarator(paramInfos, sDeclarator)

    #one or many    
    if token[1] == TokenType.OPEN_BRACKET:
        declarator = parseArrayDeclarator(tokenList, sDeclarator)
        
        token = peek(tokenList)

        while token[1] == TokenType.OPEN_BRACKET:
            declarator = parseArrayDeclarator(tokenList, declarator)
            token = peek(tokenList)
            

        return declarator
            
    return sDeclarator

def parseDeclarator(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.ASTERISK:
        takeToken(tokenList)
        declarator = parseDeclarator(tokenList)
        return PointerDeclarator(declarator)
    
    return parseDirectDeclarator(tokenList)


def processDeclarator(declarator, baseType):
    match declarator:
        case Ident(identifier=id):
            return id, baseType, []
        
        case PointerDeclarator(declarator = declarator):
            derivedType = PointerType(baseType)
            return processDeclarator(declarator, derivedType)
            
        case FunDeclarator(paramInfoList = paramInfoList, declarator = declarator):
            
            match declarator:
                case Ident(identifier=id):
                    paramNames = []
                    paramTypes = []
                    for param in paramInfoList:
                        paramName, paramType, _ = processDeclarator(param.declarator, param.type)
                        if type(paramType) == FunType:
                            print("Error: Function pointers in parameters are not supported.")
                            sys.exit(1)

                        paramTypes.append(paramType)
                        paramNames.append(paramName)
                    
                    fType = FunType(paramTypes, baseType)
                    return id, fType, paramNames

                case _:
                    print("Error: Can't apply additional type derivations to a function type.")
                    sys.exit(1)

        case ArrayDeclarator(declarator = inner, size = size):
            aT = ArrayType(baseType, size)
            return processDeclarator(inner, aT)
        
        case _:
            print("Errror: Invalid Decalarator.")
            sys.exit(1)

def parseMemberDeclaration(tokenList):
    
    types = []
    
    token = peek(tokenList)
    while isTypeSpecifier(token):
        typeSpec = parseTypeSpecifier(tokenList)
        types.append(typeSpec)
        token = peek(tokenList)

    baseType = parseTypes(types)

    declarator = parseDeclarator(tokenList)

    name, declType, params = processDeclarator(declarator, baseType)

    print(type(declType))
    match declType:
        case FunType():
            print("Error: Struct members cannot be functions.")
            sys.exit(1)

    expect(TokenType.SEMICOLON, tokenList)

    return MemberDecl(name, declType)


def parseStructDeclaration(tokenList):
    tag = parseIdentifier(tokenList)


    token = peek(tokenList)

    memberList = []
    if token[1] == TokenType.OPEN_BRACE:
        takeToken(tokenList)

        token = peek(tokenList)
        while token[1] != TokenType.CLOSE_BRACE:
            memberList.append(parseMemberDeclaration(tokenList))
            token = peek(tokenList)
        
        if memberList == []:
            print("Error: Struct member list cannot be empty.")
            sys.exit(1)

        takeToken(tokenList)

    expect(TokenType.SEMICOLON, tokenList)
        
    return StructDeclaration(tag, memberList)
    

def parseDeclaration(tokenList):

    token = peek(tokenList)
    braceToken = peek(tokenList, 2)

    if token[1] == TokenType.STRUCT_KW and (braceToken[1] == TokenType.OPEN_BRACE or braceToken[1] == TokenType.SEMICOLON):
        takeToken(tokenList)
        structDecl = parseStructDeclaration(tokenList)
        return True, StructDecl(structDecl)
    
    if isSpecifier(token) == False:
        return False, None
    
    specifierList = []
    while isSpecifier(token):
        spec = parseSpecifier(tokenList)
        specifierList.append(spec)
        token = peek(tokenList)
        
    baseType, storageClass = parseTypeAndStorageClass(specifierList)

    declarator = parseDeclarator(tokenList)

    print(baseType, declarator)

    name, declType, params = processDeclarator(declarator, baseType)

    print(declType)

    if type(declType) == FunType:
        f = parseFunctionDecl(tokenList, name, declType, params, storageClass)
        return True, FunDecl(f)
    else:
        v = parseVarDecl(tokenList, name, declType, storageClass)
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
        #breakpoint()
        BlockItem = parseBlockItem(tokenList)
        BlockItemList.append(BlockItem)
        
    takeToken(tokenList)

    return Block(BlockItemList)

class TypeSpecifier():
    pass

class Int(TypeSpecifier, Node):
    pass

class Long(TypeSpecifier, Node):
    pass

class Unsigned(TypeSpecifier, Node):
    pass

class Signed(TypeSpecifier, Node):
    pass

class Double(TypeSpecifier, Node):
    pass

class Char(TypeSpecifier, Node):
    pass

class Void(TypeSpecifier, Node):
    pass

class Struct(TypeSpecifier, Node):
    def __init__(self, identifier):
        self.identifier = identifier


def parseTypeSpecifier(tokenList):
    token = peek(tokenList)
    match token[1]:
        case TokenType.INT_KW:
            takeToken(tokenList)
            return Int()
        
        case TokenType.LONG_KW:
            takeToken(tokenList)
            return Long()
        
        case TokenType.SIGNED_KW:
            takeToken(tokenList)
            return Signed()
        
        case TokenType.UNSIGNED_KW:
            takeToken(tokenList)
            return Unsigned()
        
        case TokenType.DOUBLE_KW:
            takeToken(tokenList)
            return Double()
        
        case TokenType.CHAR_KW:
            takeToken(tokenList)
            return Char()
        
        case TokenType.VOID_KW:
            takeToken(tokenList)
            return Void()

        case TokenType.STRUCT_KW:
            takeToken(tokenList)
            identifier = parseIdentifier(tokenList)
            return Struct(identifier)

        case _:
            traceback.print_stack()
            print("Error: Invalid type specifier. {0}".format(tokenList))
            sys.exit(1)

def isTypeSpecifier(token):
    if token[1] == TokenType.INT_KW or token[1] == TokenType.LONG_KW or token[1] == TokenType.SIGNED_KW or token[1] == TokenType.UNSIGNED_KW or token[1] == TokenType.DOUBLE_KW or token[1] == TokenType.CHAR_KW or token[1] == TokenType.VOID_KW or token[1] == TokenType.STRUCT_KW: 
        return True
    
    return False

def parseParam(tokenList):
    types = []
    
    token = peek(tokenList)
    while isTypeSpecifier(token):
        typeSpec = parseTypeSpecifier(tokenList)
        types.append(typeSpec)
        #types.append(takeToken(tokenList))
        token = peek(tokenList)

    type = parseTypes(types)
    declarator = parseDeclarator(tokenList)

    return Param(type, declarator)
    
def parseParamList(tokenList):
    paramList = []

    expect(TokenType.OPEN_PAREN, tokenList)

    token = peek(tokenList)
    nextToken = peek(tokenList, 1)

    if token[1] == TokenType.VOID_KW and nextToken[1] == TokenType.CLOSE_PAREN:
        takeToken(tokenList)
        takeToken(tokenList)
        return paramList

    param = parseParam(tokenList)    
    paramList.append(param)

    token = peek(tokenList)

    while token[1] == TokenType.COMMA:
        takeToken(tokenList)
        
        param = parseParam(tokenList)
        paramList.append(param)
        token = peek(tokenList)

    expect(TokenType.CLOSE_PAREN, tokenList)

    return paramList


def parseInitilizer(tokenList):
    token = peek(tokenList)

    if token[1] == TokenType.OPEN_BRACE:
        initList = []

        takeToken(tokenList)
        init = parseInitilizer(tokenList)
        initList.append(init)

        token = peek(tokenList)

        while token[1] == TokenType.COMMA:
            takeToken(tokenList)

            token = peek(tokenList)

            if token[1] == TokenType.CLOSE_BRACE:
                break

            init = parseInitilizer(tokenList)
            initList.append(init)

            token = peek(tokenList)

        expect(TokenType.CLOSE_BRACE, tokenList)

        return CompoundInit(initList)

    exp = parseExp(tokenList, 0)    
    
    return SingleInit(exp)
    
def parseVarDecl(tokenList, name, type, storageClass):

    token = peek(tokenList)

    init = None
    if token[1] == TokenType.EQUAL:
        takeToken(tokenList)
        init = parseInitilizer(tokenList)

    expect(TokenType.SEMICOLON, tokenList)
    return VariableDecl(name, type, init, storageClass) 


def parseFunctionDecl(tokenList, name, type, params, storageClass):

    token = peek(tokenList)

    block = None

    if token[1] == TokenType.SEMICOLON:
        takeToken(tokenList)
    else:
        block = parseBlock(tokenList)

    return FunctionDecl(name, type, params, block, storageClass)

class Declarator:
    pass

class Ident(Declarator):
    def __init__(self, identifier):
        self.identifier = identifier
    
    def __str__(self):
        return "(IdenDeclarator: {self.identifier})".format(self=self)

class PointerDeclarator(Declarator):
    def __init__(self, declarator):
        self.declarator = declarator

    def __str__(self):
        return "(PointerDeclarator: {self.declarator})".format(self=self)

class ArrayDeclarator(Declarator):
    def __init__(self, declarator, size):
        self.declarator = declarator
        self.size = size

    def __str__(self):
        return "(ArrayDeclarator: {self.declarator}, {self.size})".format(self=self)


class FunDeclarator(Declarator):
    def __init__(self, paramInfoList, declarator):
        self.paramInfoList = paramInfoList
        self.declarator = declarator
    
    def __str__(self):
        return "(FunDeclarator: {self.declarator} {self.paramInfoList})".format(self=self)

class ParamInfo():
    pass

class Param(ParamInfo):
    def __init__(self, type, declarator):
        self.type = type
        self.declarator = declarator
    
    def __str__(self):
        return "{self.type} {self.declarator}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    


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

