import sys
from enum import Enum
import parser
import semanticAnalysis
import typeChecker

from typeChecker import isIntegerType

class TAC_Program:
    def __init__(self, topLevelList):
        self.topLevelList = topLevelList
    
    def __str__(self):
        return "TAC Program:{self.topLevelList}".format(self=self)

class TopLevel:
    pass

class StaticConstant(TopLevel):
    def __init__(self, identifier, type, staticInit):
        self.identifier = identifier
        self.type = type
        self.staticInit = staticInit

    def __str__(self):
        return "{self.type} - {self.identifier} = {self.staticInit}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class StaticVariable(TopLevel):
    def __init__(self, identifier, global_, type, initList):
        self.identifier = identifier
        self.global_ = global_
        self.type = type
        self.initList = initList
    
    def __str__(self):
        return "Global: {self.global_} {self.identifier} = {self.initList}".format(self=self)

    def __repr__(self):
        return self.__str__()

class TAC_FunctionDef(TopLevel):
    def __init__(self, identifier, global_, params, instructions):
        self.identifier = identifier
        self.global_ = global_
        self.params = params
        self.instructions = instructions

    def __str__(self):
        return "Function: {self.identifier} ({self.params}) instructions:{self.instructions}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class instruction:
    pass

class TAC_addPtr(instruction):
    def __init__(self, ptr, index, scale, dst):
        self.ptr = ptr
        self.index = index
        self.scale = scale
        self.dst = dst

    def __str__(self):
        return "AddPtr {self.dst} = {self.ptr} + {self.index} * {self.scale}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_copyFromOffset(instruction):
    def __init__(self, src, offset, dst):
        self.src = src
        self.offset = offset
        self.dst = dst

    def __str__(self):
        return "CopyFromOffset {self.dst} = ({self.src} + {self.offset})".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    

class TAC_copyToOffset(instruction):
    def __init__(self, src, dst, offset):
        self.src = src
        self.dst = dst
        self.offset = offset

    def __str__(self):
        return "CopyToOffset({self.dst} + {self.offset}) = {self.src} ".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_returnInstruction(instruction):
    def __init__(self, Value = None):
        self.Value = Value
    
    def __str__(self):
        return "Return {self.Value}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_signExtendInstruction(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __str__(self):
        return "SignExtend {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class TAC_zeroExtendInstruction(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "ZeroExtend {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_DoubleToInt(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "DoubleToInt {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_DoubleToUInt(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "DoubleToUInt {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_IntToDouble(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "IntToDouble {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_UIntToDouble(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "UIntToDouble {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()


class TAC_truncateInstruction(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __str__(self):
        return "Truncate {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()


class TAC_UnaryInstruction(instruction):
    def __init__(self, operator, src, dst):
        self.operator = operator
        self.src = src 
        self.dst = dst   
    
    def __str__(self):
        return "{self.dst} = {self.operator}{self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_CopyInstruction(instruction):
    def __init__(self, src, dst):
        self.src = src 
        self.dst = dst   
    
    def __str__(self):
        return "Copy {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_GetAddress(instruction):
    def __init__(self, src, dst):
        self.src = src 
        self.dst = dst

    def __str__(self):
        return "{self.dst} = Get Address {self.src} ".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class TAC_Load(instruction):
    def __init__(self, src, dst):
        self.src = src 
        self.dst = dst

    def __str__(self):
        return "{self.dst} = Load {self.src} ".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_Store(instruction):
    def __init__(self, src, dst):
        self.src = src 
        self.dst = dst
    
    def __str__(self):
        return "{self.dst} = Store {self.src} ".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_JumpIfZeroInst(instruction):
    def __init__(self, condition, label):
        self.condition = condition
        self.label = label
    
    def __str__(self):
        return "JumpIfZero({self.condition}, {self.label})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_JumpIfNotZeroInst(instruction):
    def __init__(self, condition, label):
        self.condition = condition
        self.label = label
    
    def __str__(self):
        return "JumpIfNotZero({self.condition}, {self.label})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_JumpInst(instruction):
    def __init__(self, label):
        self.label = label
    
    def __str__(self):
        return "Jump({self.label})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_LabelInst(instruction):
    def __init__(self, identifier):
        self.identifier = identifier
    
    def __str__(self):
        return "Label({self.identifier})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_BinaryInstruction:
    def __init__(self, operator, src1, src2, dst):
        self.operator = operator
        self.src1 = src1 
        self.src2 = src2
        self.dst = dst   
    
    def __str__(self):
        return "{self.dst} = {self.src1} {self.operator} {self.src2}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_FunCallInstruction:
    def __init__(self, funName, arguments, dst = None):
        self.funName = funName
        self.arguments = arguments
        self.dst = dst
    
    def __str__(self):
        return "{self.dst} = {self.funName}({self.arguments})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class Value:
    pass

class TAC_ConstantValue(Value):
    def __init__(self, const):
        self.const = const
    
    def __str__(self):
        return "{self.const}".format(self=self)

    def __repr__(self):
        return self.__str__()

class TAC_VariableValue(Value):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "{self.identifier}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class UnopType(Enum):
    NEGATE = 1
    COMPLEMENT = 2
    NOT = 3

class BinopType(Enum):
    EQUAL = 0
    NOTEQUAL = 1
    GREATERTHAN = 2
    GREATEROREQUAL = 3
    LESSTHAN = 4
    LESSOREQUAL = 5
    #NOTE this are not serialized
    ADD = 6
    SUBTRACT = 7
    MULTIPLY = 8
    DIVIDE = 9
    REMAINDER = 10

class Operator:
    pass

class TAC_UnaryOperator(Operator):
    def __init__(self, operator):
        self.operator = operator
    
    def __str__(self):
        match self.operator:
            case UnopType.NEGATE:
                return "-"
            case UnopType.COMPLEMENT:
                return "~"
            case _:
                return "_"

class TAC_BinaryOperator(Operator):
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        match self.operator:
            case BinopType.ADD:
                return "+"
            case BinopType.SUBTRACT:
                return "-"
            case BinopType.DIVIDE:
                return "/"
            case BinopType.MULTIPLY:
                return "*"
            case BinopType.REMAINDER:
                return "%"
            case _:
                return "_"


class ExpResult:
    pass

class PlainOperand(ExpResult):
    def __init__(self, val):
        self.val = val
    

class DereferencedPointer(ExpResult):
    def __init__(self, val):
        self.val = val

class SubObject(ExpResult):
    def __init__(self, base, offset):
        self.base = base
        self.offset = offset


    
def makeTemp():
    name = "tmp.{0}".format(semanticAnalysis.global_value) 
    semanticAnalysis.global_value += 1
    return name
    
def parseOperator(op):
    match op:
        case parser.UnaryOperator(operator=o):
            match o:
                case parser.UnopType.NEGATE:
                    return TAC_UnaryOperator(UnopType.NEGATE)
                case parser.UnopType.COMPLEMENT:
                    return TAC_UnaryOperator(UnopType.COMPLEMENT)
                case parser.UnopType.NOT:
                    return TAC_UnaryOperator(UnopType.NOT)
                
                case _:
                    print("Invalid Parser operator.")
                    sys.exit(1)

        case parser.BinaryOperator(operator=o):
            match o:
                case parser.BinopType.SUBTRACT:
                    return TAC_BinaryOperator(BinopType.SUBTRACT)
                    
                case parser.BinopType.ADD:
                    return TAC_BinaryOperator(BinopType.ADD)
                    
                case parser.BinopType.MULTIPLY:
                    return TAC_BinaryOperator(BinopType.MULTIPLY)
                    
                case parser.BinopType.DIVIDE:
                    return TAC_BinaryOperator(BinopType.DIVIDE)
                    
                case parser.BinopType.MODULO:
                    return TAC_BinaryOperator(BinopType.REMAINDER)
                
                case parser.BinopType.EQUAL:
                    return TAC_BinaryOperator(BinopType.EQUAL)
                
                case parser.BinopType.NOTEQUAL:
                    return TAC_BinaryOperator(BinopType.NOTEQUAL)

                case parser.BinopType.LESSTHAN:
                    return TAC_BinaryOperator(BinopType.LESSTHAN)
                
                case parser.BinopType.LESSOREQUAL:
                    return TAC_BinaryOperator(BinopType.LESSOREQUAL)
                
                case parser.BinopType.GREATERTHAN:
                    return TAC_BinaryOperator(BinopType.GREATERTHAN)

                case parser.BinopType.GREATEROREQUAL:
                    return TAC_BinaryOperator(BinopType.GREATEROREQUAL)
                
                case _:
                    print("Invalid Parser operator.")
                    sys.exit(1)

def makeTempVariable(type, symbolTable):
    dstName = makeTemp()
    symbolTable[dstName] = typeChecker.Entry(dstName, typeChecker.LocalAttributes(), type)
    return TAC_VariableValue(dstName)

"""
def makeStaticConstant(type, symbolTable):
    dstName = makeTemp()
    symbolTable[dstName] = typeChecker.Entry(dstName, typeChecker.StaticAttributes(None, None), type)
    return dstName
"""

def CastBetweenIntegers(targetType, sourceType, result, dst, instructions):

    if type(targetType) == parser.PointerType:
        targetType = parser.ULongType()
    elif type(sourceType) == parser.PointerType:
        sourceType = parser.ULongType()

    if targetType.size == sourceType.size:
        instructions.append(TAC_CopyInstruction(result, dst))
    elif targetType.size < sourceType.size:
        instructions.append(TAC_truncateInstruction(result, dst))
    elif sourceType.isSigned:
        instructions.append(TAC_signExtendInstruction(result, dst))
    else:
        instructions.append(TAC_zeroExtendInstruction(result, dst))

def TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable):
    result = TAC_parseInstructions(exp, instructions, symbolTable, typeTable)

    match result:
        
        case SubObject(base = base, offset = offset):
            dst = makeTempVariable(exp.retType, symbolTable)
            instructions.append(TAC_copyFromOffset(base, offset, dst))
            return dst
            
        case PlainOperand(val=val):
            return val
            
        case DereferencedPointer(val=ptr):
            tmp = makeTempVariable(exp.retType, symbolTable)
            instructions.append(TAC_Load(ptr, tmp))
            return tmp
        
        case _:
            print("Error: Invalid Lvalue conversion.")
            sys.exit(1)

memberOffset = 0

def TAC_parseInstructions(expression, instructions, symbolTable, typeTable):
    
    match expression:
        
        case parser.Subscript(ptrExp = e1, indexExp = e2, retType = retType):

            if type(e1.retType) == parser.PointerType and isIntegerType(e2.retType):

                src1 = TAC_emitTackyAndConvert(e1, instructions, symbolTable, typeTable)

                ptr = makeTempVariable(e1.retType, symbolTable)

                instructions.append(TAC_CopyInstruction(src1, ptr))

                src2 = TAC_emitTackyAndConvert(e2, instructions, symbolTable, typeTable)

                inte = makeTempVariable(e2.retType, symbolTable)

                instructions.append(TAC_CopyInstruction(src2, inte))
                
                dst = makeTempVariable(parser.ULongType(), symbolTable)

                scale = e1.retType.referenceType.getBaseTypeSize(0, typeTable)
                
                instructions.append(TAC_addPtr(ptr, inte, scale, dst))

                return DereferencedPointer(dst)

            elif isIntegerType(e1.retType) and type(e2.retType) == parser.PointerType:

                src1 = TAC_emitTackyAndConvert(e2, instructions, symbolTable, typeTable)

                ptr = makeTempVariable(e2.retType, symbolTable)

                instructions.append(TAC_CopyInstruction(src1, ptr))

                src2 = TAC_emitTackyAndConvert(e1, instructions, symbolTable, typeTable)

                inte = makeTempVariable(e1.retType, symbolTable)

                instructions.append(TAC_CopyInstruction(src2, inte))
                
                dst = makeTempVariable(parser.ULongType(), symbolTable)

                scale = e2.retType.referenceType.getBaseTypeSize(0, typeTable)
                
                instructions.append(TAC_addPtr(ptr, inte, scale, dst))

                return DereferencedPointer(dst)
                
        case parser.Constant_Expression(const = const):
            return PlainOperand(TAC_ConstantValue(const))
        
        case parser.SizeOf(exp = exp, retType = retType):
            type_ = exp.retType
            size = type_.getBaseTypeSize(0, typeTable)
            return PlainOperand(TAC_ConstantValue(parser.ConstULong(size)))
            
        case parser.SizeOfT(typeName = typeName, retType = retType):
            size = typeName.getBaseTypeSize(0, typeTable)
            return PlainOperand(TAC_ConstantValue(parser.ConstULong(size)))

        case parser.Cast_Expression(targetType = targetType, exp = exp):

            result = TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
            
            #== targetType.checkType(exp.retType):
            if type(targetType) == type(exp.retType):
                return PlainOperand(result)
            
            if type(targetType) == parser.VoidType:
                return PlainOperand(TAC_VariableValue("Dummy"))
            
            dst = makeTempVariable(targetType, symbolTable)
            
            match exp.retType:
                case parser.DoubleType():
                    match targetType:
                        case parser.IntType():
                            instructions.append(TAC_DoubleToInt(result, dst))

                        case parser.SCharType():
                            instructions.append(TAC_DoubleToInt(result, dst))

                        case parser.CharType():
                            instructions.append(TAC_DoubleToInt(result, dst))
                            
                        case parser.UCharType():
                            instructions.append(TAC_DoubleToUInt(result, dst))

                        case parser.LongType():
                            instructions.append(TAC_DoubleToInt(result, dst))

                        case parser.UIntType():
                            instructions.append(TAC_DoubleToUInt(result, dst))

                        case parser.ULongType():
                            instructions.append(TAC_DoubleToUInt(result, dst))
                        
                        case parser.PointerType():
                            pass

                        
                    
                case parser.IntType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_IntToDouble(result, dst))

                        case parser.VoidType():
                            pass
                        
                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)
                            
                case parser.LongType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_IntToDouble(result, dst))

                        case parser.VoidType():
                            pass  

                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)
                            
                case parser.UIntType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_UIntToDouble(result, dst))
                        
                        case parser.VoidType():
                            pass

                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)

                case parser.SCharType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_IntToDouble(result, dst))

                        case parser.VoidType():
                            pass

                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)


                case parser.CharType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_IntToDouble(result, dst))

                        case parser.VoidType():
                            pass
                            
                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)

                case parser.UCharType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_UIntToDouble(result, dst))

                        case parser.VoidType():
                            pass
                            
                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)
                
                case parser.ULongType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_UIntToDouble(result, dst))

                        case parser.VoidType():
                            pass
                        
                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)

                case parser.PointerType():
                    match targetType:
                        case parser.DoubleType():
                            print("Cannot cast pointer to double.")
                            sys.exit(1)

                        case parser.VoidType():
                            pass

                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)
                
                

                case _:
                    print("Invalid Cast Type. {0}".format(type(exp.retType)))
                    sys.exit(1)
                            
            return PlainOperand(dst)

        case parser.Dot(struct = struct, member = member, retType = retType):
            structDef = typeTable[struct.retType.tag]
            memberOffset = structDef.members[member].offset
            innerObject = TAC_parseInstructions(struct, instructions, symbolTable, typeTable)

            match innerObject:
                case PlainOperand(val = val):
                    return SubObject(val.identifier, memberOffset)
                    pass

                case SubObject(base = base, offset = offset):
                    return SubObject(base, offset + memberOffset)
                    pass

                case DereferencedPointer(val = ptr):
                    dstPtr = makeTempVariable(parser.PointerType(retType), symbolTable)

                    instructions.append(TAC_addPtr(ptr, TAC_ConstantValue(parser.ConstLong(memberOffset)), 1, dstPtr))

                    return DereferencedPointer(dstPtr)
                    
                

        case parser.Arrow(pointer = pointer, member = member, retType = retType):
            #retype no es un puntero
            match pointer.retType:
                case parser.PointerType(referenceType = referenceType):
                    structDef = typeTable[referenceType.tag]
                    memberOffset = structDef.members[member].offset
                    
                    dstPtr = makeTempVariable(parser.PointerType(retType), symbolTable)

                    ptr = TAC_emitTackyAndConvert(pointer, instructions, symbolTable, typeTable)
            
                    instructions.append(TAC_addPtr(ptr, TAC_ConstantValue(parser.ConstLong(memberOffset)), 1, dstPtr))

                    return DereferencedPointer(dstPtr)

                case _:
                    print("Error: Must be a pointer.")
                    sys.exit(1)


        case parser.Unary_Expression(operator=op, expression=inner):

            #src = TAC_parseInstructions(inner, instructions, symbolTable)
            src = TAC_emitTackyAndConvert(inner, instructions, symbolTable, typeTable)

            dst = makeTempVariable(expression.retType, symbolTable)

            operator = parseOperator(op)
            instructions.append(TAC_UnaryInstruction(operator, src, dst))

            return PlainOperand(dst)
        
        case parser.Binary_Expression(operator=op, left=left, right=right):

            def binaryCommonTacky():
                src1 = TAC_emitTackyAndConvert(left, instructions, symbolTable, typeTable)

                src2 = TAC_emitTackyAndConvert(right, instructions, symbolTable, typeTable)

                dst = makeTempVariable(expression.retType, symbolTable)                            

                operator = parseOperator(op)
                instructions.append(TAC_BinaryInstruction(operator, src1, src2, dst))

                return PlainOperand(dst)

            match op:
                case parser.BinaryOperator(operator=o):
                    
                    match o:
                        case parser.BinopType.AND:
                            
                            v1 = TAC_emitTackyAndConvert(left, instructions, symbolTable, typeTable)
                            
                            false_label = makeTemp()

                            instructions.append(TAC_JumpIfZeroInst(v1, false_label))

                            v2 = TAC_emitTackyAndConvert(right, instructions, symbolTable, typeTable)
                            
                            instructions.append(TAC_JumpIfZeroInst(v2, false_label))

                            result = makeTempVariable(expression.retType, symbolTable)

                            end = makeTemp()

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(1)), result))

                            instructions.append(TAC_JumpInst(end))

                            instructions.append(TAC_LabelInst(false_label))

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(0)), result))

                            instructions.append(TAC_LabelInst(end))

                            return PlainOperand(result)

                        case parser.BinopType.OR:
                            
                            v1 = TAC_emitTackyAndConvert(left, instructions, symbolTable, typeTable)
                            #v1 = TAC_parseInstructions(left, instructions, symbolTable)
                            
                            true_label = makeTemp()

                            instructions.append(TAC_JumpIfNotZeroInst(v1, true_label))

                            v2 = TAC_emitTackyAndConvert(right, instructions, symbolTable, typeTable)
                            #v2 = TAC_parseInstructions(right, instructions, symbolTable)

                            instructions.append(TAC_JumpIfNotZeroInst(v2, true_label))

                            result = makeTempVariable(expression.retType, symbolTable)
                            
                            end = makeTemp()

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(0)), result))

                            instructions.append(TAC_JumpInst(end))

                            instructions.append(TAC_LabelInst(true_label))

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(1)), result))

                            instructions.append(TAC_LabelInst(end))

                            return PlainOperand(result)

                        case parser.BinopType.SUBTRACT:

                            if type(left.retType) == parser.PointerType and isIntegerType(right.retType):

                                src1 = TAC_emitTackyAndConvert(left, instructions, symbolTable, typeTable)

                                ptr = makeTempVariable(left.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src1, ptr))

                                src2 = TAC_emitTackyAndConvert(right, instructions, symbolTable, typeTable)

                                inte = makeTempVariable(right.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src2, inte))

                                negate = makeTempVariable(left.retType, symbolTable)

                                instructions.append(TAC_UnaryInstruction(TAC_UnaryOperator(UnopType.NEGATE), inte, negate))
                                
                                dst = makeTempVariable(parser.ULongType(), symbolTable)

                                scale = left.retType.referenceType.getBaseTypeSize(0, typeTable)
                                
                                instructions.append(TAC_addPtr(ptr, negate, scale, dst))

                                return PlainOperand(dst)
                                
                            elif type(left.retType) == parser.PointerType and left.retType.checkType(right.retType):

                                #pointer diff

                                src1 = TAC_emitTackyAndConvert(left, instructions, symbolTable, typeTable)

                                ptr1 = makeTempVariable(left.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src1, ptr1))

                                src2 = TAC_emitTackyAndConvert(right, instructions, symbolTable, typeTable)

                                ptr2 = makeTempVariable(right.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src2, ptr2))

                                diff = makeTempVariable(parser.LongType(), symbolTable)

                                instructions.append(TAC_BinaryInstruction(TAC_BinaryOperator(BinopType.SUBTRACT), ptr1, ptr2, diff))

                                dst = makeTempVariable(parser.LongType(), symbolTable)

                                typeSize = left.retType.referenceType.getBaseTypeSize(0, typeTable)

                                instructions.append(TAC_BinaryInstruction(TAC_BinaryOperator(BinopType.DIVIDE), diff, TAC_ConstantValue(parser.ConstLong(typeSize)), dst))

                                return PlainOperand(dst)

                            else:
                                return binaryCommonTacky()
                            
                        case parser.BinopType.ADD:
                            #slo puede pointer y aritmetic
                            #pointer aritmetic
                            if type(left.retType) == parser.PointerType and isIntegerType(right.retType):

                                src1 = TAC_emitTackyAndConvert(left, instructions, symbolTable, typeTable)

                                ptr = makeTempVariable(left.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src1, ptr))

                                src2 = TAC_emitTackyAndConvert(right, instructions, symbolTable, typeTable)

                                inte = makeTempVariable(right.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src2, inte))
                                
                                dst = makeTempVariable(parser.ULongType(), symbolTable)

                                scale = left.retType.referenceType.getBaseTypeSize(0, typeTable)
                                
                                instructions.append(TAC_addPtr(ptr, inte, scale, dst))

                                return PlainOperand(dst)

                            elif isIntegerType(left.retType) and type(right.retType) == parser.PointerType:

                                src1 = TAC_emitTackyAndConvert(right, instructions, symbolTable, typeTable)

                                ptr = makeTempVariable(right.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src1, ptr))

                                src2 = TAC_emitTackyAndConvert(left, instructions, symbolTable, typeTable)

                                inte = makeTempVariable(left.retType, symbolTable)

                                instructions.append(TAC_CopyInstruction(src2, inte))
                                
                                dst = makeTempVariable(parser.ULongType(), symbolTable)

                                scale = right.retType.referenceType.getBaseTypeSize(0, typeTable)
                                
                                instructions.append(TAC_addPtr(ptr, inte, scale, dst))

                                return PlainOperand(dst)
                                
                            else:
                                return binaryCommonTacky()
                        
                        case _:
                            return binaryCommonTacky()
                            

                case parser.UnaryOperator():
                    print("Invalid operator.")
                    sys.exit(1)
                     
        case parser.Var_Expression(identifier=id):
            return PlainOperand(TAC_VariableValue(id))
            
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):

            lval = TAC_parseInstructions(lvalue, instructions, symbolTable, typeTable)
            rval = TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
            
            match lval:

                case SubObject(base = base, offset = offset):
                    instructions.append(TAC_copyToOffset(rval, base, offset))
                    return PlainOperand(rval)

                case PlainOperand(val=obj):
                    instructions.append(TAC_CopyInstruction(rval, obj))
                    return lval
                
                case DereferencedPointer(val=ptr):
                    instructions.append(TAC_Store(rval, ptr))
                    return PlainOperand(rval)
                
                case _:
                    print("Error: Invalid Exp Result.")
                    sys.exit(1)

        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            a = []

            if argumentList:
                for exp in argumentList:
                    src = TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
                    
                    dst = makeTempVariable(exp.retType, symbolTable)
                                
                    instructions.append(TAC_CopyInstruction(src, dst))
                    a.append(dst)
                    
                    #if type(exp.retType) == parser.VoidType:
                    #    pass
                    #else:
                    #    dst = makeTempVariable(exp.retType, symbolTable)
                                
                    #    instructions.append(TAC_CopyInstruction(src, dst))
                    #    a.append(dst)
            

            if type(expression.retType) == parser.VoidType:
                instructions.append(TAC_FunCallInstruction(id, a))    
                return PlainOperand(TAC_VariableValue("Dummy"))
                
            else:
                dst = makeTempVariable(expression.retType, symbolTable)
                instructions.append(TAC_FunCallInstruction(id, a, dst))    
                return PlainOperand(dst)
                

        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            cond = TAC_emitTackyAndConvert(condExp, instructions, symbolTable, typeTable)

            c = makeTempVariable(condExp.retType, symbolTable)
            
            instructions.append(TAC_CopyInstruction(cond, c))

            e2_label = makeTemp()
            instructions.append(TAC_JumpIfZeroInst(c, e2_label))

            if type(expression.retType) == parser.VoidType:

                TAC_emitTackyAndConvert(thenExp, instructions, symbolTable, typeTable)

                end = makeTemp()
                instructions.append(TAC_JumpInst(end))

                instructions.append(TAC_LabelInst(e2_label))

                TAC_emitTackyAndConvert(elseExp, instructions, symbolTable, typeTable)

                instructions.append(TAC_LabelInst(end))

                return PlainOperand(TAC_VariableValue("Dummy"))
            
            else:

                thenE = TAC_emitTackyAndConvert(thenExp, instructions, symbolTable, typeTable)

                v1 = makeTempVariable(thenExp.retType, symbolTable)
                
                instructions.append(TAC_CopyInstruction(thenE, v1))

                result = makeTempVariable(expression.retType, symbolTable)
                
                instructions.append(TAC_CopyInstruction(v1, result))

                end = makeTemp()
                instructions.append(TAC_JumpInst(end))

                instructions.append(TAC_LabelInst(e2_label))

                elseE = TAC_emitTackyAndConvert(elseExp, instructions, symbolTable, typeTable)
                
                v2 = makeTempVariable(elseExp.retType, symbolTable)
                
                instructions.append(TAC_CopyInstruction(elseE, v2))

                instructions.append(TAC_CopyInstruction(v2, result))

                instructions.append(TAC_LabelInst(end))

                return PlainOperand(result)
        
        case parser.AddrOf(exp = exp, retType = retType):
                
            v = TAC_parseInstructions(exp, instructions, symbolTable, typeTable)

            match v:
                case SubObject(base = base, offset = offset):
                    dst = makeTempVariable(retType, symbolTable)
                    instructions.append(TAC_GetAddress(TAC_VariableValue(base), dst))
                    instructions.append(TAC_addPtr(dst, TAC_ConstantValue(parser.ConstLong(offset)), 1, dst))
                    return PlainOperand(dst)
                    

                case PlainOperand(val=obj):
                    dst = makeTempVariable(retType, symbolTable)
                    instructions.append(TAC_GetAddress(obj, dst))
                    return PlainOperand(dst)
                
                case DereferencedPointer(val=ptr):
                    return PlainOperand(ptr)
                    
        case parser.Dereference(exp=exp):
            dst = TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
            return DereferencedPointer(dst)

        case parser.StringExpression(string = string, retType = retType):
            tmp = makeTemp()
            symbolTable[tmp] = typeChecker.Entry(tmp, typeChecker.ConstantAttr(typeChecker.StringInit(string, True)), parser.ArrayType(parser.CharType(), len(string) + 1))
            return PlainOperand(TAC_VariableValue(tmp))

        

        case _:
            print("Invalid Expression. {0}".format(type(expression)))
            sys.exit(1)           
    
def TAC_parseForInit(forInit, instructions, symbolTable, typeTable):
    match forInit:
        case parser.InitExp(exp=exp):
            if exp:
                TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
                #TAC_parseInstructions(exp, instructions, symbolTable)
            
        case parser.InitDecl(varDecl=varDecl):
            TAC_parseVarDeclarations(varDecl, instructions, symbolTable, typeTable)

        case _:
            print("Invalid For init")
            sys.exit(1)
            
    

    
def TAC_parseStatement(statement, instructions, symbolTable, typeTable, end=None):
    match statement:
        case parser.ExpressionStmt(exp=exp):
            TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
            #TAC_parseInstructions(exp, instructions, symbolTable)

        case parser.ReturnStmt(expression=exp):
            
            if exp:
                Val = TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
                instructions.append(TAC_returnInstruction(Val))
            else:
                instructions.append(TAC_returnInstruction())


        case parser.CompoundStatement(block=block):
            #print(block.blockItemList)
            TAC_parseBlock(block, instructions, symbolTable, typeTable)

        case parser.BreakStatement(identifier=id):
            instructions.append(TAC_JumpInst('break_{0}'.format(id)))
             
        case parser.ContinueStatement(identifier=id):
            instructions.append(TAC_JumpInst('continue_{0}'.format(id)))

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=id):
            #print(forInit)
            TAC_parseForInit(forInit, instructions, symbolTable, typeTable)
            
            #print(instructions)

            #jump label
            startLabel = makeTemp()
            instructions.append(TAC_LabelInst(startLabel))
            
            
            breakLabel = "break_{0}".format(id)

            if condExp:
                Val = TAC_emitTackyAndConvert(condExp, instructions, symbolTable, typeTable)
                #Val = TAC_parseInstructions(condExp, instructions, symbolTable)

                v = makeTempVariable(condExp.retType, symbolTable)
                instructions.append(TAC_CopyInstruction(Val, v))

                instructions.append(TAC_JumpIfZeroInst(v, breakLabel))


            TAC_parseStatement(statement, instructions, symbolTable, typeTable)

            continueLabel = "continue_{0}".format(id)
            instructions.append(TAC_LabelInst(continueLabel))

            if postExp:
                TAC_emitTackyAndConvert(postExp, instructions, symbolTable, typeTable)
                #TAC_parseInstructions(postExp, instructions, symbolTable)

            instructions.append(TAC_JumpInst(startLabel))

            instructions.append(TAC_LabelInst(breakLabel))
            
        

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):

            startLabel = "continue_{0}".format(id)

            instructions.append(TAC_LabelInst(startLabel))

            Val = TAC_emitTackyAndConvert(condExp, instructions, symbolTable, typeTable)
            #Val = TAC_parseInstructions(condExp, instructions, symbolTable)

            v = makeTempVariable(condExp.retType, symbolTable)

            instructions.append(TAC_CopyInstruction(Val, v))

            endLabel = "break_{0}".format(id)
            instructions.append(TAC_JumpIfZeroInst(v, endLabel))

            TAC_parseStatement(statement, instructions, symbolTable, typeTable)

            instructions.append(TAC_JumpInst(startLabel))

            instructions.append(TAC_LabelInst(endLabel))
            

        case parser.DoWhileStatement(statement=statement, condExp=condExp, identifier=id):    
            
            startLabel = makeTemp()

            instructions.append(TAC_LabelInst(startLabel))

            TAC_parseStatement(statement, instructions, symbolTable, typeTable)

            instructions.append(TAC_LabelInst('continue_{0}'.format(id)))

            Val = TAC_emitTackyAndConvert(condExp, instructions, symbolTable, typeTable)
            #Val = TAC_parseInstructions(condExp, instructions, symbolTable)

            v = makeTempVariable(condExp.retType, symbolTable)
            
            instructions.append(TAC_CopyInstruction(Val, v))

            instructions.append(TAC_JumpIfNotZeroInst(v, startLabel))

            instructions.append(TAC_LabelInst('break_{0}'.format(id)))
            

        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):

            val = TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
            #val = TAC_parseInstructions(exp, instructions, symbolTable)

            #print(type(val))
            c = makeTempVariable(exp.retType, symbolTable)
            
            ins0 = TAC_CopyInstruction(val, c)

            instructions.append(ins0)

            if end == None:
                end = makeTemp()

            if elseS:

                else_label = makeTemp()

                ins1 = TAC_JumpIfZeroInst(c, else_label)
                instructions.append(ins1)
                
                TAC_parseStatement(thenS, instructions, symbolTable, typeTable)

                instructions.append(TAC_JumpInst(end))

                instructions.append(TAC_LabelInst(else_label))

                #print(type(elseS))

                TAC_parseStatement(elseS, instructions, symbolTable, typeTable, end)

                if type(elseS) != parser.IfStatement:
                    instructions.append(TAC_LabelInst(end))

                
            else:
                ins1 = TAC_JumpIfZeroInst(c, end)
                instructions.append(ins1)

                #aqui nunca pasa porq no tiene un else
                TAC_parseStatement(thenS, instructions, symbolTable, typeTable, end)

                instructions.append(TAC_LabelInst(end))


            

        case parser.NullStatement():
            pass

        case _:
            print("Invalid Statement")
            sys.exit(1)

def TAC_emitInitializer(variableDecl, init, instructions, symbolTable, typeTable, offset):
    
    match init, init.retType:
        case parser.SingleInit(exp = exp, retType = retType), parser.ArrayType(elementType = elementType, size = size):
            match exp:
                case parser.StringExpression(string = string, retType = retType_):
                    #tu estas modificando otro offset!
                    for char in string:            
                        #print(retType)
                        typeSize = elementType.getBaseTypeSize(0, typeTable)
                        instructions.append(TAC_copyToOffset(TAC_ConstantValue(parser.ConstChar(ord(char))), variableDecl.identifier, offset[0]))
                        offset[0] += typeSize

                    #add zero padding
                    
                    print(size)
                    at = size

                    while at > len(string):
                        typeSize = elementType.getBaseTypeSize(0, typeTable)
                        instructions.append(TAC_copyToOffset(TAC_ConstantValue(parser.ConstChar(0)), variableDecl.identifier, offset[0]))
                        offset[0] += typeSize
                        at -= 1

                case _:
                    print("Error: Invalid")
                    sys.exit(1)
                    
            

        case parser.SingleInit(exp = exp, retType = retType), _:
            src = TAC_emitTackyAndConvert(exp, instructions, symbolTable, typeTable)
            instructions.append(TAC_copyToOffset(src, variableDecl.identifier, offset[0]))

        case parser.CompoundInit(initializerList = initializerList, retType = retType), parser.StuctureType(tag = tag):

            members = typeTable[tag].members
            members = list(members.values())

            for memInit, member in zip(initializerList, members):
                temp = [offset[0] + member.offset]
                TAC_emitInitializer(variableDecl, memInit, instructions, symbolTable, typeTable, temp)
                

        case parser.CompoundInit(initializerList = initializerList, retType = retType), parser.ArrayType(elementType = elementType, size = size):

            for i in initializerList:
                temp = [offset[0]]
                TAC_emitInitializer(variableDecl, i, instructions, symbolTable, typeTable, temp)
                offset[0] = offset[0] + elementType.getBaseTypeSize(0, typeTable)
            
        case _,_:
            print("Error: {0} {1}".format(init, init.retType))
            sys.exit(1)
    

def TAC_parseVarDeclarations(variableDecl, instructions, symbolTable, typeTable):

    if variableDecl.storageClass.storageClass != parser.StorageType.NULL:
        pass
    else:
        if variableDecl.initializer:
            
            TAC_emitInitializer(variableDecl, variableDecl.initializer, instructions, symbolTable, typeTable, [0])
            
            #src = TAC_emitTackyAndConvert(variableDecl.exp, instructions, symbolTable)
            #dst = TAC_VariableValue(variableDecl.identifier)
            #instructions.append(TAC_CopyInstruction(src, dst))
            #print(dst)

def TAC_parseDeclarations(decl, instructions, symbolTable, typeTable):
    match decl:
        case parser.VarDecl(variableDecl = variableDecl):
            TAC_parseVarDeclarations(variableDecl, instructions, symbolTable, typeTable)
                    
def TAC_parseBlock(block, instructions, symbolTable, typeTable):
    if block.blockItemList:        
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    TAC_parseDeclarations(dec, instructions, symbolTable, typeTable)

                case parser.S(statement=statement):
                    TAC_parseStatement(statement, instructions, symbolTable, typeTable)

def TAC_parseFunctionDefinition(functionDef, symbolTable, typeTable):
    if functionDef.block:
        identifier = functionDef.iden

        instructions = []

        TAC_parseBlock(functionDef.block, instructions, symbolTable, typeTable)
        
        Val = TAC_ConstantValue(parser.ConstInt(0))
        instructions.append(TAC_returnInstruction(Val))
        
        if functionDef.iden in symbolTable:
            decl = symbolTable[functionDef.iden]
            #print(decl[2].global_)
            global_ = decl.attrs.global_
            return TAC_FunctionDef(identifier, global_, functionDef.paramNames, instructions)

        print("ERROR: function is not in symbol table.")
        sys.exit(1)

def TAC_parseTopLevel(decl, symbolTable, typeTable):
    match decl:
        case parser.VarDecl(variableDecl = variableDecl):
            pass

        case parser.FunDecl(funDecl = funDecl):
            return TAC_parseFunctionDefinition(funDecl, symbolTable, typeTable)


def TAC_convertSymbolsToTAC(symbolTable, typeTable):
    tacDefs = []
    for name, entry in symbolTable.items():
        print(entry)
        match entry.attrs:
            case typeChecker.StaticAttributes(initialVal = initialVal, global_ = global_):
                #print(type(initialVal))
                match initialVal:
                    #si son tentativas se meten ahi
                    case typeChecker.Tentative():
                        #print(type(entry.type))
                        
                        init = None
                        match entry.type:
                            case parser.IntType():
                                init = typeChecker.IntInit(0)
                                
                            case parser.LongType():
                                init = typeChecker.LongInit(0)
                            
                            case parser.UIntType():
                                init = typeChecker.UIntInit(0)
                            
                            case parser.ULongType():
                                init = typeChecker.ULongInit(0)

                            case parser.DoubleType():
                                init = typeChecker.DoubleInit(0)

                            case parser.PointerType():
                                init = typeChecker.ULongInit(0)
                            
                            case parser.ArrayType(elementType = elementType, size = size):
                                size = entry.type.getBaseTypeSize(0, typeTable)
                                init = typeChecker.ZeroInit(size)

                            case parser.StuctureType(tag = tag):
                                size = entry.type.getBaseTypeSize(0, typeTable)
                                init = typeChecker.ZeroInit(size)

                                #structDef = typeTable[tag]
                                #init = typeChecker.ZeroInit(structDef.size)
                                
                            case _:
                                print("Error: Invalid Tentative Initializer. {0}".format(entry.type))
                                sys.exit(1)
                                
                                    
                        tacDefs.append(StaticVariable(name, global_, entry.type, [init]))

                    case typeChecker.Initial(initList = initList):
                        tacDefs.append(StaticVariable(name, global_, entry.type, initList))

                    case typeChecker.NoInitializer():
                        pass
                    
                    case _:
                        print("Invalid Initial Val. {0}".format(initialVal))
                        sys.exit(1)

            case typeChecker.ConstantAttr(staticInit = staticInit):
                tacDefs.append(StaticConstant(entry.name, entry.type, staticInit))


            case typeChecker.FunAttributes():
                pass

            case typeChecker.LocalAttributes():
                pass

            case _:
                print("Error: {0} {1}".format(type(entry.attrs), entry.attrs))
                sys.exit(1)
    #print(tacDefs)
    return tacDefs 
                
def TAC_parseProgram(pro, symbolTable, typeTable):
    topLevelList = []
    if pro.declList:
        for decl in pro.declList:
            topLevel = TAC_parseTopLevel(decl, symbolTable, typeTable)
            if topLevel:
                topLevelList.append(topLevel)

    ast = TAC_Program(topLevelList)
    tacDefs = TAC_convertSymbolsToTAC(symbolTable, typeTable)

    ast.topLevelList.extend(tacDefs)

    return ast

    