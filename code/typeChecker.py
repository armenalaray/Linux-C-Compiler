import sys
import traceback
from enum import Enum
import ctypes
import parser

import assemblyGenerator

from semanticAnalysis import makeTemporary

class Entry:
    def __init__(self, name, attrs, type, funType=None):
        self.name = name
        self.attrs = attrs
        self.type = type
        
    def __str__(self):
        return "{self.name} {self.type} {self.attrs}".format(self=self)
    
    def __repr__(self):
        return self.__str__()


class IdentifierAttributes:
    pass

class FunAttributes(IdentifierAttributes):
    def __init__(self, defined, global_):
        self.defined = defined
        self.global_ = global_
    
    def __str__(self):
        return "Defined: {self.defined} Global: {self.global_}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

 
class StaticAttributes(IdentifierAttributes):
    def __init__(self, initialVal, global_):
        self.initialVal = initialVal
        self.global_ = global_
    
    def __str__(self):
        return "InitialVal: {self.initialVal} Global: {self.global_}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class LocalAttributes(IdentifierAttributes):
    pass

class ConstantAttr(IdentifierAttributes):
    def __init__(self, staticInit):
        self.staticInit = staticInit

    def __str__(self):
        return "{self.staticInit}".format(self=self)


class InitialValue:
    pass

class Tentative(InitialValue):
    pass

class Initial(InitialValue):
    def __init__(self, initList):
        self.initList = initList

    def __str__(self):
        return "InitialList: {self.initList}".format(self=self)

class NoInitializer(InitialValue):
    pass

class StaticInit:
    def __repr__(self):
        return self.__str__()
    
class CharInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_int8(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)
    
class UCharInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_uint8(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)

class IntInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_int32(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)

class LongInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_int64(int(int_))

    def __str__(self):
        return "{self.int}".format(self=self)

class UIntInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_uint32(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)


class ULongInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_uint64(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)

class DoubleInit(StaticInit):
    def __init__(self, double):
        self.double = ctypes.c_double(double)
    
    def __str__(self):
        return "{self.double}".format(self=self)

class StringInit(StaticInit):
    def __init__(self, string, nullT):
        self.string = string
        self.nullT = nullT
    
    def __str__(self):
        return "({self.string}, AddZero: {self.nullT})".format(self=self)

class PointerInit(StaticInit):
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return "PointerInit: {self.name}".format(self=self)


class ZeroInit(StaticInit):
    def __init__(self, bytes):
        self.bytes = bytes

    def __str__(self):
        return "{self.bytes}".format(self=self)

def getCommonType(type1, type2):
    
    if isCharacterType(type1):
        type1 = parser.IntType()

    if isCharacterType(type2):
        type2 = parser.IntType()

    if type1.checkType(type2):
        return type1
    
    if type(type1) == parser.DoubleType or type(type2) == parser.DoubleType:
        return parser.DoubleType()
    
    if type1.size == type2.size:
        if type1.isSigned:
            return type2
        else:
            return type1
    
    if type1.size > type2.size:
        return type1
    else:
        return type2

def convertTo(exp, resultType):
    if exp.retType.checkType(resultType):
        return exp
    
    return parser.Cast_Expression(resultType, exp, resultType)

def isNullPointerConstant(exp):
    match exp:
        case parser.Constant_Expression(const = const):
            match const:
                case parser.ConstInt(int = int):
                    if int == 0:
                        return True
                    
                case parser.ConstLong(int = int):
                    if int == 0:
                        return True
                    
                case parser.ConstUInt(int = int):
                    if int == 0:
                        return True
                    
                case parser.ConstULong(int = int):
                    if int == 0:
                        return True
        
    return False


def getCommonPointerType(exp1, exp2):
    #si los dos son punteros regresas puntero

    type1 = exp1.retType
    type2 = exp2.retType

    if type1.checkType(type2):
        return type1
    
    elif isNullPointerConstant(exp1):
        return type2
    elif isNullPointerConstant(exp2):
        return type1
    elif type(type1) == parser.PointerType and type(type1.referenceType) == parser.VoidType and type(type2) == parser.PointerType:
        print("Ale 1")
        return parser.PointerType(parser.VoidType())
    elif type(type2) == parser.PointerType and type(type2.referenceType) == parser.VoidType and type(type1) == parser.PointerType:
        print("Ale 2")
        return parser.PointerType(parser.VoidType())

    print("Error: Expressions have incompatible types. {0} and {1}".format(type1, type2))
    sys.exit(1)


def isCharacterType(targetType):
    if type(targetType) == parser.CharType or type(targetType) == parser.SCharType or type(targetType) == parser.UCharType:
        return True
    return False

def isIntegerType(targetType):
    if isCharacterType(targetType) or type(targetType) == parser.IntType or type(targetType) == parser.LongType or type(targetType) == parser.UIntType or type(targetType) == parser.ULongType:
        return True
    
    return False

def isArithmeticType(targetType):
    if isIntegerType(targetType) or type(targetType) == parser.DoubleType:
        return True
    
    return False
    

def convertByAssignment(exp, targetType):
    
    if exp.retType.checkType(targetType):
        return exp

    if isArithmeticType(exp.retType) and isArithmeticType(targetType):
        return convertTo(exp, targetType)

    if isNullPointerConstant(exp) and type(targetType) == parser.PointerType:
        return convertTo(exp, targetType)
    
    if type(targetType) == parser.PointerType and type(targetType.referenceType) == parser.VoidType and type(exp.retType) == parser.PointerType:
        return convertTo(exp, targetType)
    if type(exp.retType) == parser.PointerType and type(exp.retType.referenceType) == parser.VoidType and type(targetType) == parser.PointerType:
        return convertTo(exp, targetType)
    
    print("Error: Cannot convert type for assignment. {0} and {1}".format(exp.retType, targetType))
    sys.exit(1)


def typeCheckAndConvert(exp, symbolTable):
    typedExp = typeCheckExpression(exp, symbolTable)
    match typedExp.retType:
        case parser.ArrayType(elementType = elementType, size = size):
            return parser.AddrOf(typedExp, parser.PointerType(elementType))
        
        case _:
            return typedExp

def isAnLvalue(exp):
    if type(exp) == parser.StringExpression or type(exp) == parser.Var_Expression or type(exp) == parser.Dereference or type(exp) == parser.Subscript:
        return True
    
    return False

def isComplete(t):
    if type(t) != parser.VoidType:
        return True
    
    return False

def isPointerToComplete(t):
    match t:
        case parser.PointerType(referenceType = referenceType):
            return isComplete(referenceType)
        case _:
            return False

def validateTypeSpecifier(t):

    match t:
        case parser.ArrayType(elementType = elementType, size = size):
            if not isComplete(elementType):
                print("Error: Illegal array of incomplete type.")
                sys.exit(1)

            validateTypeSpecifier(elementType)

        case parser.PointerType(referenceType = referenceType):
            validateTypeSpecifier(referenceType)
            
        case parser.FunType(paramTypes = paramTypes, retType = retType):
            for paramType in paramTypes:
                validateTypeSpecifier(paramType)
            
            validateTypeSpecifier(retType)

        case _:
            return

def typeCheckExpression(exp, symbolTable):
    match exp:

        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            
            ## NEW CODE
            paramCount = 0
            if argumentList:
                paramCount = len(argumentList)

            #aqui estoy buscando la declaracion de la funcion
            match symbolTable[id].type:
                case parser.FunType(paramTypes = paramTypes, retType = retType):
                    if len(paramTypes) != paramCount:
                        print("Error: Function {0}() called with the wrong number of arguments.".format(id))
                        sys.exit(1)

                    if argumentList:

                        convertedArgs = []
                        for exp, targetType in zip(argumentList, paramTypes):

                            exp = typeCheckAndConvert(exp, symbolTable)
                            #exp = typeCheckExpression(exp, symbolTable)

                            exp = convertByAssignment(exp, targetType)

                            convertedArgs.append(exp)
                        
                        print(convertedArgs)

                        return parser.FunctionCall_Exp(id, convertedArgs, retType)
                    
                    return parser.FunctionCall_Exp(id, None, retType)
                    
                case _:
                    print("Error: Variable {0} used as function name.".format(id))
                    sys.exit(1)

        case parser.StringExpression(string = string):
            return parser.StringExpression(string, parser.ArrayType(parser.CharType(), len(string) + 1))

        case parser.Dereference(exp = exp):
            typedInner = typeCheckAndConvert(exp, symbolTable)
            
            match typedInner.retType:
                case parser.PointerType(referenceType = referenceType):

                    if not isComplete(referenceType):
                        print("Error: Cannot dereference pointer to void.")
                        sys.exit(1)         

                    return parser.Dereference(typedInner, referenceType)

                case _:
                    print("Error: Cannot derefence a non-pointer.")
                    sys.exit(1)

        case parser.Subscript(ptrExp = e1, indexExp = e2):
            typedE1 = typeCheckAndConvert(e1, symbolTable)
            typedE2 = typeCheckAndConvert(e2, symbolTable)

            ptrType = None

            #if type(typedE1.retType) == parser.PointerType and isIntegerType(typedE2.retType):
            if isPointerToComplete(typedE1.retType) and isIntegerType(typedE2.retType):
                ptrType = typedE1.retType
                typedE2 = convertTo(typedE2, parser.LongType())

            #elif isIntegerType(typedE1.retType) and type(typedE2.retType) == parser.PointerType:
            elif isIntegerType(typedE1.retType) and isPointerToComplete(typedE2.retType):
                ptrType = typedE2.retType
                typedE1 = convertTo(typedE1, parser.LongType())
            
            else:
                print("Error: Invalid subscript operation. {0} and {1}".format(typedE1.retType, typedE2.retType))
                sys.exit(1)

            return parser.Subscript(typedE1, typedE2, ptrType.referenceType)
            
        case parser.AddrOf(exp = exp):
            
            if not isAnLvalue(exp):
                print("Error: Can't take the address of a non-lvalue.")
                sys.exit(1)
            
            typedInner = typeCheckExpression(exp, symbolTable)
            retType = parser.PointerType(typedInner.retType)
            return parser.AddrOf(typedInner, retType)

        case parser.Cast_Expression(targetType = targetType, exp = exp):
            e = typeCheckAndConvert(exp, symbolTable)
            
            validateTypeSpecifier(targetType)
            validateTypeSpecifier(e.retType)

            if (type(e.retType) == parser.PointerType and type(targetType) == parser.DoubleType) or (type(e.retType) == parser.DoubleType and type(targetType) == parser.PointerType):
                print("Error: Casting pointer to double or a double to a pointer.")
                sys.exit(1)

            if type(targetType) == parser.VoidType:
                return parser.Cast_Expression(targetType, e, parser.VoidType())
            
            if not isScalar(targetType):
                print("Error: Can only cast to scalar type or void.")
                sys.exit(1)
            
            if not isScalar(e.retType):
                print("Error: Cannot cast non scalar expression to scalar type.")
                sys.exit(1)

            else:
                return parser.Cast_Expression(targetType, e, targetType)

        case parser.Var_Expression(identifier = id):
            if type(symbolTable[id].type) == parser.FunType:
                print("ERROR: Function {0}() used as variable.".format(id))
                sys.exit(1)
            
            return parser.Var_Expression(id, symbolTable[id].type)
        
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            l = typeCheckAndConvert(lvalue, symbolTable)
            
            if not isAnLvalue(l):
                print("Error: Tried to assign to a non-lvalue.")
                sys.exit(1)
                
            r = typeCheckAndConvert(exp, symbolTable)
            r = convertByAssignment(r, l.retType)
            return parser.Assignment_Expression(l, r, l.retType)
            
        case parser.Constant_Expression(const=const):
            #print(type(const))
            match const:
                case parser.ConstInt():
                    return parser.Constant_Expression(const, parser.IntType())
                
                ##NOTE: Lo vas a hacer despues!
                case parser.ConstLong():
                    return parser.Constant_Expression(const, parser.LongType())
                
                case parser.ConstUInt():
                    return parser.Constant_Expression(const, parser.UIntType())
                
                case parser.ConstULong():
                    return parser.Constant_Expression(const, parser.ULongType())
                
                case parser.ConstDouble():
                    return parser.Constant_Expression(const, parser.DoubleType())

                case _:
                    print("Invalid Constant Type. {0}".format(type(const)))
                    sys.exit(1)

        case parser.Unary_Expression(operator=op, expression=exp_):
            e = typeCheckAndConvert(exp_, symbolTable)
            
            match op.operator:
                case parser.UnopType.COMPLEMENT:
                    if type(e.retType) == parser.DoubleType:
                        print("Error: Can't take the bitwise complement of a double.")
                        sys.exit(1)
                    
                    if type(e.retType) == parser.PointerType:
                        print("Error: Can't take the bitwise complement of a pointer.")
                        sys.exit(1)
                    
                    if isCharacterType(e.retType):
                        e = convertTo(e, parser.IntType())
                        
                    return parser.Unary_Expression(op, e, e.retType)

                case parser.UnopType.NEGATE:
                    if type(e.retType) == parser.PointerType:
                        print("Error: Can't negate a pointer.")
                        sys.exit(1)
                    
                    if not isComplete(e.retType):
                        print("Error: Cannot negate void expressions.")
                        sys.exit(1)

                    if isCharacterType(e.retType):
                        e = convertTo(e, parser.IntType())
                        
                    return parser.Unary_Expression(op, e, e.retType)

                case parser.UnopType.NOT:
                    if not isScalar(e.retType):
                        print("Error: Logical operators only apply to escalar expressions.")
                        sys.exit(1)

                    return parser.Unary_Expression(op, e, parser.IntType())
                    
                case _:
                    return parser.Unary_Expression(op, e, e.retType)
                          
        case parser.Binary_Expression(operator=op, left=left, right=right):
            
            def typeCheckCommonArithmeticBinaryExp(op, l, r):
                match op.operator:        
                    case parser.BinopType.MULTIPLY:

                        if type(l.retType) == parser.PointerType or type(r.retType) == parser.PointerType:
                            print("Error: Can't multiply a pointer.")
                            sys.exit(1)

                    case parser.BinopType.DIVIDE:

                        if type(l.retType) == parser.PointerType or type(r.retType) == parser.PointerType:
                            print("Error: Can't divide a pointer.")
                            sys.exit(1)

                    case parser.BinopType.MODULO:

                        if type(l.retType) == parser.PointerType or type(r.retType) == parser.PointerType:
                            print("Error: Can't take the modulo of a pointer.")
                            sys.exit(1)
                            

                        if type(l.retType) == parser.DoubleType or type(r.retType) == parser.DoubleType:
                            print("Error: Can't take the modulo of a double.")
                            sys.exit(1)

                    case parser.BinopType.AND:
                        if (not isScalar(l.retType)) or (not isScalar(r.retType)):
                            print("Error: Logical operators only apply to scalar expressions.")
                            sys.exit(1)

                        return parser.Binary_Expression(op, l, r, parser.IntType())
                    case parser.BinopType.OR:
                        if (not isScalar(l.retType)) or (not isScalar(r.retType)):
                            print("Error: Logical operators only apply to scalar expressions.")
                            sys.exit(1)

                        return parser.Binary_Expression(op, l, r, parser.IntType())
                
                commonType = None

                if type(l.retType) == parser.PointerType or type(r.retType) == parser.PointerType:
                    commonType = getCommonPointerType(l, r)
                elif isArithmeticType(l.retType) and isArithmeticType(r.retType):
                    commonType = getCommonType(l.retType, r.retType)
                else:
                    print("Error: Invalid Operands for expression {0}.".format(op.operator.name))
                    sys.exit(1)
                    
                l = convertTo(l, commonType)
                r = convertTo(r, commonType)

                match op.operator:
                    case parser.BinopType.ADD:
                        return parser.Binary_Expression(op, l, r, commonType)
                    case parser.BinopType.SUBTRACT:
                        return parser.Binary_Expression(op, l, r, commonType)
                    case parser.BinopType.MULTIPLY:
                        return parser.Binary_Expression(op, l, r, commonType)
                    case parser.BinopType.MODULO:
                        return parser.Binary_Expression(op, l, r, commonType)
                    case parser.BinopType.DIVIDE:
                        return parser.Binary_Expression(op, l, r, commonType)
                    case _:
                        return parser.Binary_Expression(op, l, r, parser.IntType())

            def matchRelationalOperator(op, l, r):
                if isArithmeticType(l.retType) and isArithmeticType(r.retType):
                    return typeCheckCommonArithmeticBinaryExp(op, l, r)
                
                elif type(l.retType) == parser.PointerType and l.retType.checkType(r.retType):
                    return parser.Binary_Expression(op, l, r, parser.IntType())
                else:
                    print("Error: Invalid operand types for comparison. {0} and {1}".format(l.retType, r.retType))
                    sys.exit(1)
                
            l = typeCheckAndConvert(left, symbolTable)
            r = typeCheckAndConvert(right, symbolTable)

            match op.operator:
                case parser.BinopType.ADD:
                    if isArithmeticType(l.retType) and isArithmeticType(r.retType):
                        return typeCheckCommonArithmeticBinaryExp(op, l, r)

                    elif isPointerToComplete(l.retType) and isIntegerType(r.retType):
                        convertedE2 = convertTo(r, parser.LongType())
                        return parser.Binary_Expression(op, l, convertedE2, l.retType)
                        
                    elif isIntegerType(l.retType) and isPointerToComplete(r.retType):
                        convertedE1 = convertTo(l, parser.LongType())
                        return parser.Binary_Expression(op, convertedE1, r, r.retType)
                    
                    else:
                        print("Error: Invalid operand types for addition.")
                        sys.exit(1)

                case parser.BinopType.SUBTRACT:
                    
                    if isArithmeticType(l.retType) and isArithmeticType(r.retType):
                        return typeCheckCommonArithmeticBinaryExp(op, l, r)

                    elif isPointerToComplete(l.retType) and isIntegerType(r.retType):
                        convertedE2 = convertTo(r, parser.LongType())
                        return parser.Binary_Expression(op, l, convertedE2, l.retType)
                        
                    elif isPointerToComplete(l.retType) and l.retType.checkType(r.retType):
                        return parser.Binary_Expression(op, l, r, parser.LongType())
                    
                    else:
                        print("Error: Invalid operand types for subtraction.")
                        sys.exit(1)

                case parser.BinopType.GREATERTHAN:
                    return matchRelationalOperator(op, l, r)
                    
                case parser.BinopType.GREATEROREQUAL:
                    return matchRelationalOperator(op, l, r)
                    
                case parser.BinopType.LESSTHAN:
                    return matchRelationalOperator(op, l, r)
                    
                case parser.BinopType.LESSOREQUAL:
                    return matchRelationalOperator(op, l, r)
                
                case _:                    
                    return typeCheckCommonArithmeticBinaryExp(op, l, r)
      
        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):

            condExp = typeCheckAndConvert(condExp, symbolTable)
            thenExp = typeCheckAndConvert(thenExp, symbolTable)
            elseExp = typeCheckAndConvert(elseExp, symbolTable)
            
            if not isScalar(condExp.retType):
                print("Error: Logical operators only apply to scalar expressions.")
                sys.exit(1)

            commonType = None

            if type(thenExp.retType) == parser.VoidType and type(elseExp.retType) == parser.VoidType:
                commonType = parser.VoidType()

            elif isArithmeticType(thenExp.retType) and isArithmeticType(elseExp.retType):
                commonType = getCommonType(thenExp.retType, elseExp.retType)

            elif type(thenExp.retType) == parser.PointerType or type(elseExp.retType) == parser.PointerType:
                commonType = getCommonPointerType(thenExp, elseExp)

            else:
                traceback.print_stack()
                print("Fail cannot convert branches of conditional to a common type. {0} and {1}".format(thenExp.retType, elseExp.retType))
                sys.exit(1)
                
            thenExp = convertTo(thenExp, commonType)
            elseExp = convertTo(elseExp, commonType)

            return parser.Conditional_Expression(condExp, thenExp, elseExp, commonType)


        case parser.SizeOfT(typeName = typeName):
            validateTypeSpecifier(typeName)
            if not isComplete(typeName):
                print("Error: Can't get the size of an incomplete type.")
                sys.exit(1)

            return parser.SizeOfT(typeName, parser.ULongType())
        
        case parser.SizeOf(exp = exp):
            e = typeCheckExpression(exp, symbolTable)
            if not isComplete(e.retType):
                print("Error: Can't get the size of an incomplete type.")
                sys.exit(1)

            return parser.SizeOf(e, parser.ULongType())

        case parser.Dot(struct = struct, member = member):
            pass     

        case parser.Arrow(pointer = pointer, member = member):
            pass   

        case _:
            traceback.print_stack()
            print("Invalid expression type. {0}".format(type(exp)))
            sys.exit(1)


def GetStaticInitializer(varType, int):
    match varType:
        case parser.IntType():
            return IntInit(int)

        case parser.LongType():
            return LongInit(int)
        
        case parser.UIntType():
            return UIntInit(int)

        case parser.ULongType():
            return ULongInit(int)

        case parser.DoubleType():
            return DoubleInit(int)

        case parser.PointerType():
            return ULongInit(int)
        
        case parser.CharType():
            return CharInit(int)

        case parser.SCharType():
            return CharInit(int)

        case parser.UCharType():
            return UCharInit(int)

        case _:
            print("Error: Invalid Variable Type. {0}".format(varType))
            sys.exit(1)

def CreateZeroInitializer(type_, initList):
    match type_:
        case parser.ArrayType(elementType = elementType, size = size):
            for i in range(size):    
                CreateZeroInitializer(elementType, initList)
            
        case _:
            initList.append(GetStaticInitializer(type_, 0))
            
def AnnotateInitializer(varDecl, type_, init, initList, symbolTable):

    def AnnotateSingleInit(exp, type_):
        match exp:
            case parser.Constant_Expression(const = const):
                match const:
                    case parser.ConstLong(int = int):
                        temp = parser.Constant_Expression(const, parser.LongType())
                        temp = convertByAssignment(temp, type_)
                        initList.append(GetStaticInitializer(type_, int))  
                        return parser.SingleInit(temp, type_)

                    case parser.ConstInt(int = int):
                        temp = parser.Constant_Expression(const, parser.IntType())
                        temp = convertByAssignment(temp, type_)
                        initList.append(GetStaticInitializer(type_, int))                            
                        return parser.SingleInit(temp, type_)

                    case parser.ConstULong(int = int):
                        temp = parser.Constant_Expression(const, parser.ULongType())
                        temp = convertByAssignment(temp, type_)
                        initList.append(GetStaticInitializer(type_, int))                            
                        return parser.SingleInit(temp, type_)
                        
                    case parser.ConstUInt(int = int):
                        temp = parser.Constant_Expression(const, parser.UIntType())
                        temp = convertByAssignment(temp, type_)
                        initList.append(GetStaticInitializer(type_, int))                            
                        return parser.SingleInit(temp, type_)
                    
                    case parser.ConstDouble(double=double):
                        temp = parser.Constant_Expression(const, parser.DoubleType())
                        temp = convertByAssignment(temp, type_)
                        initList.append(GetStaticInitializer(type_, double))                            
                        return parser.SingleInit(temp, type_)

                    case _:
                        print("Error: Invalid Constant. {0}".format(type(const)))
                        sys.exit(1)
                        
            case _:
                print("Error: Non constant expression.")
                sys.exit(1)

    match type_, init:
        case parser.ArrayType(elementType = elementType, size = size), parser.SingleInit(exp = exp, retType = retType):

            match exp:
                case parser.StringExpression(string = string):
                    if not isCharacterType(elementType):
                        print("Error: Cannot initialize a non character type with a string literal. {0}".format(elementType))
                        sys.exit(1)
                    
                    if len(string) > size:
                        print("Error: Too many characters in string literal.")
                        sys.exit(1)

                    nullT = True
                    occupiedB = len(string)

                    if occupiedB == size:
                        nullT = False
                    elif occupiedB < size:
                        nullT = True
                        occupiedB += 1

                    initList.append(StringInit(string, nullT))

                    if occupiedB < size: 
                        initList.append(ZeroInit(size - occupiedB))
                    
                    return parser.SingleInit(parser.StringExpression(string, type_), type_)
                    
                case _:
                    print("Error: Scalar Initializer for Array Type.")
                    sys.exit(1)
            
        case parser.PointerType(referenceType = referenceType), parser.SingleInit(exp = exp, retType = retType):

            match exp:
                case parser.StringExpression(string = string):
                    if type(referenceType) != parser.CharType:
                        print("Error: Cannot initialize a pointer to non char type.")
                        sys.exit(1)

                    tmp = makeTemporary("string")
                    print(tmp)

                    symbolTable[tmp] = Entry(tmp, ConstantAttr(StringInit(string, True)), parser.ArrayType(parser.CharType(), len(string) + 1))

                    initList.append(PointerInit(tmp))

                    return parser.SingleInit(parser.StringExpression(string, type_), type_)
                
                case _:
                    return AnnotateSingleInit(exp, type_)

        case _, parser.SingleInit(exp = exp, retType = retType):
            return AnnotateSingleInit(exp, type_)

        case parser.ArrayType(elementType = elementType, size = size), parser.CompoundInit(initializerList = initializerList, retType = retType):
            
            if len(initializerList) > size:
                print("Error: Wrong number of values of initializer.")
                sys.exit(1)

            astInitList = []
            index  = 0
            for astInit in initializerList:
                i = AnnotateInitializer(varDecl, elementType, astInit, initList, symbolTable)
                astInitList.append(i)
                index += 1

            size = type_.getBaseTypeSize(index)

            if index < type_.size:
                initList.append(ZeroInit(size))

            return parser.CompoundInit(astInitList, type_)


        case _:
            print("Error: Can't Initialize a scalar object with a compound initializer.")
            sys.exit(1)

def typeCheckFileScopeVarDecl(varDecl, symbolTable):

    if not isComplete(varDecl.varType):
        print("Error: Cannot declare variable with void Type.")
        sys.exit(1)

    validateTypeSpecifier(varDecl.varType)

    initialValue = None

    if varDecl.initializer:
        initList = []
        astInit = AnnotateInitializer(varDecl, varDecl.varType, varDecl.initializer, initList, symbolTable)

        varDecl.initializer = astInit
        initialValue = Initial(initList)

    else:
        if varDecl.storageClass.storageClass == parser.StorageType.EXTERN:
            initialValue = NoInitializer()
        else:
            initialValue = Tentative()


    global_ = True
    if varDecl.storageClass.storageClass == parser.StorageType.STATIC:
        global_ = False
    
    if varDecl.identifier in symbolTable:

        oldDecl = symbolTable[varDecl.identifier]    

        if type(oldDecl.type) == parser.FunType:
            print("Error: Function redeclared as variable.")
            sys.exit(1)
        
        #type(oldDecl.type) != type(varDecl.varType):
        if not oldDecl.type.checkType(varDecl.varType):
            print("Error: Incompatible variable declarations.")
            sys.exit(1)

        if varDecl.storageClass.storageClass == parser.StorageType.EXTERN:
            #print(type(oldDecl[1]))
            global_ = oldDecl.attrs.global_
        
        elif oldDecl.attrs.global_ != global_:
            print("Error: Conflicting Variable Linkage.")
            sys.exit(1)

        match oldDecl.attrs.initialVal:
            case Initial():
                match initialValue:
                    case Initial():
                        print("Error: Conflicting File Scope variable definitions.")
                        sys.exit(1)
                    case _:
                        initialValue = oldDecl.attrs.initialVal
            case Tentative():
                if type(initialValue) != Initial:
                    #print("Ale")
                    initialValue = Tentative()

    vattr = StaticAttributes(initialVal=initialValue, global_=global_)
    symbolTable[varDecl.identifier] = Entry(varDecl.identifier, vattr, varDecl.varType)

    return parser.VariableDecl(varDecl.identifier, varDecl.varType, varDecl.initializer, varDecl.storageClass)

#esta funcion es para locales
def zeroInitializer(elementType):
    match elementType:

        case parser.CharType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstChar(0), elementType), elementType)
        
        case parser.UCharType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstUChar(0), elementType), elementType)

        case parser.SCharType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstChar(0), elementType), elementType)
        
        case parser.IntType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstInt(0), elementType), elementType)
        
        case parser.LongType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstLong(0), elementType), elementType)

        case parser.UIntType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstUInt(0), elementType), elementType)
            
        case parser.ULongType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstULong(0), elementType), elementType)

        case parser.DoubleType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstDouble(0), elementType), elementType)
        
        case parser.PointerType():
            return parser.SingleInit(parser.Constant_Expression(parser.ConstULong(0), elementType), elementType)

        case parser.ArrayType(elementType = elementType_, size = size):
            initList = []
            for i in range(size):
                init = zeroInitializer(elementType_)
                initList.append(init)

            return parser.CompoundInit(initList, elementType)
            
        case _:
            print("Error: Cannot create zero initializer for type {0}".format(elementType))
            sys.exit(1)
    pass

def typeCheckInitializer(targetType, initializer, symbolTable):
    
    match targetType, initializer:
        
        case parser.ArrayType(elementType = elementType, size = size), parser.SingleInit(exp = exp):
            match exp:
                case parser.StringExpression(string = string):
                    if not isCharacterType(elementType):
                        print("Error: Cannot initialize a non character type with a string literal. {0}".format(elementType))
                        sys.exit(1)
                    
                    if len(string) > size:
                        print("Error: Too many characters in string literal.")
                        sys.exit(1)
                    
                    return parser.SingleInit(parser.StringExpression(string, targetType), targetType)

                case _:
                    print("Error: Scalar Initializer for Array Type.")
                    sys.exit(1)

                    #e = typeCheckAndConvert(exp, symbolTable)
                    #e = convertByAssignment(e, targetType)
                    #return parser.SingleInit(e, targetType)


        case _, parser.SingleInit(exp = exp):
            e = typeCheckAndConvert(exp, symbolTable)
            e = convertByAssignment(e, targetType)
            return parser.SingleInit(e, targetType)

        case parser.ArrayType(elementType = elementType, size = size), parser.CompoundInit(initializerList = initializerList):
            if len(initializerList) > size:
                print("Error: Wrong number of values of initializer.")
                sys.exit(1)

            typeCheckedList = []
            for i in initializerList:
                #aqui le faltan bytes en string literals
                init = typeCheckInitializer(elementType, i, symbolTable)
                typeCheckedList.append(init)

            while len(typeCheckedList) < size:
                typeCheckedList.append(zeroInitializer(elementType))

            return parser.CompoundInit(typeCheckedList, targetType)


        case _:
            print("Error: Can't Initialize a scalar object with a compound initializer.")
            sys.exit(1)

def typeCheckLocalVarDecl(varDecl, symbolTable):

    if not isComplete(varDecl.varType):
        print("Error: Cannot declare variable with void Type.")
        sys.exit(1)

    validateTypeSpecifier(varDecl.varType)

    if varDecl.storageClass.storageClass == parser.StorageType.EXTERN:
        if varDecl.initializer:
            print("Error: Initializer on local extern variable declaration.")
            sys.exit(1)
        
        if varDecl.identifier in symbolTable:
            oldDecl = symbolTable[varDecl.identifier]
            
            if type(oldDecl.type) == parser.FunType:
                print("Error: Function redeclared as variable.")
                sys.exit(1)

            if not oldDecl.type.checkType(varDecl.varType):
                print("Error: Incompatible local variable declarations.")
                sys.exit(1)
            
        else:
            symbolTable[varDecl.identifier] = Entry(varDecl.identifier, StaticAttributes(NoInitializer(), global_=True), varDecl.varType)

        return parser.VariableDecl(varDecl.identifier, varDecl.varType, varDecl.initializer, varDecl.storageClass)
    
    elif varDecl.storageClass.storageClass == parser.StorageType.STATIC:
        
        initialValue = None
        
        if varDecl.initializer:
            initList = []
            astInit = AnnotateInitializer(varDecl, varDecl.varType, varDecl.initializer, initList, symbolTable)
            varDecl.initializer = astInit
            initialValue = Initial(initList)
        else:
            initList = []
            CreateZeroInitializer(varDecl.varType, initList)
            initialValue = Initial(initList)
        
        symbolTable[varDecl.identifier] = Entry(varDecl.identifier, StaticAttributes(initialVal=initialValue, global_=False), varDecl.varType)

        return parser.VariableDecl(varDecl.identifier, varDecl.varType, varDecl.initializer, varDecl.storageClass)

            
    else:
        symbolTable[varDecl.identifier] = Entry(varDecl.identifier, LocalAttributes(), varDecl.varType)
        
        if varDecl.initializer:
            init = typeCheckInitializer(varDecl.varType, varDecl.initializer, symbolTable)

            return parser.VariableDecl(varDecl.identifier, varDecl.varType, init, varDecl.storageClass)
        
        return parser.VariableDecl(varDecl.identifier, varDecl.varType, None, varDecl.storageClass)

def typeCheckVarDeclaration(varDecl, symbolTable, isBlockScope):
    if isBlockScope:
        return typeCheckLocalVarDecl(varDecl, symbolTable)
    else:
        return typeCheckFileScopeVarDecl(varDecl, symbolTable)

class StructEntry():
    def __init__(self, alignment, size, members):
        self.alignment = alignment
        self.size = size
        self.members = members

class MemberEntry():
    def __init__(self, name, type_, offset):
        self.name = name
        self.memberType = type_
        self.offset = offset

def validateStructDefinition(structDecl, typeTable):
    if structDecl.tag in typeTable:
        print("Error: Struct {0} already defined.".format(structDecl.tag))
        sys.exit(1)

    memberTable = []
    for member in structDecl.members:
        if member.name in memberTable:
            print("Error: Duplicate member name {0} in struct {1}.".format(member.name, structDecl.tag))
            sys.exit(1)
        
        validateTypeSpecifier(member.memberType)

        if not isComplete(member.memberType):
            print("Error: Incomplete type {0} in struct {1}.".format(member.memberType, structDecl.tag))
            sys.exit(1)

        memberTable.append(member.name) 

        
    
    

def typeCheckStructDeclaration(structDecl, typeTable):

    if structDecl.members == []:
        return
    
    validateStructDefinition(structDecl, typeTable)

    memberEntries = []

    structSize = 0
    structAlignment = 1


    for member in structDecl.members:
        memberAlignment, other = assemblyGenerator.matchCType(member.memberType)
        #print("memberAlignment:",memberAlignment)

        memberOffset = structSize + (structSize % memberAlignment)
        print("memberOffset:",memberOffset)

        memberEntries.append(MemberEntry(member.name, member.memberType, memberOffset))

        structAlignment = max(structAlignment, memberAlignment)

        structSize = memberOffset + member.memberType.getBaseTypeSize(0)
        
        print("structSize:",structSize)


    print("structAlignment:",structAlignment)

    structSize = structSize + (structAlignment - (structSize % structAlignment))
    
    print("structSize:",structSize)

    typeTable[structDecl.tag] = StructEntry(structAlignment, structSize, memberEntries)

    
        
def typeCheckDeclaration(dec, symbolTable, typeTable, isBlockScope):
    match dec:
        case parser.VarDecl(variableDecl = variableDecl):
            variableDecl = typeCheckVarDeclaration(variableDecl, symbolTable, isBlockScope)
            return parser.VarDecl(variableDecl)
            
        case parser.FunDecl(funDecl = funDecl):
            funDecl = typeCheckFunctionDeclaration(funDecl, symbolTable)
            return parser.FunDecl(funDecl)
        
        case parser.StructDecl(structDecl = structDecl):
            typeCheckStructDeclaration(structDecl, typeTable)
            return parser.StructDecl(structDecl)
            

        case _:
            print("Error: Invalid Declaration {0}".format(dec))
            sys.exit(1)

def typeCheckForInit(forInit, symbolTable):
    match forInit:
        case parser.InitDecl(varDecl = varDecl):
            if varDecl.storageClass.storageClass != parser.StorageType.NULL:
                print("Error: Invalid Storage class specifier in variable declaration in for init.")
                sys.exit(1)

            varDecl = typeCheckVarDeclaration(varDecl, symbolTable, True)
            #este esta bien
            return parser.InitDecl(varDecl)
        
        case parser.InitExp(exp=exp):
            if exp:
                exp = typeCheckAndConvert(exp, symbolTable)
                #exp = typeCheckExpression(exp, symbolTable)
                return parser.InitExp(exp)
            
            return parser.InitExp()

def isScalar(t):
    match t:
        case parser.VoidType():
            return False
        case parser.FunType():
            return False
        case parser.ArrayType():
            return False
        case _:
            return True

def typeCheckStatement(statement, symbolTable, functionParentName):
    match statement:
        case parser.BreakStatement():
            return parser.BreakStatement()

        case parser.ContinueStatement():
            return parser.ContinueStatement()

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement):
            f = typeCheckForInit(forInit, symbolTable)
            
            c = None
            if condExp:
                c = typeCheckAndConvert(condExp, symbolTable)

                if not isScalar(c.retType):
                    print("Error: Logical operators only apply to scalar expressions.")
                    sys.exit(1)

            p = None
            if postExp:
                p = typeCheckAndConvert(postExp, symbolTable)

            s = typeCheckStatement(statement, symbolTable, functionParentName)

            return parser.ForStatement(f, s, c, p)
        
        case parser.DoWhileStatement(statement=statement, condExp=condExp):
            statement = typeCheckStatement(statement, symbolTable, functionParentName)

            condExp = typeCheckAndConvert(condExp, symbolTable)
            
            if not isScalar(condExp.retType):
                print("Error: Logical operators only apply to scalar expressions.")
                sys.exit(1)

            return parser.DoWhileStatement(statement, condExp)

        case parser.WhileStatement(condExp=condExp, statement=statement):

            condExp = typeCheckAndConvert(condExp, symbolTable)

            if not isScalar(condExp.retType):
                print("Error: Logical operators only apply to scalar expressions.")
                sys.exit(1)

            statement = typeCheckStatement(statement, symbolTable, functionParentName)

            return parser.WhileStatement(condExp, statement)

        case parser.ExpressionStmt(exp=exp):
            e = typeCheckAndConvert(exp, symbolTable)
            #e = typeCheckExpression(exp, symbolTable)

            return parser.ExpressionStmt(e)

        case parser.ReturnStmt(expression=exp):
            funRetType = symbolTable[functionParentName].type.retType
            
            if exp:
                if type(funRetType) == parser.VoidType:
                    print("Error: Function with void return type cannot have return expression.")
                    sys.exit(1)

                e = typeCheckAndConvert(exp, symbolTable)
                e = convertByAssignment(e, funRetType)
                return parser.ReturnStmt(e)
            
            if type(funRetType) != parser.VoidType:
                print("Error: Function must return a value.")
                sys.exit(1)

            return parser.ReturnStmt()
            
        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            exp = typeCheckAndConvert(exp, symbolTable)

            if not isScalar(exp.retType):
                print("Error: Logical operators only apply to scalar expressions.")
                sys.exit(1)

            thenS = typeCheckStatement(thenS, symbolTable, functionParentName)

            if elseS:
                elseS = typeCheckStatement(elseS, symbolTable, functionParentName)
                return parser.IfStatement(exp, thenS, elseS)

            return parser.IfStatement(exp, thenS)
            
        case parser.CompoundStatement(block=block):
            block = typeCheckBlock(block, symbolTable, functionParentName)
            return parser.CompoundStatement(block)

        case parser.NullStatement():
            return parser.NullStatement()
        
        case _:
            print("Error: Invalid Statement {0}".format(statement))
            sys.exit(1)


def typeCheckBlock(block, symbolTable, functionParentName):
    
    if block.blockItemList:
        
        blockItemList = []

        for item in block.blockItemList:
            match item:
                case parser.D(declaration=dec):
                    dec = typeCheckDeclaration(dec, symbolTable, True)
                    blockItemList.append(parser.D(dec))
                    
                case parser.S(statement=statement):
                    statement = typeCheckStatement(statement, symbolTable, functionParentName)
                    blockItemList.append(parser.S(statement)) 
                
        return parser.Block(blockItemList)
    
    return parser.Block()      
        
def typeCheckFunctionDeclaration(funDec, symbolTable):
    
    validateTypeSpecifier(funDec.funType)

    if type(funDec.funType.retType) == parser.ArrayType:
        print("Error: A function cannot return an array.")
        sys.exit(1)

    adjustedParamTypes = []
    for paramType in funDec.funType.paramTypes:
        
        if not isComplete(paramType):
            print("Error: Cannot declare variable with void Type.")
            sys.exit(1)

        match paramType:
            case parser.ArrayType(elementType = elementType, size = size):
                adjT = parser.PointerType(referenceType= elementType)
                adjustedParamTypes.append(adjT)

            case _:
                adjustedParamTypes.append(paramType)

    funDec.funType.paramTypes = adjustedParamTypes

    funType = funDec.funType
    hasBody = funDec.block != None
    alreadyDefined = False
    global_ = True
    
    if funDec.storageClass.storageClass == parser.StorageType.STATIC:
        global_ = False
    

    if funDec.iden in symbolTable:
        oldDecl = symbolTable[funDec.iden]

        if type(oldDecl.type) != parser.FunType:
            print("Error: Variable redeclared as function.")
            sys.exit(1)

        if len(oldDecl.type.paramTypes) != len(funType.paramTypes):
            print("Error: Incompatible arity in function declarations.")
            sys.exit(1)
        
        if not oldDecl.type.retType.checkType(funType.retType):
            print("Error: Incompatible return type in function declarations.")
            sys.exit(1)

        for old, new in zip(oldDecl.type.paramTypes, funType.paramTypes):
            print("Old: ", old, "New:", new)
            if not old.checkType(new):
                print("Error: Incompatible parameter types in function declarations.")
                sys.exit(1)

        alreadyDefined = oldDecl.attrs.defined

        if alreadyDefined and hasBody:
            print("Error: function is defined more than once.")
            sys.exit(1)

        if oldDecl.attrs.global_ and funDec.storageClass.storageClass == parser.StorageType.STATIC:
            print("Static function declaration follows non-static.")
            sys.exit(1)

        global_ = oldDecl.attrs.global_

    fattr = FunAttributes(defined=(alreadyDefined or hasBody), global_=global_)

    symbolTable[funDec.iden] = Entry(funDec.iden, fattr, funType)

    if hasBody:
        for paramName, paramType in zip(funDec.paramNames, funType.paramTypes):
            symbolTable[paramName] = Entry(paramName, LocalAttributes(), paramType)
        
        block = typeCheckBlock(funDec.block, symbolTable, funDec.iden)

        return parser.FunctionDecl(funDec.iden, funType, funDec.paramNames, block, funDec.storageClass)
    
    return parser.FunctionDecl(funDec.iden, funType, funDec.paramNames, None, funDec.storageClass)
    

def typeCheckProgram(pro):
    symbolTable = {}
    typeTable = {}

    if pro.declList:
        declList = []
        for decl in pro.declList:
            d = typeCheckDeclaration(decl, symbolTable, typeTable, False)
            declList.append(d)

        return parser.Program(declList), symbolTable
    
    return parser.Program(), symbolTable
    
