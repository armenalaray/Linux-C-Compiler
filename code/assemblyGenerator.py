from enum import Enum
import tacGenerator
import sys
import parser
import typeChecker
import copy
import traceback

from tacGenerator import makeTemp
#from tacGenerator import makeStaticConstant

class Program:
    
    def __init__(self, topLevelList):
        self.topLevelList = topLevelList

    def __str__(self):

        return "ASM Program: {self.topLevelList}".format(self=self)

class AssemblyType:
    pass

class Byte(AssemblyType):
    pass

class Longword(AssemblyType):
    pass

class Quadword(AssemblyType):
    pass

class Double(AssemblyType):
    pass

class ByteArray(AssemblyType):
    def __init__(self, size, alignment):
        self.size = size
        self.alignment = alignment
    
    def __str__(self):
        return "ByteArray(Size = {self.size}, Alignment = {self.alignment})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TopLevel:
    pass

class StaticConstant(TopLevel):
    def __init__(self, identifier, alignment, staticInit):
        self.identifier = identifier
        self.alignment = alignment
        self.staticInit = staticInit

    def __str__(self):
        return "Static Constant: Alignment = {self.alignment} : {self.identifier} = {self.staticInit}".format(self=self)

    def __repr__(self):
        return self.__str__()

class StaticVariable(TopLevel):

    def __init__(self, identifier, global_, alignment, initList):
        self.identifier = identifier
        self.global_ = global_
        self.alignment = alignment
        self.initList = initList

    def __str__(self):
        return "Static Variable: Global = {self.global_} Alignment = {self.alignment} : {self.identifier} = {self.initList}".format(self=self)

    def __repr__(self):
        return self.__str__()
    
class Function(TopLevel):

    def __init__(self, identifier, global_, insList, stackOffset = None):
        self.identifier = identifier
        self.global_ = global_
        self.insList = insList
        self.stackOffset = stackOffset 

    def __str__(self):
        
        return "Function {self.identifier} stackOffset: {self.stackOffset} global: {self.global_} instructions:{self.insList}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class ReturnInstruction:

    def __init__(self):
        pass
    
    #debuggear
    def __str__(self):
        return "ret"
    
    
    def __repr__(self):
        return self.__str__()

class Cvttsd2si:

    def __init__(self, assType, sourceO, destO):
        self.assType = assType
        self.sourceO = sourceO
        self.destO = destO
        
    def __str__(self):
        return "AssType: {self.assType} Cvttsd2si({self.sourceO}, {self.destO})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()


class Cvtsi2sd:

    def __init__(self, assType, sourceO, destO):
        self.assType = assType
        self.sourceO = sourceO
        self.destO = destO
        
    def __str__(self):
        return "AssType: {self.assType} Cvtsi2sd({self.sourceO}, {self.destO})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()


class MovInstruction:

    def __init__(self, assType, sourceO, destO):
        self.assType = assType
        self.sourceO = sourceO
        self.destO = destO
        
    def __str__(self):
        return "AssType: {self.assType} Mov({self.sourceO}, {self.destO})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()

class MovSXInstruction:

    def __init__(self, srcType, dstType, sourceO, destO):
        self.srcType = srcType
        self.dstType = dstType
        self.sourceO = sourceO
        self.destO = destO

    def __str__(self):
        return "SrcType: {self.srcType} DstType: {self.dstType} MovSX({self.sourceO}, {self.destO})".format(self=self)

    def __repr__(self):
        return self.__str__()    
    
class MovZeroExtendIns:

    def __init__(self, srcType, dstType, sourceO, destO):
        self.srcType = srcType
        self.dstType = dstType
        self.sourceO = sourceO
        self.destO = destO

    def __str__(self):
        return "SrcType: {self.srcType} DstType: {self.dstType} MovZeroExtend({self.sourceO}, {self.destO})".format(self=self)

    def __repr__(self):
        return self.__str__()    
    
class LeaInstruction:

    def __init__(self, sourceO, destO):
        self.sourceO = sourceO
        self.destO = destO
        
    def __str__(self):
        return "Lea({self.sourceO}, {self.destO})".format(self=self)

    def __repr__(self):
        return self.__str__()    
    
class UnaryInstruction:
    def __init__(self, operator, assType, dest):
        self.operator = operator
        self.assType = assType
        self.dest = dest
    
    def __str__(self):
        return "AssType: {self.assType} Unary({self.operator}, {self.dest})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class CompInst:
    def __init__(self, assType, operand0, operand1):
        self.assType = assType
        self.operand0 = operand0
        self.operand1 = operand1
    
    def __str__(self):
        return "AssType: {self.assType} Cmp({self.operand0}, {self.operand1})".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class JumpInst:
    def __init__(self, identifier):
        self.identifier = identifier
    
    def __str__(self):
        return "Jmp({self.identifier})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class ConcCodeType(Enum):
    E = 1
    NE = 2
    G = 3
    GE = 4
    L = 5
    LE = 6

class ConcCodeTypeUnsigned(Enum):
    E = 1
    NE = 2
    A = 3
    AE = 4
    B = 5
    BE = 6

class JumpCCInst:
    def __init__(self, conc_code, identifier):
        self.conc_code = conc_code
        self.identifier = identifier
    
    def __str__(self):
        return "JmpCC({self.conc_code}, {self.identifier})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class SetCCInst:
    def __init__(self, conc_code, operand):
        self.conc_code = conc_code
        self.operand = operand
    
    def __str__(self):
        return "SetCC({self.conc_code}, {self.operand})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class LabelInst:
    def __init__(self, identifier):
        self.identifier = identifier
    
    def __str__(self):
        return "Label({self.identifier})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class BinaryInstruction:
    def __init__(self, operator, assType, src, dest):
        self.operator = operator
        self.assType = assType
        self.src = src
        self.dest = dest
    
    def __str__(self):
        return "AssType: {self.assType} Binary({self.operator}, {self.src}, {self.dest})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

#(operator, src2, dst)

class IDivInstruction:
    def __init__(self, assType, divisor):
        self.assType = assType
        self.divisor = divisor
    
    def __str__(self):
        return "AssType: {self.assType} Idiv({self.divisor})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class DivInstruction:
    def __init__(self, assType, divisor):
        self.assType = assType
        self.divisor = divisor
    
    def __str__(self):
        return "AssType: {self.assType} Div({self.divisor})".format(self=self)
    
    def __repr__(self):
        return self.__str__()
        

class CDQInstruction:
    def __init__(self, assType):
        self.assType = assType

    def __str__(self):
        return "AssType: {self.assType} Cdq"
    
    
    def __repr__(self):
        return self.__str__()

class Pop():
    def __init__(self, reg):
        self.reg = reg
    
    def __str__(self):
        return "Pop({self.reg})".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class PushInstruction():
    def __init__(self, operand):
        self.operand = operand
    
    def __str__(self):
        return "Push({self.operand})".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class CallInstruction():
    def __init__(self, identifier):
        self.identifier = identifier    
    
    def __str__(self):
        return "Call({self.identifier})".format(self=self)
    
    def __repr__(self):
        return self.__str__()


class Operand:
    pass

class PseudoMem(Operand):
    
    def __init__(self, identifier, offset):
        self.identifier = identifier
        self.offset = offset

    def __str__(self):
        return r"PseudoMem({self.identifier}, {self.offset})".format(self=self)

    def __repr__(self):
        return self.__str__()
    
    
class Indexed(Operand):
    def __init__(self, base, index, scale):
        self.base = base
        self.index = index
        self.scale = scale

    def __str__(self):
        return r"Indexed({self.base} + {self.index} * {self.scale})".format(self=self)

    def __repr__(self):
        return self.__str__()

class PseudoRegisterOperand:

    def __init__(self, pseudo):
        self.pseudo = pseudo
    
    def __str__(self):
        return r"Pseudo({self.pseudo})".format(self=self)

    def __repr__(self):
        return self.__str__()

class MemoryOperand:
    def __init__(self, reg, int):
        self.reg = reg
        self.int = int

    def __str__(self):
        return "Memory({self.reg}, {self.int})".format(self=self)

class DataOperand:
    def __init__(self, identifier, offset):
        self.identifier = identifier
        self.offset = offset

    def __str__(self):
        return "Data({self.identifier}, {self.offset})".format(self=self)

class RegisterOperand:

    def __init__(self, register):
        self.register = register
    
    def __str__(self):
        return r"Reg({self.register})".format(self=self)
    """
    
    def __repr__(self):
        return self.__str__()
    """

class ImmediateOperand:
    def __init__(self, intVal):
        self.imm = intVal

    def __str__(self):
        return r"Imm({self.imm})".format(self=self)
    
    """
    def __repr__(self):
        return self.__str__()
    """

class UnopType(Enum):
    Not = 1
    Neg = 2
    Shr = 3
    
class BinopType(Enum):
    Add = 1
    Sub = 2
    Mult = 3
    DivDouble = 4
    And = 5
    Or = 6
    Xor = 7
    Shl = 8
    ShrTwoOp = 9


class UnaryOperator:
    def __init__(self, operator):
        self.operator = operator
    
    def __str__(self):
        match self.operator:
            case UnopType.Not:
                return "Not"
            case UnopType.Neg:
                return "Neg"
            case UnopType.Shr:
                return "Shr"
            case _:
                return "_"

class BinaryOperator:
    def __init__(self, operator):
        self.operator = operator

    def __str__(self):
        match self.operator:
            case BinopType.Add:
                return "Add"
            case BinopType.Sub:
                return "Sub"
            case BinopType.Mult:
                return "Mult"
            case BinopType.And:
                return "And"
            case BinopType.Or:
                return "Or"
            case BinopType.Xor:
                return "Xor"
            case BinopType.DivDouble:
                return "DivDouble"
            
            case _:
                return "_"

class RegisterType(Enum):
    #These are used for registers
    DI = 0
    SI = 1
    DX = 2
    CX = 3
    R8 = 4
    R9 = 5
    
    AX = 6
    BX = 7

    R10 = 8
    R11 = 9
    R12 = 10
    R13 = 11
    R14 = 12
    R15 = 13

    SP = 14
    BP = 15

class SSERegisterType(Enum):
    XMM0 = 0
    XMM1 = 1
    XMM2 = 2
    XMM3 = 3
    XMM4 = 4
    XMM5 = 5
    XMM6 = 6
    XMM7 = 7
    XMM8 = 8
    XMM9 = 9
    XMM10 = 10
    XMM11 = 11
    XMM12 = 12
    XMM13 = 13
    XMM14 = 14
    XMM15 = 15


class Register:
    def __init__(self, register):
        self.register = register

    def __str__(self):
        match self.register:
            case RegisterType.AX:
                return "AX"
            case RegisterType.CX:
                return "CX"
            case RegisterType.DX:
                return "DX"
            case RegisterType.DI:
                return "DI"
            case RegisterType.SI:
                return "SI"
            case RegisterType.R8:
                return "R8d"
            case RegisterType.R9:
                return "R9d"
            case RegisterType.R10:
                return "R10d"
            case RegisterType.R11:
                return "R11d"
            case RegisterType.SP:
                return "SP"
            
            case SSERegisterType.XMM0:
                return "XMM0"
            case SSERegisterType.XMM1:
                return "XMM1"
            case SSERegisterType.XMM2:
                return "XMM2"
            case SSERegisterType.XMM3:
                return "XMM3"
            case SSERegisterType.XMM4:
                return "XMM4"
            case SSERegisterType.XMM5:
                return "XMM5"
            case SSERegisterType.XMM6:
                return "XMM6"
            case SSERegisterType.XMM7:
                return "XMM7"
            case SSERegisterType.XMM14:
                return "XMM14"
            case SSERegisterType.XMM15:
                return "XMM15"
            
            case RegisterType.BP:
                return "BP"

            case _:
                return "_"


def parseValueFromType(type, symbolTable, typeTable):
    
    match type:

        case parser.CharType():
            asmType = Byte()
            cType = parser.CharType()

        case parser.SCharType():
            asmType = Byte()
            cType = parser.SCharType()

        case parser.UCharType():
            asmType = Byte()
            cType = parser.UCharType()

        case parser.IntType():
            asmType = Longword()
            cType = parser.IntType()

        case parser.LongType():
            asmType = Quadword()
            cType = parser.LongType()
        
        case parser.UIntType():
            asmType = Longword()
            cType = parser.UIntType()
        
        case parser.ULongType():
            asmType = Quadword()
            cType = parser.ULongType()

        case parser.DoubleType():
            asmType = Double()
            cType = parser.DoubleType()
        
        case parser.PointerType(referenceType = referenceType):
            asmType = Quadword()
            cType = parser.ULongType()

        case parser.ArrayType(elementType = elementType, size = size):
            
            asmType = None
            cType = symbolTable[i].type
            
            sizeArray = cType.getBaseTypeSize(0, typeTable)
            print(sizeArray)

            while type(cType) == parser.ArrayType:
                cType = cType.elementType

            alignment, other = matchCType(cType, typeTable)
                
            if sizeArray < 16:
                asmType = ByteArray(sizeArray, alignment)                
            else:
                asmType = ByteArray(sizeArray, 16)                

            return asmType, cType, PseudoMem(i, 0)
        
        case parser.StuctureType(tag = tag):
            cType = parser.StuctureType(tag)
            
            if tag in typeTable:
                structDef = typeTable[tag]
                asmType = ByteArray(structDef.size, structDef.alignment)

                return asmType, cType, PseudoMem(i, 0)
            
            return None, cType, PseudoMem(i, 0)
        
        case _:
            traceback.print_stack()
            print("Error: Invalid Assembly Type.")
            sys.exit(1)

    return asmType, cType, PseudoRegisterOperand(i)

def parseValue(v, symbolTable, typeTable, topLevelList):
    asmType = None
    cType = None
    alignment = 0

    match v:
        case tacGenerator.TAC_ConstantValue(const = const):

            match const:

                case parser.ConstChar():
                    asmType = Byte()
                    cType = parser.CharType()
                    return asmType, cType, ImmediateOperand(const.int)

                case parser.ConstUChar():
                    asmType = Byte()
                    cType = parser.UCharType()
                    return asmType, cType, ImmediateOperand(const.int)

                case parser.ConstInt():
                    asmType = Longword()
                    cType = parser.IntType()
                    return asmType, cType, ImmediateOperand(const.int)
                    
                case parser.ConstLong():
                    asmType = Quadword()
                    cType = parser.LongType()
                    return asmType, cType, ImmediateOperand(const.int)

                case parser.ConstUInt():
                    asmType = Longword()
                    cType = parser.UIntType()
                    return asmType, cType, ImmediateOperand(const.int)
                
                case parser.ConstULong():
                    asmType = Quadword()
                    cType = parser.ULongType()
                    return asmType, cType, ImmediateOperand(const.int)

                case parser.ConstDouble():
                    name = makeTemp()
                    topLevelList.append(StaticConstant(name, 8, typeChecker.DoubleInit(const.double)))
                    
                    asmType = Double()
                    cType = parser.DoubleType()
                    return asmType, cType, DataOperand(name, 0)
                
                
                case _:
                    print("Error: Invalid Assembly Constant. {0}".format(type(const)))
                    sys.exit(1)

        case tacGenerator.TAC_VariableValue(identifier=i):

            match symbolTable[i].type:

                case parser.CharType():
                    asmType = Byte()
                    cType = parser.CharType()

                case parser.SCharType():
                    asmType = Byte()
                    cType = parser.SCharType()

                case parser.UCharType():
                    asmType = Byte()
                    cType = parser.UCharType()

                case parser.IntType():
                    asmType = Longword()
                    cType = parser.IntType()

                case parser.LongType():
                    asmType = Quadword()
                    cType = parser.LongType()
                
                case parser.UIntType():
                    asmType = Longword()
                    cType = parser.UIntType()
                
                case parser.ULongType():
                    asmType = Quadword()
                    cType = parser.ULongType()

                case parser.DoubleType():
                    asmType = Double()
                    cType = parser.DoubleType()
                
                case parser.PointerType(referenceType = referenceType):
                    asmType = Quadword()
                    cType = parser.ULongType()

                case parser.ArrayType(elementType = elementType, size = size):
                    
                    asmType = None
                    cType = symbolTable[i].type
                    
                    sizeArray = cType.getBaseTypeSize(0, typeTable)
                    print(sizeArray)

                    while type(cType) == parser.ArrayType:
                        cType = cType.elementType

                    alignment, other = matchCType(cType, typeTable)
                        
                    if sizeArray < 16:
                        asmType = ByteArray(sizeArray, alignment)                
                    else:
                        asmType = ByteArray(sizeArray, 16)                

                    return asmType, cType, PseudoMem(i, 0)
                
                case parser.StuctureType(tag = tag):
                    cType = parser.StuctureType(tag)
                    
                    if tag in typeTable:
                        structDef = typeTable[tag]
                        asmType = ByteArray(structDef.size, structDef.alignment)

                        return asmType, cType, PseudoMem(i, 0)
                    
                    return None, cType, PseudoMem(i, 0)
                
                case _:
                    traceback.print_stack()
                    print("Error: Invalid Assembly Variable_. {0}".format(symbolTable[i].type))
                    sys.exit(1)

            return asmType, cType, PseudoRegisterOperand(i)
        
        case _:

            match symbolTable[v].type:
                
                case parser.CharType():
                    asmType = Byte()
                    cType = parser.CharType()

                case parser.SCharType():
                    asmType = Byte()
                    cType = parser.SCharType()

                case parser.UCharType():
                    asmType = Byte()
                    cType = parser.UCharType()

                case parser.IntType():
                    asmType = Longword()
                    cType = parser.IntType()

                case parser.LongType():
                    asmType = Quadword()
                    cType = parser.LongType()
                
                case parser.UIntType():
                    asmType = Longword()
                    cType = parser.UIntType()
                
                case parser.ULongType():
                    asmType = Quadword()
                    cType = parser.ULongType()

                case parser.DoubleType():
                    asmType = Double()
                    cType = parser.DoubleType()
                
                case parser.PointerType(referenceType = referenceType):
                    asmType = Quadword()
                    cType = parser.ULongType()

                case parser.ArrayType():

                    asmType = None
                    cType = symbolTable[v].type
                    
                    sizeArray = cType.getBaseTypeSize(0)
                    print(sizeArray)

                    while type(cType) == parser.ArrayType:
                        cType = cType.elementType

                    alignment, other = matchCType(cType)
                        
                    if sizeArray < 16:
                        asmType = ByteArray(sizeArray, alignment)                
                    else:
                        asmType = ByteArray(sizeArray, 16)                

                    return asmType, cType, PseudoMem(v, 0)
                
                case parser.StuctureType(tag = tag):
                    structDef = typeTable[tag]
                    asmType = ByteArray(structDef.size, structDef.alignment)
                    cType = parser.StuctureType(tag)

                    return asmType, cType, PseudoMem(v, 0)
                
                case _:
                    print("Error: Invalid Assembly Variable. {0}".format(symbolTable[v].type))
                    sys.exit(1)
            return asmType, cType, PseudoRegisterOperand(v)

def parseOperator(op):
    match op:
        case tacGenerator.TAC_UnaryOperator(operator=o):
            match o:
                case tacGenerator.UnopType.NEGATE:
                    return UnaryOperator(UnopType.Neg)
                case tacGenerator.UnopType.COMPLEMENT:
                    return UnaryOperator(UnopType.Not)
                case _:
                    print("Invalid TAC operator.")
                    sys.exit(1)
        case tacGenerator.TAC_BinaryOperator(operator=o):
            match o:
                case tacGenerator.BinopType.ADD:
                    return BinaryOperator(BinopType.Add)
                case tacGenerator.BinopType.MULTIPLY:
                    return BinaryOperator(BinopType.Mult)
                case tacGenerator.BinopType.SUBTRACT:
                    return BinaryOperator(BinopType.Sub)

def Expect(*args):
    other = None
    for i in args:
        if other:
            if type(i) != type(other):
                traceback.print_stack()
                print("Types are not equal.")
                sys.exit(1)
        other = i

"""
def isIntegerType(type_):
    if type(type_) == parser.UIntType or type(type_) == parser.ULongType or type(type_) == parser.IntType or type(type_) == parser.LongType:
        return True 
    return False
"""

def parseUnaryInstructionGeneral(src_, dst_, o, symbolTable, typeTable, ASM_Instructions, topLevelList):
    type1, alignment1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
    type2, alignment2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

    operator = parseOperator(o)

    instruction0 = MovInstruction(type1, src, dst)
    instruction1 = UnaryInstruction(operator, type1, dst)
    
    ASM_Instructions.append(instruction0)
    ASM_Instructions.append(instruction1)

class ABI_StructType(Enum):
    MEMORY = 1
    SSE = 2
    INTEGER = 3

def flattenMembers(members, typeTable, outList):

    members = list(members.values())

    for member in members:

        match member.memberType:
            case parser.StuctureType(tag = tag):
                structDef = typeTable[tag]
                flattenMembers(structDef.members, typeTable, outList)
                
            case parser.ArrayType(elementType = elementType, size = size):
                for i in range(size):
                    outList.append(elementType)

            case _:
                outList.append(member.memberType)

    

def classifyStructure(struct, typeTable):
    size = struct.size
    if size > 16:
        result = []
        while size > 0:
            result.append(ABI_StructType.MEMORY)
            size -= 8

        return result
    
    members = []
    flattenMembers(struct.members, typeTable, members)

    print(members)

    if size > 8:
        if type(members[0]) == parser.DoubleType and type(members[-1]) == parser.DoubleType:
            return [ABI_StructType.SSE, ABI_StructType.SSE]
        
        if type(members[0]) == parser.DoubleType:
            return [ABI_StructType.SSE, ABI_StructType.INTEGER]
            pass

        if type(members[-1]) == parser.DoubleType:
            return [ABI_StructType.INTEGER, ABI_StructType.SSE]
            pass

        return [ABI_StructType.INTEGER, ABI_StructType.INTEGER]


    if type(members[0]) == parser.DoubleType:
        return [ABI_StructType.SSE]

    else:
        return [ABI_StructType.INTEGER]

def classifyReturnValue(retVal, symbolTable, typeTable, topLevelList):

    #assemblyTypeOf(retVal)
    t, cType1, operand = parseValue(retVal, symbolTable, typeTable, topLevelList)

    if type(cType1) == parser.DoubleType:
        return ([], [operand], False)
    
    elif typeChecker.isScalar(cType1):
        typedOperand = (t, operand)
        return ([typedOperand], [], False)

    else:
        match cType1:
            case parser.StuctureType(tag = tag):
                structDef = typeTable[tag]
                classes = classifyStructure(structDef, typeTable)
                structSize = structDef.size

                if classes[0] == ABI_StructType.MEMORY:
                    return ([], [], True)
                
                else:

                    intRetVals = []
                    doubleRetVals = []
                    offset = 0
                    for class_ in classes:

                        operand = PseudoMem(retVal.identifier, offset)

                        match class_:
                            case ABI_StructType.SSE:
                                doubleRetVals.append(operand)
                                
                            case ABI_StructType.INTEGER:
                                eightByteType = getEightByteType(offset, structSize)
                                intRetVals.append((eightByteType, operand))

                                pass
                            case ABI_StructType.MEMORY:
                                print("Error: Invalid ABI.")
                                sys.exit(1)

                        offset += 8  

                    return (intRetVals, doubleRetVals, False)

                
            case _:
                print("Error:")
                sys.exit(1)

def getEightByteType(offset, structSize):
    bytesFromEnd = structSize - offset
    print("bytesFromEnd:", bytesFromEnd)

    if bytesFromEnd >= 8:
        return Quadword()
    
    if bytesFromEnd == 4:
        return Longword()
    
    if bytesFromEnd == 1:
        return Byte()
    
    return ByteArray(bytesFromEnd, 8)    

def classifyParametersFromTypes(paramTypes, symbolTable, typeTable, returnInMemory):

    intRegArgs = []
    doubleRegArgs = []
    stackArgs = []

    intRegsAvailable = 6

    if returnInMemory:
        intRegsAvailable = 5

    else:
        intRegsAvailable = 6


    for paramType in paramTypes:
        t, cType1, operand = parseValueFromType(paramType, symbolTable, typeTable)

        print("Operand:", operand)

        typedOperand = (t, operand)

        if type(cType1) == parser.DoubleType:

            if len(doubleRegArgs) < 8:
                doubleRegArgs.append(operand)
            else:
                stackArgs.append(typedOperand)

        elif typeChecker.isScalar(cType1):

            if len(intRegArgs) < intRegsAvailable:
                intRegArgs.append(typedOperand)
            else:
                stackArgs.append(typedOperand)
            
        else:
            
            match cType1:
                case parser.StuctureType(tag = tag):

                    structDef = typeTable[tag]
                    classes = classifyStructure(structDef, typeTable)

                    useStack = True
                    structSize = structDef.size

                    if classes[0] != ABI_StructType.MEMORY:
                        
                        #breakpoint()

                        tentativeInts = []
                        tentativeDoubles = []
                        offset = 0

                        for class_ in classes:
                            operand_ = addOffset(operand, offset)

                            if class_ == ABI_StructType.SSE:
                                tentativeDoubles.append(operand_)
                            else:
                                eightByteType = getEightByteType(offset, structSize)
                                tentativeInts.append((eightByteType, operand_))
                                
                            offset += 8

                        
                        if len(tentativeDoubles) + len(doubleRegArgs) <= 8 and len(tentativeInts) + len(intRegArgs) <= intRegsAvailable:
                            doubleRegArgs.extend(tentativeDoubles)
                            intRegArgs.extend(tentativeInts)
                            useStack = False

                    if useStack:
                        offset = 0
                        for class_ in classes:
                            operand_ = addOffset(operand, offset)

                            eightByteType = getEightByteType(offset, structSize)
                            stackArgs.append((eightByteType, operand_))
                            offset += 8

                case _:
                    print("Error:")
                    sys.exit(1)
                
    return intRegArgs, doubleRegArgs, stackArgs  

def classifyParameters(values, symbolTable, typeTable, topLevelList, returnInMemory):
    
    intRegArgs = []
    doubleRegArgs = []
    stackArgs = []

    intRegsAvailable = 6

    if returnInMemory:
        intRegsAvailable = 5

    else:
        intRegsAvailable = 6


    for arg in values:
        #t, cType1, operand = parseValueFromType(type, symbolTable, typeTable)
        t, cType1, operand = parseValue(arg, symbolTable, typeTable, topLevelList)

        print("Operand:", operand)

        typedOperand = (t, operand)

        if type(cType1) == parser.DoubleType:

            if len(doubleRegArgs) < 8:
                doubleRegArgs.append(operand)
            else:
                stackArgs.append(typedOperand)

        elif typeChecker.isScalar(cType1):

            if len(intRegArgs) < intRegsAvailable:
                intRegArgs.append(typedOperand)
            else:
                stackArgs.append(typedOperand)
            
        else:
            
            match cType1:
                case parser.StuctureType(tag = tag):

                    structDef = typeTable[tag]
                    classes = classifyStructure(structDef, typeTable)

                    useStack = True
                    structSize = structDef.size

                    if classes[0] != ABI_StructType.MEMORY:
                        
                        #breakpoint()

                        tentativeInts = []
                        tentativeDoubles = []
                        offset = 0

                        for class_ in classes:
                            operand_ = addOffset(operand, offset)

                            if class_ == ABI_StructType.SSE:
                                tentativeDoubles.append(operand_)
                            else:
                                eightByteType = getEightByteType(offset, structSize)
                                tentativeInts.append((eightByteType, operand_))
                                
                            offset += 8

                        
                        if len(tentativeDoubles) + len(doubleRegArgs) <= 8 and len(tentativeInts) + len(intRegArgs) <= intRegsAvailable:
                            doubleRegArgs.extend(tentativeDoubles)
                            intRegArgs.extend(tentativeInts)
                            useStack = False

                    if useStack:
                        offset = 0
                        for class_ in classes:
                            operand_ = addOffset(operand, offset)

                            eightByteType = getEightByteType(offset, structSize)
                            stackArgs.append((eightByteType, operand_))
                            offset += 8

                case _:
                    print("Error:")
                    sys.exit(1)
                
    return intRegArgs, doubleRegArgs, stackArgs  

def copyBytes(src, dst, size, ASM_Instructions):
                    
    match src, dst:
        case MemoryOperand(reg = reg1, int = int1), MemoryOperand(reg = reg2, int = int2):
            base1 = int1
            base2 = int2

            target = base1 + size

            while base1 < target:
                dif = target - base1

                bytes = None
                type_ = None

                if dif >= 8:
                    type_ = Quadword()
                    bytes = 8
                elif dif >= 4:
                    type_ = Longword()
                    bytes = 4
                else:
                    type_ = Byte()
                    bytes = 1

                if type == None:
                    print("Error: Invalid Copy Instruction.")
                    sys.exit(1)
                
                ASM_Instructions.append(MovInstruction(type_, MemoryOperand(reg1, base1), MemoryOperand(reg2, base2)))

                base1 += bytes
                base2 += bytes

        case MemoryOperand(reg = reg, int = int), PseudoMem(identifier = identifier, offset = offset):
            
            base1 = int
            base2 = offset

            target = base1 + size

            while base1 < target:
                dif = target - base1

                bytes = None
                type_ = None

                if dif >= 8:
                    type_ = Quadword()
                    bytes = 8
                elif dif >= 4:
                    type_ = Longword()
                    bytes = 4
                else:
                    type_ = Byte()
                    bytes = 1

                if type == None:
                    print("Error: Invalid Copy Instruction.")
                    sys.exit(1)
                
                ASM_Instructions.append(MovInstruction(type_, MemoryOperand(reg, base1), PseudoMem(identifier, base2)))

                base1 += bytes
                base2 += bytes
            
        case PseudoMem(identifier = identifier, offset = offset), MemoryOperand(reg = reg, int = int):
            
            base1 = offset
            base2 = int

            target = base1 + size

            while base1 < target:
                dif = target - base1

                bytes = None
                type_ = None

                if dif >= 8:
                    type_ = Quadword()
                    bytes = 8
                elif dif >= 4:
                    type_ = Longword()
                    bytes = 4
                else:
                    type_ = Byte()
                    bytes = 1

                if type == None:
                    print("Error: Invalid Copy Instruction.")
                    sys.exit(1)
                
                ASM_Instructions.append(MovInstruction(type_, PseudoMem(identifier, base1), MemoryOperand(reg, base2)))

                base1 += bytes
                base2 += bytes

        case PseudoMem(identifier = identifier1, offset = offset1), PseudoMem(identifier = identifier2, offset = offset2):

            base1 = offset1
            base2 = offset2

            target = base1 + size

            while base1 < target:
                dif = target - base1

                bytes = None
                type_ = None

                if dif >= 8:
                    type_ = Quadword()
                    bytes = 8
                elif dif >= 4:
                    type_ = Longword()
                    bytes = 4
                else:
                    type_ = Byte()
                    bytes = 1

                if type == None:
                    print("Error: Invalid Copy Instruction.")
                    sys.exit(1)
                
                ASM_Instructions.append(MovInstruction(type_, PseudoMem(identifier1, base1), PseudoMem(identifier2, base2)))

                base1 += bytes
                base2 += bytes
            
        case _:
            traceback.print_stack()
            print("Error: Invalid memory Operand. {0} {1}".format(src, dst))
            sys.exit(1)

def copyBytesFromReg(srcReg, destOp, byteCount, ASM_Instructions):
    offset = 0
    while offset < byteCount:
        dstByte = addOffset(destOp, offset)
        ASM_Instructions.append(MovInstruction(Byte(), RegisterOperand(Register(srcReg)), dstByte))

        if offset < byteCount - 1:
            ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.ShrTwoOp), Quadword(), ImmediateOperand(8), RegisterOperand(Register(srcReg))))

        offset += 1


def addOffset(operand, offset):
    match operand:
        case PseudoMem(identifier = identifier, offset = offset_):
            return PseudoMem(identifier, offset_ + offset)
            
        case _:
            print("Error: Invalid Operand.")
            sys.exit(1)


def copyBytesToReg(srcOp, dstReg, byteCount, ASM_Instructions):
    offset = byteCount - 1

    while offset >= 0:
        srcByte = addOffset(srcOp, offset)
        ASM_Instructions.append(MovInstruction(Byte(), srcByte, RegisterOperand(Register(dstReg))))
        
        #Los esta shifteando e insertando!
        if offset > 0:
            ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Shl), Quadword(), ImmediateOperand(8), RegisterOperand(Register(dstReg))))

        offset -= 1

def ASM_parseInstructions(TAC_Instructions, ASM_Instructions, symbolTable, typeTable, topLevelList, parentFunName):

    for i in TAC_Instructions:
        match i:
            
            #scale is a number
            case tacGenerator.TAC_addPtr(ptr = ptr_, index = index_, scale = scale, dst = dst_):
                
                type1, cType1, ptr = parseValue(ptr_, symbolTable, typeTable, topLevelList)
                type2, cType2, index = parseValue(index_, symbolTable, typeTable, topLevelList)
                type3, cType3, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)
                
                match index_:
                    case tacGenerator.TAC_ConstantValue(const = const):

                        ASM_Instructions.append(MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX))))

                        ASM_Instructions.append(LeaInstruction(MemoryOperand(Register(RegisterType.AX), const.int * scale), dst))
                        
                        
                    case tacGenerator.TAC_VariableValue(identifier = identifier):
                        
                        def PtrArithmeticSupportedScale():
                            ASM_Instructions.append(MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX))))

                            ASM_Instructions.append(MovInstruction(Quadword(), index, RegisterOperand(Register(RegisterType.DX))))

                            ASM_Instructions.append(LeaInstruction(Indexed(Register(RegisterType.AX), Register(RegisterType.DX), scale), dst))

                        match scale:
                            case 1:
                                PtrArithmeticSupportedScale()
                                pass
                            case 2:
                                PtrArithmeticSupportedScale()
                                pass
                            case 4:
                                PtrArithmeticSupportedScale()
                                pass
                            case 8:
                                PtrArithmeticSupportedScale()
                                pass
                            case _:
                                ASM_Instructions.append(MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX))))

                                ASM_Instructions.append(MovInstruction(Quadword(), index, RegisterOperand(Register(RegisterType.DX))))

                                ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Mult), Quadword(), ImmediateOperand(scale), RegisterOperand(Register(RegisterType.DX))))

                                ASM_Instructions.append(LeaInstruction(Indexed(Register(RegisterType.AX), Register(RegisterType.DX), 1), dst))

                        """
                        if scale > 8 :
                            ASM_Instructions.append(MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX))))

                            ASM_Instructions.append(MovInstruction(Quadword(), index, RegisterOperand(Register(RegisterType.DX))))

                            ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Mult), Quadword(), ImmediateOperand(scale), RegisterOperand(Register(RegisterType.DX))))

                            ASM_Instructions.append(LeaInstruction(Indexed(Register(RegisterType.AX), Register(RegisterType.DX), 1), dst))

                        else:
                            ASM_Instructions.append(MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX))))

                            ASM_Instructions.append(MovInstruction(Quadword(), index, RegisterOperand(Register(RegisterType.DX))))

                            ASM_Instructions.append(LeaInstruction(Indexed(Register(RegisterType.AX), Register(RegisterType.DX), scale), dst))
                        """

                    case _:
                        print("Error: Invalid TAC Value.")
                        sys.exit(1)

            case tacGenerator.TAC_copyFromOffset(src = src, offset = offset, dst = dst):

                type1, cType1, dst = parseValue(dst, symbolTable, typeTable, topLevelList)

                match cType1:
                    case parser.StuctureType(tag = tag):

                        src = PseudoMem(src, offset)

                        copyBytes(src, dst, typeTable[tag].size, ASM_Instructions)

                        """
                        size = typeTable[tag].size

                        while dst.offset < size:

                            dif = size - dst.offset
                            print("DIF:", dif)

                            bytes = None
                            type_ = None

                            if dif >= 8:
                                type_ = Quadword()
                                bytes = 8
                            elif dif >= 4:
                                type_ = Longword()
                                bytes = 4
                            else:
                                type_ = Byte()
                                bytes = 1

                            if type == None:
                                print("Error: Invalid Copy Instruction.")
                                sys.exit(1)

                            s = copy.deepcopy(src)
                            d = copy.deepcopy(dst)
                            
                            ASM_Instructions.append(MovInstruction(type_, s, d))

                            src.offset += bytes
                            dst.offset += bytes
                        """
                        
                    case _:
                        ASM_Instructions.append(MovInstruction(type1, PseudoMem(src, offset), dst))


            #dest is a string
            case tacGenerator.TAC_copyToOffset(src = src, dst = dst, offset = offset):
                #breakpoint()
                type1, cType1, src = parseValue(src, symbolTable, typeTable, topLevelList)

                match cType1:
                    case parser.StuctureType(tag = tag):

                        dst = PseudoMem(dst, offset)
                        copyBytes(src, dst, typeTable[tag].size, ASM_Instructions)

                        """
                        size = typeTable[tag].size
                        while src.offset < size:

                            dif = size - src.offset
                            print("DIF:", dif)

                            bytes = None
                            type_ = None

                            if dif >= 8:
                                type_ = Quadword()
                                bytes = 8
                            elif dif >= 4:
                                type_ = Longword()
                                bytes = 4
                            else:
                                type_ = Byte()
                                bytes = 1

                            if type == None:
                                print("Error: Invalid Copy Instruction.")
                                sys.exit(1)

                            s = copy.deepcopy(src)
                            d = copy.deepcopy(dst)
                            
                            ASM_Instructions.append(MovInstruction(type_, s, d))

                            src.offset += bytes
                            dst.offset += bytes
                        """
                        
                    case _:
                        ASM_Instructions.append(MovInstruction(type1, src, PseudoMem(dst, offset)))

            case tacGenerator.TAC_returnInstruction(Value=v):

                if v == None:
                    ASM_Instructions.append(ReturnInstruction())
                    return
                
                #breakpoint()

                intRetVals, doubleRetVals, returnInMemory = classifyReturnValue(v, symbolTable, typeTable, topLevelList)


                if returnInMemory:
                    
                    ASM_Instructions.append(MovInstruction(Quadword(), MemoryOperand(Register(RegisterType.BP), -8), RegisterOperand(Register(RegisterType.AX))))

                    dst = MemoryOperand(Register(RegisterType.AX), 0)

                    assType, cType1, src = parseValue(v, symbolTable, typeTable, topLevelList)

                    copyBytes(src, dst, assType.size, ASM_Instructions)

                else:

                    funAttrs = symbolTable[parentFunName].attrs

                    intReturnRegisters = [RegisterType.AX, RegisterType.DX]
                    doubleReturnRegisters = [SSERegisterType.XMM0, SSERegisterType.XMM1]

                    for i, (t, op) in enumerate(intRetVals):
                        
                        r = intReturnRegisters[i]

                        funAttrs.returnInt.add(r)

                        match t:
                            case ByteArray(size = size, alignment = alignment):
                                copyBytesToReg(op, r, size, ASM_Instructions)

                            case _:
                                ASM_Instructions.append(MovInstruction(t, op, RegisterOperand(Register(r))))
                                

                    
                    for i, op in enumerate(doubleRetVals):
                        r = doubleReturnRegisters[i]

                        funAttrs.returnDouble.add(r)

                        ASM_Instructions.append(MovInstruction(Double(), op, RegisterOperand(Register(r))))

                
                ASM_Instructions.append(ReturnInstruction())

                """
                if v:
                    type1, cType1, src = parseValue(v, symbolTable, typeTable, topLevelList)

                    if typeChecker.isIntegerType(cType1):
                        instruction0 = MovInstruction(type1, src, RegisterOperand(Register(RegisterType.AX)))

                        instruction1 = ReturnInstruction()
                        
                        ASM_Instructions.append(instruction0)
                        ASM_Instructions.append(instruction1)
                    else:
                        
                        instruction0 = MovInstruction(Double(), src, RegisterOperand(Register(SSERegisterType.XMM0)))

                        instruction1 = ReturnInstruction()
                        
                        ASM_Instructions.append(instruction0)
                        ASM_Instructions.append(instruction1)
                else:
                    instruction0 = ReturnInstruction()    
                    ASM_Instructions.append(instruction0)
                """
                 
            case tacGenerator.TAC_UnaryInstruction(operator=o, src=src_, dst=dst_):
                
                match o:
                    case tacGenerator.TAC_UnaryOperator(operator=op):
                        match op:
                            case tacGenerator.UnopType.NOT:
                                
                                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                                if typeChecker.isIntegerType(cType1):
                                    instruction0 = CompInst(type1, ImmediateOperand(0), src)
                                    instruction1 = MovInstruction(type2, ImmediateOperand(0), dst)
                                    instruction2 = SetCCInst(ConcCodeType.E, dst)

                                    ASM_Instructions.append(instruction0)
                                    ASM_Instructions.append(instruction1)
                                    ASM_Instructions.append(instruction2)
                                else:

                                    instruction0 = BinaryInstruction(BinaryOperator(BinopType.Xor), Double(), RegisterOperand(Register(SSERegisterType.XMM0)), RegisterOperand(Register(SSERegisterType.XMM0)))
                                    
                                    #instruction0 = BinaryInstruction(BinaryOperator(BinopType.Xor), AssemblySize(AssemblyType.DOUBLE), RegisterOperand(Register(SSERegisterType.XMM0)), RegisterOperand(Register(SSERegisterType.XMM0)))
                                    
                                    instruction1 = CompInst(Double(), src, RegisterOperand(Register(SSERegisterType.XMM0)))

                                    #instruction1 = CompInst(AssemblySize(AssemblyType.DOUBLE), src, RegisterOperand(Register(SSERegisterType.XMM0)))

                                    instruction2 = MovInstruction(type2, ImmediateOperand(0), dst)

                                    instruction3 = SetCCInst(ConcCodeType.E, dst)

                                    ASM_Instructions.append(instruction0)
                                    ASM_Instructions.append(instruction1)
                                    ASM_Instructions.append(instruction2)
                                    ASM_Instructions.append(instruction3)

                            case tacGenerator.UnopType.NEGATE:
                                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                                if typeChecker.isIntegerType(cType1):
                                    parseUnaryInstructionGeneral(src_, dst_, o, symbolTable, typeTable, ASM_Instructions, topLevelList)
                                    
                                else:
                                    name = makeTemp()
                                    topLevelList.append(StaticConstant(name, 16, typeChecker.DoubleInit(-0.0)))
                                    
                                    instruction0 = MovInstruction(Double(), src, dst)
                                    
                                    instruction1 = BinaryInstruction(BinaryOperator(BinopType.Xor), Double(), DataOperand(name, 0), dst)

                                    ASM_Instructions.append(instruction0)
                                    ASM_Instructions.append(instruction1)

                                
                            case _:
                                parseUnaryInstructionGeneral(src_, dst_, o, symbolTable, typeTable, ASM_Instructions, topLevelList)


            case tacGenerator.TAC_FunCallInstruction(funName = funName, arguments = arguments, dst = dst):

                returnInMemory = False
                intDests = []
                doubleDests = []
                regIndex = 0

                if dst:
                    intDests, doubleDests, returnInMemory = classifyReturnValue(dst, symbolTable, typeTable, topLevelList)

                    print("IntDests:", intDests)
                    print("DoubleDests:", doubleDests)
                    print("ReturnInMemory:", returnInMemory)

                if returnInMemory:
                    a, b, dst_ = parseValue(dst, symbolTable, typeTable, topLevelList)
                    ASM_Instructions.append(LeaInstruction(dst_, RegisterOperand(Register(RegisterType.DI))))
                    regIndex = 1
                
                intArgs, doubleArgs, stackArgs = classifyParameters(arguments, symbolTable, typeTable, topLevelList, returnInMemory)

                print("IntArgs:", intArgs)
                print("DoubleArgs:", doubleArgs)
                print("StackArgs:", stackArgs)


                stackPadding = 0
                if len(stackArgs) % 2:
                    stackPadding = 8
                
                if stackPadding != 0:
                    
                    instruction0 = BinaryInstruction(BinaryOperator(BinopType.Sub), Quadword(), ImmediateOperand(stackPadding), RegisterOperand(Register(RegisterType.SP)))                    
                    
                    ASM_Instructions.append(instruction0)

                funAttrs = symbolTable[funName].attrs

                intRegisters = [RegisterType.DI, RegisterType.SI, RegisterType.DX, RegisterType.CX, RegisterType.R8, RegisterType.R9]

                doubleRegisters = [SSERegisterType.XMM0, SSERegisterType.XMM1, SSERegisterType.XMM2, SSERegisterType.XMM3, SSERegisterType.XMM4, SSERegisterType.XMM5, SSERegisterType.XMM6, SSERegisterType.XMM7]

                for i, (assType, assArg) in enumerate(intArgs):
                    
                    r = intRegisters[i]

                    funAttrs.paramInt.add(r)

                    match assType:
                        case ByteArray(size = size, alignment = alignment):
                            copyBytesToReg(assArg, r, size, ASM_Instructions)
                            
                        case _:
                            ASM_Instructions.append(MovInstruction(assType, assArg, RegisterOperand(Register(r))))

                
                for i, assArg in enumerate(doubleArgs):
                    r = doubleRegisters[i]

                    funAttrs.paramDouble.add(r)

                    ASM_Instructions.append(MovInstruction(Double(), assArg, RegisterOperand(Register(r))))

                stackArgs.reverse()
                
                for assType, asmArg in stackArgs:
                    
                    match assType:
                        case ByteArray(size = size, alignment = alignment):
                            #print("Ale")
                            ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Sub), Quadword(), ImmediateOperand(8), RegisterOperand(Register(RegisterType.SP))))

                            copyBytes(asmArg, MemoryOperand(Register(RegisterType.SP), 0), size, ASM_Instructions)

                        case _:
                            if type(asmArg) == ImmediateOperand or type(asmArg) == RegisterOperand or type(assType) == Quadword or type(assType) == Double:

                                #print(type(assType))

                                ASM_Instructions.append(PushInstruction(asmArg))
                                
                            else:

                                i0 = MovInstruction(assType, asmArg, RegisterOperand(Register(RegisterType.AX)))
                                
                                ASM_Instructions.append(i0)
                                ASM_Instructions.append(PushInstruction(RegisterOperand(Register(RegisterType.AX))))
                
                        
                ASM_Instructions.append(CallInstruction(funName))

                bytesToRemove = stackPadding + 8 * len(stackArgs)
                if bytesToRemove:

                    instruction0 = BinaryInstruction(BinaryOperator(BinopType.Add), Quadword(), ImmediateOperand(bytesToRemove), RegisterOperand(Register(RegisterType.SP)))
                    
                    ASM_Instructions.append(instruction0)

                if dst and not returnInMemory:
                    intReturnRegisters = [RegisterType.AX, RegisterType.DX]
                    doubleReturnRegisters = [SSERegisterType.XMM0, SSERegisterType.XMM1]

                    for i, (t, op) in enumerate(intDests):
                        #print("T:", i, t, op)

                        r = intReturnRegisters[i]

                        funAttrs.returnInt.add(r)

                        match t:
                            case ByteArray(size = size, alignment = alignment):
                                copyBytesFromReg(r, op, size, ASM_Instructions)
                                
                            case _:
                                ASM_Instructions.append(MovInstruction(t, RegisterOperand(Register(r)), op))
                        

                    for i, op in enumerate(doubleDests):
                        #print("T:", i, op)

                        r = doubleReturnRegisters[i]

                        funAttrs.returnDouble.add(r)

                        ASM_Instructions.append(MovInstruction(Double(), RegisterOperand(Register(r)), op))



            case tacGenerator.TAC_BinaryInstruction(operator=op, src1=src1_, src2=src2_, dst=dst_):
                
                if op.operator == tacGenerator.BinopType.EQUAL or op.operator == tacGenerator.BinopType.GREATERTHAN or op.operator == tacGenerator.BinopType.LESSTHAN or op.operator == tacGenerator.BinopType.GREATEROREQUAL or op.operator == tacGenerator.BinopType.LESSOREQUAL or op.operator == tacGenerator.BinopType.NOTEQUAL:
                    #print(op.operator)
                    type1, cType1, src1 = parseValue(src1_, symbolTable, typeTable, topLevelList)
                    type2, cType2, src2 = parseValue(src2_, symbolTable, typeTable, topLevelList)
                    type3, cType3, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                    print(type(cType1))

                    instruction0 = CompInst(type1, src2, src1)
                    instruction1 = MovInstruction(type3, ImmediateOperand(0), dst)

                    instruction2 = None

                    def isSigned(cType):
                        if type(cType) == parser.IntType or type(cType) == parser.LongType:                         
                            return True
                        return False

                    if isSigned(cType1) and isSigned(cType2):
                        instruction2 = SetCCInst(list(ConcCodeType)[op.operator.value], dst)
                    else:
                        instruction2 = SetCCInst(list(ConcCodeTypeUnsigned)[op.operator.value], dst)
                        
                    ASM_Instructions.append(instruction0)
                    ASM_Instructions.append(instruction1)
                    ASM_Instructions.append(instruction2)
                    
                else:
                    match op.operator:
                        case tacGenerator.BinopType.DIVIDE:
                            type1, cType1, src1 = parseValue(src1_, symbolTable, typeTable, topLevelList)
                            type2, alignment2, src2 = parseValue(src2_, symbolTable, typeTable, topLevelList)
                            type3, alignment3, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)
                            
                            #SIGNED
                            if type(cType1) == parser.IntType or type(cType1) == parser.LongType:
                                instruction0 = MovInstruction(type1, src1, RegisterOperand(Register(RegisterType.AX)))
                                instruction1 = CDQInstruction(type1)
                                instruction2 = IDivInstruction(type1, src2)
                                instruction3 = MovInstruction(type1, RegisterOperand(Register(RegisterType.AX)), dst)

                                ASM_Instructions.append(instruction0)
                                ASM_Instructions.append(instruction1)
                                ASM_Instructions.append(instruction2)
                                ASM_Instructions.append(instruction3)
                            #UNSIGNED
                            elif type(cType1) == parser.UIntType or type(cType1) == parser.ULongType:
                                instruction0 = MovInstruction(type1, src1, RegisterOperand(Register(RegisterType.AX)))
                                instruction1 = MovInstruction(type1, ImmediateOperand(0), RegisterOperand(Register(RegisterType.DX)))

                                instruction2 = DivInstruction(type1, src2)
                                instruction3 = MovInstruction(type1, RegisterOperand(Register(RegisterType.AX)), dst)

                                ASM_Instructions.append(instruction0)
                                ASM_Instructions.append(instruction1)
                                ASM_Instructions.append(instruction2)
                                ASM_Instructions.append(instruction3)
                                pass
                            elif type(cType1) == parser.DoubleType:
                                
                                Expect(type1, type2, type3)

                                instruction0 = MovInstruction(type1, src1, dst)
                                instruction1 = BinaryInstruction(BinaryOperator(BinopType.DivDouble), type1, src2, dst)
                                
                                ASM_Instructions.append(instruction0)
                                ASM_Instructions.append(instruction1)
                            
                        case tacGenerator.BinopType.REMAINDER:
                            type1, cType1, src1 = parseValue(src1_, symbolTable, typeTable, topLevelList)
                            type2, alignment2, src2 = parseValue(src2_, symbolTable, typeTable, topLevelList)
                            type3, alignment3, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                            if type(cType1) == parser.IntType or type(cType1) == parser.LongType:
                                instruction0 = MovInstruction(type1, src1, RegisterOperand(Register(RegisterType.AX)))
                                instruction1 = CDQInstruction(type1)
                                instruction2 = IDivInstruction(type1, src2)
                                instruction3 = MovInstruction(type1, RegisterOperand(Register(RegisterType.DX)), dst)

                                ASM_Instructions.append(instruction0)
                                ASM_Instructions.append(instruction1)
                                ASM_Instructions.append(instruction2)
                                ASM_Instructions.append(instruction3)

                            elif type(cType1) == parser.UIntType or type(cType1) == parser.ULongType:
                                instruction0 = MovInstruction(type1, src1, RegisterOperand(Register(RegisterType.AX)))
                                instruction1 = MovInstruction(type1, ImmediateOperand(0), RegisterOperand(Register(RegisterType.DX)))
                                instruction2 = DivInstruction(type1, src2)
                                instruction3 = MovInstruction(type1, RegisterOperand(Register(RegisterType.DX)), dst)

                                ASM_Instructions.append(instruction0)
                                ASM_Instructions.append(instruction1)
                                ASM_Instructions.append(instruction2)
                                ASM_Instructions.append(instruction3)
                                

                        case _:
                            #parseBinaryInstructionGeneral(src1_, src2_, dst_, op, symbolTable, ASM_Instructions, topLevelList)

                            type1, alignment1, src1 = parseValue(src1_, symbolTable, typeTable, topLevelList)
                            type2, alignment2, src2 = parseValue(src2_, symbolTable, typeTable, topLevelList)
                            type3, alignment3, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)
                            
                            #Expect(type1, type2, type3)

                            operator = parseOperator(op)
                                    
                            instruction0 = MovInstruction(type1, src1, dst)
                            instruction1 = BinaryInstruction(operator, type1, src2, dst)
                            
                            ASM_Instructions.append(instruction0)
                            ASM_Instructions.append(instruction1)
            
            case tacGenerator.TAC_JumpInst(label=label):
                ASM_Instructions.append(JumpInst(label))

            case tacGenerator.TAC_JumpIfZeroInst(condition=cond, label=label):
                type1, cType1, c = parseValue(cond, symbolTable, typeTable, topLevelList)

                if typeChecker.isIntegerType(cType1):
                    instruction0 = CompInst(type1, ImmediateOperand(0), c)
                    instruction1 = JumpCCInst(ConcCodeType.E, label)
                    
                    ASM_Instructions.append(instruction0)
                    ASM_Instructions.append(instruction1)
                else:
                    
                    instruction0 = BinaryInstruction(BinaryOperator(BinopType.Xor), Double(), RegisterOperand(Register(SSERegisterType.XMM0)), RegisterOperand(Register(SSERegisterType.XMM0)))

                    #instruction0 = BinaryInstruction(BinaryOperator(BinopType.Xor), AssemblySize(AssemblyType.DOUBLE), RegisterOperand(Register(SSERegisterType.XMM0)), RegisterOperand(Register(SSERegisterType.XMM0)))

                    instruction1 = CompInst(Double(), c, RegisterOperand(Register(SSERegisterType.XMM0)))

                    #instruction1 = CompInst(AssemblySize(AssemblyType.DOUBLE), c, RegisterOperand(Register(SSERegisterType.XMM0)))

                    instruction2 = JumpCCInst(ConcCodeType.E, label)
                    
                    ASM_Instructions.append(instruction0)
                    ASM_Instructions.append(instruction1)
                    ASM_Instructions.append(instruction2)

            case tacGenerator.TAC_JumpIfNotZeroInst(condition=cond, label=label):
                type1, cType1, c = parseValue(cond, symbolTable, typeTable, topLevelList)

                if typeChecker.isIntegerType(cType1):
                    instruction0 = CompInst(type1, ImmediateOperand(0), c)
                    instruction1 = JumpCCInst(ConcCodeType.NE, label)
                    
                    ASM_Instructions.append(instruction0)
                    ASM_Instructions.append(instruction1)        
                else:
                    instruction0 = BinaryInstruction(BinaryOperator(BinopType.Xor), Double(), RegisterOperand(Register(SSERegisterType.XMM0)), RegisterOperand(Register(SSERegisterType.XMM0)))

                    #instruction0 = BinaryInstruction(BinaryOperator(BinopType.Xor), AssemblySize(AssemblyType.DOUBLE), RegisterOperand(Register(SSERegisterType.XMM0)), RegisterOperand(Register(SSERegisterType.XMM0)))

                    instruction1 = CompInst(Double(), c, RegisterOperand(Register(SSERegisterType.XMM0)))
                    
                    #instruction1 = CompInst(AssemblySize(AssemblyType.DOUBLE), c, RegisterOperand(Register(SSERegisterType.XMM0)))

                    instruction2 = JumpCCInst(ConcCodeType.NE, label)
                    
                    ASM_Instructions.append(instruction0)
                    ASM_Instructions.append(instruction1)
                    ASM_Instructions.append(instruction2)
                    
            case tacGenerator.TAC_UIntToDouble(src = src_, dst = dst_):
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                if type(cType1) == parser.UCharType:
                    ASM_Instructions.append(MovZeroExtendIns(Byte(), Longword(), src, RegisterOperand(Register(RegisterType.AX))))
                    ASM_Instructions.append(Cvtsi2sd(Longword(), RegisterOperand(Register(RegisterType.AX)), dst))
                
                elif type(cType1) == parser.UIntType:
                    ASM_Instructions.append(MovZeroExtendIns(Longword(), Quadword(), src, RegisterOperand(Register(RegisterType.AX))))
                    ASM_Instructions.append(Cvtsi2sd(Quadword(), RegisterOperand(Register(RegisterType.AX)), dst))

                elif type(cType1) == parser.ULongType:
                    
                    ASM_Instructions.append(CompInst(Quadword(), ImmediateOperand(0), src))
                    
                    #ASM_Instructions.append(CompInst(AssemblySize(AssemblyType.QUADWORD), ImmediateOperand(0), src))
                    
                    label1 = makeTemp()
                    
                    label2 = makeTemp()
                    
                    ASM_Instructions.append(JumpCCInst(ConcCodeType.L, label1))
                    
                    ASM_Instructions.append(Cvtsi2sd(Quadword(), src, dst))
                    
                    #ASM_Instructions.append(Cvtsi2sd(AssemblySize(AssemblyType.QUADWORD), src, dst))
                    
                    ASM_Instructions.append(JumpInst(label2))
                    
                    ASM_Instructions.append(LabelInst(label1))
                    
                    ASM_Instructions.append(MovInstruction(Quadword(), src, RegisterOperand(Register(RegisterType.AX))))
                    
                    #ASM_Instructions.append(MovInstruction(AssemblySize(AssemblyType.QUADWORD), src, RegisterOperand(Register(RegisterType.AX))))
                    
                    ASM_Instructions.append(MovInstruction(Quadword(), RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))))

                    #ASM_Instructions.append(MovInstruction(AssemblySize(AssemblyType.QUADWORD), RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))))
                    
                    ASM_Instructions.append(UnaryInstruction(UnaryOperator(UnopType.Shr), Quadword(), RegisterOperand(Register(RegisterType.DX))))
                    
                    #ASM_Instructions.append(UnaryInstruction(UnaryOperator(UnopType.Shr), AssemblySize(AssemblyType.QUADWORD), RegisterOperand(Register(RegisterType.DX))))

                    ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.And), Quadword(), ImmediateOperand(1), RegisterOperand(Register(RegisterType.AX))))

                    ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Or), Quadword(), RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))))

                    ASM_Instructions.append(Cvtsi2sd(Quadword(), RegisterOperand(Register(RegisterType.DX)), dst))

                    ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Add), Double(), dst, dst))

                    ASM_Instructions.append(LabelInst(label2))


            case tacGenerator.TAC_DoubleToUInt(src = src_, dst = dst_):
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                if type(cType2) == parser.UCharType:
                    ASM_Instructions.append(Cvttsd2si(Longword(), src, RegisterOperand(Register(RegisterType.AX))))
                    ASM_Instructions.append(MovInstruction(Byte(), RegisterOperand(Register(RegisterType.AX)), dst))

                elif type(cType2) == parser.UIntType:
                    i0 = Cvttsd2si(Quadword(), src, RegisterOperand(Register(RegisterType.AX)))
                    i1 = MovInstruction(Longword(), RegisterOperand(Register(RegisterType.AX)), dst)

                    ASM_Instructions.append(i0)
                    ASM_Instructions.append(i1)

                    
                elif type(cType2) == parser.ULongType:
                    
                    upperBound = makeTemp()
                    topLevelList.append(StaticConstant(upperBound, 8, typeChecker.DoubleInit(9223372036854775808.0)))

                    ASM_Instructions.append(CompInst(Double(), DataOperand(upperBound, 0), src))
                    
                    label1 = makeTemp()
                    
                    label2 = makeTemp()
                    
                    ASM_Instructions.append(JumpCCInst(ConcCodeTypeUnsigned.AE, label1))
                    
                    ASM_Instructions.append(Cvttsd2si(Quadword(), src, dst))
                    
                    ASM_Instructions.append(JumpInst(label2))
                    
                    ASM_Instructions.append(LabelInst(label1))
                    
                    ASM_Instructions.append(MovInstruction(Double(), src, RegisterOperand(Register(SSERegisterType.XMM1))))

                    ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Sub), Double(), DataOperand(upperBound, 0), RegisterOperand(Register(SSERegisterType.XMM1))))
                    
                    ASM_Instructions.append(Cvttsd2si(Quadword(), RegisterOperand(Register(SSERegisterType.XMM1)), dst))

                    ASM_Instructions.append(MovInstruction(Quadword(), ImmediateOperand(9223372036854775808), RegisterOperand(Register(RegisterType.DX))))

                    ASM_Instructions.append(BinaryInstruction(BinaryOperator(BinopType.Add), Quadword(), RegisterOperand(Register(RegisterType.DX)), dst))

                    ASM_Instructions.append(LabelInst(label2))


            case tacGenerator.TAC_signExtendInstruction(src = src, dst = dst):
                type1, alignment1, src = parseValue(src, symbolTable, typeTable, topLevelList)
                type2, alignment2, dst = parseValue(dst, symbolTable, typeTable, topLevelList)

                instruction0 = MovSXInstruction(type1, type2, src, dst)

                ASM_Instructions.append(instruction0)

            case tacGenerator.TAC_truncateInstruction(src = src, dst = dst):
                type1, alignment1, src = parseValue(src, symbolTable, typeTable, topLevelList)
                type2, alignment2, dst = parseValue(dst, symbolTable, typeTable, topLevelList)

                instruction0 = MovInstruction(type2, src, dst)

                ASM_Instructions.append(instruction0)           

            

            case tacGenerator.TAC_CopyInstruction(src=src_, dst=dst_):
                #breakpoint()
                
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                match cType1:
                    case parser.StuctureType(tag = tag):

                        copyBytes(src, dst, typeTable[tag].size, ASM_Instructions)                                                
                        
                    case _:
                        instruction0 = MovInstruction(type1, src, dst)
                        ASM_Instructions.append(instruction0)
                
            case tacGenerator.TAC_LabelInst(identifier=id):
                
                ASM_Instructions.append(LabelInst(id))

            case tacGenerator.TAC_zeroExtendInstruction(src = src_, dst = dst_):
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                ASM_Instructions.append(MovZeroExtendIns(type1, type2, src, dst))

            case tacGenerator.TAC_DoubleToInt(src = src_, dst = dst_):
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)
                
                if type(cType2) == parser.IntType or type(cType2) == parser.LongType: 
                    ASM_Instructions.append(Cvttsd2si(type2, src, dst))
                elif type(cType2) == parser.CharType or type(cType2) == parser.SCharType: 
                    ASM_Instructions.append(Cvttsd2si(Longword(), src, RegisterOperand(Register(RegisterType.AX))))
                    ASM_Instructions.append(MovInstruction(Byte(), RegisterOperand(Register(RegisterType.AX)), dst))


            case tacGenerator.TAC_IntToDouble(src = src_, dst = dst_):
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                if type(cType1) == parser.IntType or type(cType1) == parser.LongType: 
                    ASM_Instructions.append(Cvtsi2sd(type1, src, dst))
                elif type(cType1) == parser.CharType or type(cType1) == parser.SCharType: 
                    ASM_Instructions.append(MovSXInstruction(Byte(), Longword(), src, RegisterOperand(Register(RegisterType.AX))))
                    ASM_Instructions.append(Cvtsi2sd(Longword(), RegisterOperand(Register(RegisterType.AX)), dst))
                

            case tacGenerator.TAC_GetAddress(src = src_, dst = dst_):
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)

                ASM_Instructions.append(LeaInstruction(src, dst))

            
            case tacGenerator.TAC_Store(src = src_, dst = dst_):
                type1, cType1, src = parseValue(src_, symbolTable, typeTable, topLevelList)

                type2, cType2, ptr = parseValue(dst_, symbolTable, typeTable, topLevelList)
                
                match cType1:
                    case parser.StuctureType(tag = tag):
                        
                        ASM_Instructions.append(MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX))))

                        ptr = MemoryOperand(Register(RegisterType.AX), 0)

                        copyBytes(src, ptr, typeTable[tag].size, ASM_Instructions)

                        """
                        size = typeTable[tag].size
                        while ptr.int < size:

                            dif = size - ptr.int
                            print("DIF:", dif)

                            bytes = None
                            type_ = None

                            if dif >= 8:
                                type_ = Quadword()
                                bytes = 8
                            elif dif >= 4:
                                type_ = Longword()
                                bytes = 4
                            else:
                                type_ = Byte()
                                bytes = 1

                            if type == None:
                                print("Error: Invalid Copy Instruction.")
                                sys.exit(1)

                            s = copy.deepcopy(src)
                            p = copy.deepcopy(ptr)
                            
                            ASM_Instructions.append(MovInstruction(type_, s, p))

                            src.offset += bytes
                            ptr.int += bytes
                        """

                    case _:
                        instruction0 = MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX)))
                        
                        instruction1 = MovInstruction(type1, src, MemoryOperand(Register(RegisterType.AX), 0))

                        ASM_Instructions.append(instruction0)
                        ASM_Instructions.append(instruction1)
                

            case tacGenerator.TAC_Load(src = src_, dst = dst_):
                #breakpoint()
                type1, cType1, ptr = parseValue(src_, symbolTable, typeTable, topLevelList)
                type2, cType2, dst = parseValue(dst_, symbolTable, typeTable, topLevelList)
                
                match cType2:
                    case parser.StuctureType(tag = tag):
                        
                        ASM_Instructions.append(MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX))))

                        src = MemoryOperand(Register(RegisterType.AX), 0)

                        copyBytes(src, dst, typeTable[tag].size, ASM_Instructions)

                        """
                        size = typeTable[tag].size

                        while src.int < size:

                            dif = size - src.int
                            print("DIF:", dif)

                            bytes = None
                            type_ = None

                            if dif >= 8:
                                type_ = Quadword()
                                bytes = 8
                            elif dif >= 4:
                                type_ = Longword()
                                bytes = 4
                            else:
                                type_ = Byte()
                                bytes = 1

                            if type == None:
                                print("Error: Invalid Copy Instruction.")
                                sys.exit(1)

                            s = copy.deepcopy(src)
                            d = copy.deepcopy(dst)
                            
                            ASM_Instructions.append(MovInstruction(type_, s, d))

                            src.int += bytes
                            dst.offset += bytes
                        """
                    
                    case _:
                        instruction0 = MovInstruction(Quadword(), ptr, RegisterOperand(Register(RegisterType.AX)))
                        
                        instruction1 = MovInstruction(type2, MemoryOperand(Register(RegisterType.AX), 0), dst)

                        ASM_Instructions.append(instruction0)
                        ASM_Instructions.append(instruction1)
                        
                

            case _:
                print("Invalid TAC Instruction. {0}".format(type(i)))
                sys.exit(1)


def ASM_parseTopLevel(topLevel, symbolTable, typeTable, topLevelList):
    match topLevel:
        case tacGenerator.StaticConstant(identifier = identifier, type = type_, staticInit = staticInit):
            alignment, other = matchCType(type_, typeTable)
            return StaticConstant(identifier, alignment, staticInit)

        case tacGenerator.StaticVariable(identifier = identifier, global_ = global_, type = type_, initList = initList):
            alignment, other = matchCType(type_, typeTable)
            return StaticVariable(identifier, global_, alignment, initList)
        
        case tacGenerator.TAC_FunctionDef(identifier = identifier, global_ = global_, params = params, instructions = instructions):
            
            funcDef = symbolTable[identifier]
            
            returnInMemory = False

            match funcDef.type:
                case parser.FunType(paramTypes = paramTypes, retType = retType):
                    
                    match retType:
                        case parser.StuctureType(tag = tag):
                            if tag in typeTable:
                                structDef = typeTable[tag]
                                if structDef.size > 16:
                                    returnInMemory = True
                                else:
                                    returnInMemory = False

                            else:
                                returnInMemory = False
                                        
                        case _:
                            returnInMemory = False
                    
                case _:
                    print("Error: Not fun type.")
                    sys.exit(1)

            intParams, doubleParams, stackParams = classifyParameters(params, symbolTable, typeTable, topLevelList, returnInMemory)

            print("IntParams:",intParams)

            ASM_Instructions = []

            funAttrs = funcDef.attrs

            intRegisters = [RegisterType.DI, RegisterType.SI, RegisterType.DX, RegisterType.CX, RegisterType.R8, RegisterType.R9]

            doubleRegisters = [SSERegisterType.XMM0, SSERegisterType.XMM1, SSERegisterType.XMM2, SSERegisterType.XMM3, SSERegisterType.XMM4, SSERegisterType.XMM5, SSERegisterType.XMM6, SSERegisterType.XMM7]

            regIndex = 0

            if returnInMemory:
                ASM_Instructions.append(MovInstruction(Quadword(), RegisterOperand(Register(RegisterType.DI)), MemoryOperand(Register(RegisterType.BP), -8)))

                regIndex = 1

            for i, (paramType, param) in enumerate(intParams):
                
                r = intRegisters[i]

                funAttrs.paramInt.add(r)

                match paramType:
                    case ByteArray(size = size, alignment = alignment):
                        copyBytesFromReg(r, param, size, ASM_Instructions)

                    case _:
                        ASM_Instructions.append(MovInstruction(paramType, RegisterOperand(Register(r)), param))
            
            for i, param in enumerate(doubleParams):
                r = doubleRegisters[i]

                funAttrs.paramDouble.add(r)

                ASM_Instructions.append(MovInstruction(Double(), RegisterOperand(Register(r)), param))
                
            offset = 16 

            for i, (paramType, param) in enumerate(stackParams):
                #print(paramType, param)

                match paramType:
                    case ByteArray(size = size, alignment = alignment):
                        copyBytes(MemoryOperand(Register(RegisterType.BP), offset), param, size, ASM_Instructions)
                    
                    case _:
                        ASM_Instructions.append(MovInstruction(paramType, MemoryOperand(Register(RegisterType.BP), offset), param))
                
                offset += 8

            ASM_parseInstructions(instructions, ASM_Instructions, symbolTable, typeTable, topLevelList, identifier)

            return Function(identifier, global_, ASM_Instructions)

        case _:
            print("Error: Invalid TAC Top Level. {0}".format(type(topLevel)))
            sys.exit(1)

class asm_symtab_entry:
    pass

class ObjEntry(asm_symtab_entry):
    def __init__(self, assType, isStatic, isConstant):
        self.assType = assType
        self.isStatic = isStatic
        self.isConstant = isConstant

    def __str__(self):
        return "AssType: {self.assType} IsStatic: {self.isStatic} IsConstant: {self.isConstant}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class FunEntry(asm_symtab_entry):
    def __init__(self, defined, returnOnStack, paramInt, paramDouble, returnInt, returnDouble):

        self.defined = defined
        self.returnOnStack = returnOnStack

        self.paramInt = paramInt 
        self.paramDouble = paramDouble
        
        #self.paramStack = []

        self.returnInt = returnInt
        self.returnDouble = returnDouble

        #self.returnStack = []

    def __str__(self):
        return "Defined: {self.defined} ReturnOnStack: {self.returnOnStack} IntParams: {self.paramInt} DoubleParams: {self.paramDouble} ReturnInt: {self.returnInt} ReturnDouble: {self.returnDouble}".format(self=self)

    def __repr__(self):
        return self.__str__()

def matchCType(cType, typeTable):
    match cType:
        case parser.IntType():
            return 4, Longword()
            return 4, AssemblySize(AssemblyType.LONGWORD)

        case parser.LongType():
            return 8, Quadword()
            return 8, AssemblySize(AssemblyType.QUADWORD)

        case parser.UIntType():
            return 4, Longword()
            return 4, AssemblySize(AssemblyType.LONGWORD)
        
        case parser.ULongType():
            return 8, Quadword()
            return 8, AssemblySize(AssemblyType.QUADWORD)

        case parser.DoubleType():
            return 8, Double()
            return 8, AssemblySize(AssemblyType.DOUBLE)
        
        case parser.PointerType():
            return 8, Quadword()
            return 8, AssemblySize(AssemblyType.QUADWORD)

        case parser.ArrayType(elementType = elementType, size = size):
            sizeArray = cType.getBaseTypeSize(0, typeTable)
            print(sizeArray)

            while type(cType) == parser.ArrayType:
                cType = cType.elementType

            alignment, other = matchCType(cType, typeTable)
             
            if sizeArray < 16:
                return alignment, ByteArray(sizeArray, alignment)                
            else:
                return 16, ByteArray(sizeArray, 16)                
        
        case parser.CharType():
            return 1, Byte()

        case parser.SCharType():
            return 1, Byte()

        case parser.UCharType():
            return 1, Byte()

        case parser.StuctureType(tag = tag):
            if tag in typeTable:
                structDef = typeTable[tag]
                return structDef.alignment, ByteArray(structDef.size, structDef.alignment)
            
            return 0, ByteArray(0,0)

        case _:
            traceback.print_stack()
            print("Error: Invalid C Type to Assembly Conversion. {0}".format(cType))
            sys.exit(1)

def ASM_parseAST(ast, symbolTable, typeTable):
    
    funcDefList = []
    for topLevel in ast.topLevelList:
        function = ASM_parseTopLevel(topLevel, symbolTable, typeTable, funcDefList)
        funcDefList.append(function)

    backendSymbolTable = {}

    for i in funcDefList:
        match i:
            case StaticConstant(identifier = identifier, alignment = alignment, staticInit = staticInit):
                #print("StaticInit:", type(staticInit))
                match staticInit:
                    case typeChecker.DoubleInit():
                        backendSymbolTable[identifier] = ObjEntry(Double(), isStatic=True, isConstant=True)

                    #case typeChecker.StringInit(string = string, nullT = nullT):
                    #    backendSymbolTable[identifier] = ObjEntry(, isStatic=True, isConstant=True)

                    #case _:
                    #    print("Invalid Static Constant.")
                    #    sys.exit(1)
                        
    #la viejita
    for name, entry in symbolTable.items():

        match entry.attrs:

            case typeChecker.FunAttributes(defined = defined, global_ = global_, paramInt = paramInt, paramDouble = paramDouble, returnInt = returnInt, returnDouble = returnDouble):

                funcDef = symbolTable[name]
                
                returnOnStack = False

                match funcDef.type:
                    case parser.FunType(paramTypes = paramTypes, retType = retType):
                        
                        match retType:
                            case parser.StuctureType(tag = tag):
                                if tag in typeTable:
                                    structDef = typeTable[tag]
                                    if structDef.size > 16:
                                        returnOnStack = True
                                    else:
                                        returnOnStack = False

                                else:
                                    returnOnStack = False
                                            
                            case _:
                                returnOnStack = False

                        #classifyParametersFromTypes(paramTypes, symbolTable, typeTable, returnOnStack)
                        
                    case _:
                        print("Error: Not fun type.")
                        sys.exit(1)

                backendSymbolTable[name] = FunEntry(defined, returnOnStack, paramInt, paramDouble, returnInt, returnDouble)
             
            case typeChecker.LocalAttributes():
                alignment, type_ = matchCType(entry.type, typeTable)
                backendSymbolTable[name] = ObjEntry(assType=type_, isStatic=False, isConstant=False)
                
            case typeChecker.StaticAttributes():
                alignment, type_ = matchCType(entry.type, typeTable)
                backendSymbolTable[name] = ObjEntry(assType=type_, isStatic=True, isConstant=False)

            case typeChecker.ConstantAttr():
                alignment, type_ = matchCType(entry.type, typeTable)
                backendSymbolTable[name] = ObjEntry(assType=type_, isStatic=True, isConstant=True)

            case _:
                print("Error: {0}".format(type(entry.attrs)))
                sys.exit(1)
    


    return Program(funcDefList), backendSymbolTable


    
                    

        
    