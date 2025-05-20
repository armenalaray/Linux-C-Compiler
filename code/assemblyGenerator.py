from enum import Enum
import tacGenerator
import sys
import parser
import typeChecker

class Program:
    
    def __init__(self, topLevelList):
        self.topLevelList = topLevelList

    def __str__(self):

        return "ASM Program: {self.topLevelList}".format(self=self)

class AssemblyType(Enum):
    LONGWORD = 1
    QUADWORD = 2
    

class AssemblySize:
    def __init__(self, type):
        self.type = type
    
    def __str__(self):
        return "{self.type}".format(self=self)

class TopLevel:
    pass

class StaticVariable(TopLevel):

    def __init__(self, identifier, global_, alignment, staticInit):
        self.identifier = identifier
        self.global_ = global_
        self.alignment = alignment
        self.staticInit = staticInit

    def __str__(self):
        return "Static Variable: Global = {self.global_} Alignment = {self.alignment} : {self.identifier} = {self.staticInit}".format(self=self)

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
    

class MovInstruction:

    def __init__(self, assType, sourceO, destO):
        self.assType = assType
        self.sourceO = sourceO
        self.destO = destO
        
    def __str__(self):
        return "Mov({self.sourceO}, {self.destO})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()

class MovSXInstruction:

    def __init__(self, sourceO, destO):
        self.sourceO = sourceO
        self.destO = destO
    

class UnaryInstruction:
    def __init__(self, operator, assType, dest):
        self.operator = operator
        self.assType = assType
        self.dest = dest
    
    def __str__(self):
        return "Unary({self.operator}, {self.dest})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class CompInst:
    def __init__(self, assType, operand0, operand1):
        self.assType = assType
        self.operand0 = operand0
        self.operand1 = operand1
    
    def __str__(self):
        return "Cmp({self.operand0}, {self.operand1})".format(self=self)
    
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
        return "Binary({self.operator}, {self.src}, {self.dest})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()

#(operator, src2, dst)

class IDivInstruction:
    def __init__(self, assType, divisor):
        self.assType = assType
        self.divisor = divisor
    
    def __str__(self):
        return "Idiv({self.divisor})".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    

class CDQInstruction:
    def __init__(self, assType):
        self.assType = assType

    def __str__(self):
        return "Cdq"
    
    
    def __repr__(self):
        return self.__str__()

"""
class AllocateStackInstruction:
    def __init__(self, offset):
        self.offset = offset
    
    def __str__(self):
        return "AllocateStack({self.offset})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()


class DeallocateStackInstruction():
    def __init__(self, offset):
        self.offset = offset

    def __str__(self):
        return "De allocate Stack({self.offset})".format(self=self)
    
    def __repr__(self):
        return self.__str__()    

"""
    
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

class PseudoRegisterOperand:

    def __init__(self, pseudo):
        self.pseudo = pseudo
    
    def __str__(self):
        return r"Pseudo({self.pseudo})".format(self=self)

class StackOperand:
    def __init__(self, offset):
        self.offset = offset

    def __str__(self):
        return r"Stack({self.offset})".format(self=self)

class DataOperand:
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "Data({self.identifier})".format(self=self)

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
    
class BinopType(Enum):
    Add = 1
    Sub = 2
    Mult = 3

class UnaryOperator:
    def __init__(self, operator):
        self.operator = operator
    
    def __str__(self):
        match self.operator:
            case UnopType.Not:
                return "Not"
            case UnopType.Neg:
                return "Neg"

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

class RegisterType(Enum):
    #These are used for registers
    DI = 0
    SI = 1
    DX = 2
    CX = 3
    R8 = 4
    R9 = 5
    AX = 6
    R10 = 7
    R11 = 8
    SP = 9


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

def parseValue(v, symbolTable):
    type = None
    alignment = 0

    match v:
        case tacGenerator.TAC_ConstantValue(const = const):

            match const:
                case parser.ConstInt():
                    type = AssemblySize(AssemblyType.LONGWORD)
                    alignment = 4
                    
                case parser.ConstLong():
                    type = AssemblySize(AssemblyType.QUADWORD)
                    alignment = 8

            return type, alignment, ImmediateOperand(const.int)
            
        case tacGenerator.TAC_VariableValue(identifier=i):

            match symbolTable[i].type:
                case parser.IntType():
                    type = AssemblySize(AssemblyType.LONGWORD)
                    alignment = 4

                case parser.LongType():
                    type = AssemblySize(AssemblyType.QUADWORD)
                    alignment = 8

            return type, alignment, PseudoRegisterOperand(i)
        
        case _:
            print("Error: Invalid Value.")
            sys.exit(1)


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
                print("Types are not equal.")
                sys.exit(1)
        other = i

def ASM_parseInstructions(TAC_Instructions, ASM_Instructions, symbolTable):

    for i in TAC_Instructions:
        match i:
            
            case tacGenerator.TAC_returnInstruction(Value=v):
                type1, alignment1, src = parseValue(v, symbolTable)

                dst = RegisterOperand(Register(RegisterType.AX))

                instruction0 = MovInstruction(type1, src, dst)
                instruction1 = ReturnInstruction()
                
                ASM_Instructions.append(instruction0)
                ASM_Instructions.append(instruction1)
                 
            case tacGenerator.TAC_UnaryInstruction(operator=o, src=src_, dst=dst_):
                
                match o:
                    case tacGenerator.TAC_UnaryOperator(operator=op):
                        match op:
                            case tacGenerator.UnopType.NOT:
                                
                                type1, alignment1, src = parseValue(src_, symbolTable)
                                type2, alignment2, dst = parseValue(dst_, symbolTable)
                                
                                instruction0 = CompInst(type1, ImmediateOperand(0), src)
                                instruction1 = MovInstruction(type2, ImmediateOperand(0), dst)
                                instruction2 = SetCCInst(ConcCodeType.E, dst)

                                ASM_Instructions.append(instruction0)
                                ASM_Instructions.append(instruction1)
                                ASM_Instructions.append(instruction2)
                                
                            case _:
                                type1, alignment1, src = parseValue(src_, symbolTable)
                                type2, alignment2, dst = parseValue(dst_, symbolTable)

                                operator = parseOperator(o)

                                instruction0 = MovInstruction(type1, src, dst)
                                instruction1 = UnaryInstruction(operator, type1, dst)
                                
                                ASM_Instructions.append(instruction0)
                                ASM_Instructions.append(instruction1)

            case tacGenerator.TAC_FunCallInstruction(funName = funName, arguments = arguments, dst = dst):
                
                registerArgs = arguments[:6]
                stackArgs = arguments[6:]

                print(registerArgs)
                print(stackArgs)

                #Alignement
                stackPadding = 0
                if len(stackArgs) % 2:
                    #is odd
                    stackPadding = 8
                
                #print("stackPadding", stackPadding)
                if stackPadding != 0:
                    instruction0 = BinaryInstruction(BinaryOperator(BinopType.Sub), AssemblySize(AssemblyType.QUADWORD), ImmediateOperand(stackPadding), RegisterOperand(Register(RegisterType.SP)))
                    
                    ASM_Instructions.append(instruction0)

                    #ASM_Instructions.append(AllocateStackInstruction(stackPadding))

                    pass
                
                for i, arg in enumerate(registerArgs):
                    #print(type(arg))
                    type1, alignment1, asmArg = parseValue(arg, symbolTable)

                    ASM_Instructions.append(MovInstruction(type1, asmArg, RegisterOperand(Register(list(RegisterType)[i]))))
                    
                stackArgs.reverse()

                #print(stackArgs)

                for arg in stackArgs:
                    type1, alignment1, asmArg = parseValue(arg, symbolTable)

                    if type(asmArg) == ImmediateOperand or type(asmArg) == RegisterOperand or type1.type == AssemblyType.QUADWORD:

                        ASM_Instructions.append(PushInstruction(asmArg))
                        
                    else:
                        i0 = MovInstruction(AssemblySize(AssemblyType.LONGWORD), asmArg, RegisterOperand(Register(RegisterType.AX)))
                        
                        ASM_Instructions.append(i0)
                        ASM_Instructions.append(PushInstruction(RegisterOperand(Register(RegisterType.AX))))
                        

                ASM_Instructions.append(CallInstruction(funName))

                bytesToRemove = stackPadding + 8 * len(stackArgs)
                if bytesToRemove:

                    instruction0 = BinaryInstruction(BinaryOperator(BinopType.Add), AssemblySize(AssemblyType.QUADWORD), ImmediateOperand(bytesToRemove), RegisterOperand(Register(RegisterType.SP)))
                    
                    ASM_Instructions.append(instruction0)

                    #ASM_Instructions.append(DeallocateStackInstruction(bytesToRemove))
                
                type1, alignment1, asmDst = parseValue(dst, symbolTable)
                
                ASM_Instructions.append(MovInstruction(type1, RegisterOperand(Register(RegisterType.AX)), asmDst))

            case tacGenerator.TAC_BinaryInstruction(operator=op, src1=src1_, src2=src2_, dst=dst_):
                
                if op.operator == tacGenerator.BinopType.EQUAL or op.operator == tacGenerator.BinopType.GREATERTHAN or op.operator == tacGenerator.BinopType.LESSTHAN or op.operator == tacGenerator.BinopType.GREATEROREQUAL or op.operator == tacGenerator.BinopType.LESSOREQUAL or op.operator == tacGenerator.BinopType.NOTEQUAL:
                    #print(op.operator)
                    type1, alignment1, src1 = parseValue(src1_, symbolTable)
                    type2, alignment2, src2 = parseValue(src2_, symbolTable)
                    type3, alignment3, dst = parseValue(dst_, symbolTable)

                    instruction0 = CompInst(type1, src2, src1)
                    instruction1 = MovInstruction(type3, ImmediateOperand(0), dst)
                    instruction2 = SetCCInst(list(ConcCodeType)[op.operator.value], dst)

                    ASM_Instructions.append(instruction0)
                    ASM_Instructions.append(instruction1)
                    ASM_Instructions.append(instruction2)
                    
                else:
                    match op.operator:
                        case tacGenerator.BinopType.DIVIDE:
                            type1, alignment1, src1 = parseValue(src1_, symbolTable)
                            type2, alignment2, src2 = parseValue(src2_, symbolTable)
                            type3, alignment3, dst = parseValue(dst_, symbolTable)

                            instruction0 = MovInstruction(type1, src1, RegisterOperand(Register(RegisterType.AX)))
                            instruction1 = CDQInstruction(type1)
                            instruction2 = IDivInstruction(type1, src2)
                            instruction3 = MovInstruction(type1, RegisterOperand(Register(RegisterType.AX)), dst)

                            ASM_Instructions.append(instruction0)
                            ASM_Instructions.append(instruction1)
                            ASM_Instructions.append(instruction2)
                            ASM_Instructions.append(instruction3)
                            
                        case tacGenerator.BinopType.REMAINDER:
                            type1, alignment1, src1 = parseValue(src1_, symbolTable)
                            type2, alignment2, src2 = parseValue(src2_, symbolTable)
                            type3, alignment3, dst = parseValue(dst_, symbolTable)

                            instruction0 = MovInstruction(type1, src1, RegisterOperand(Register(RegisterType.AX)))
                            instruction1 = CDQInstruction(type1)
                            instruction2 = IDivInstruction(type1, src2)
                            instruction3 = MovInstruction(type1, RegisterOperand(Register(RegisterType.DX)), dst)

                            ASM_Instructions.append(instruction0)
                            ASM_Instructions.append(instruction1)
                            ASM_Instructions.append(instruction2)
                            ASM_Instructions.append(instruction3)

                        case _:
                            type1, alignment1, src1 = parseValue(src1_, symbolTable)

                            #print(type1, alignment1, src1)

                            type2, alignment2, src2 = parseValue(src2_, symbolTable)

                            type3, alignment3, dst = parseValue(dst_, symbolTable)
                            
                            Expect(type1, type2, type3)

                            operator = parseOperator(op)
                                    
                            instruction0 = MovInstruction(type1, src1, dst)
                            instruction1 = BinaryInstruction(operator, type1, src2, dst)
                            
                            ASM_Instructions.append(instruction0)
                            ASM_Instructions.append(instruction1)
            
            case tacGenerator.TAC_JumpInst(label=label):
                ASM_Instructions.append(JumpInst(label))

            case tacGenerator.TAC_JumpIfZeroInst(condition=cond, label=label):
                type1, alignment1, c = parseValue(cond, symbolTable)

                instruction0 = CompInst(type1, ImmediateOperand(0), c)
                instruction1 = JumpCCInst(ConcCodeType.E, label)
                
                ASM_Instructions.append(instruction0)
                ASM_Instructions.append(instruction1)

            case tacGenerator.TAC_signExtendInstruction(src = src, dst = dst):
                type1, alignment1, src = parseValue(src, symbolTable)
                type2, alignment2, dst = parseValue(dst, symbolTable)

                instruction0 = MovSXInstruction(src, dst)

                ASM_Instructions.append(instruction0)

            case tacGenerator.TAC_truncateInstruction(src = src, dst = dst):
                type1, alignment1, src = parseValue(src, symbolTable)
                type2, alignment2, dst = parseValue(dst, symbolTable)

                instruction0 = MovInstruction(AssemblySize(AssemblyType.LONGWORD), src, dst)

                ASM_Instructions.append(instruction0)

                pass                

            case tacGenerator.TAC_JumpIfNotZeroInst(condition=cond, label=label):
                type1, alignment1, c = parseValue(cond, symbolTable)

                instruction0 = CompInst(type1, ImmediateOperand(0), c)
                instruction1 = JumpCCInst(ConcCodeType.NE, label)
                
                ASM_Instructions.append(instruction0)
                ASM_Instructions.append(instruction1)

            case tacGenerator.TAC_CopyInstruction(src=src_, dst=dst_):
                type1, alignment1, src = parseValue(src_, symbolTable)
                type2, alignment2, dst = parseValue(dst_, symbolTable)

                instruction0 = MovInstruction(type1, src, dst)

                ASM_Instructions.append(instruction0)
                
            case tacGenerator.TAC_LabelInst(identifier=id):
                
                ASM_Instructions.append(LabelInst(id))

            case _:
                print("Invalid TAC Instruction. {0}".format(type(i)))
                sys.exit(1)


def ASM_parseTopLevel(topLevel, symbolTable):
    match topLevel:
        case tacGenerator.StaticVariable(identifier = identifier, global_ = global_, type = type, init = init):
            print(identifier)
            alignment = 0
            match type:
                case parser.IntType():
                    alignment = 4

                case parser.LongType():
                    alignment = 8
                
                case _:
                    print("Invalid Type.")
                    sys.exit(1)

            return StaticVariable(identifier, global_, alignment, init)
        
        case tacGenerator.TAC_FunctionDef(identifier = identifier, global_ = global_, params = params, instructions = instructions):
            ASM_Instructions = []

            offset = 16 
            for i, param in enumerate(params):
                type = None
                match symbolTable[param].type:
                    case parser.IntType():
                        type = AssemblySize(AssemblyType.LONGWORD)

                    case parser.LongType():
                        type = AssemblySize(AssemblyType.QUADWORD)

                if type == None:
                    print("Error")
                    sys.exit(1)

                a = None
                if i > 5:
                    a = MovInstruction(type, StackOperand(offset), PseudoRegisterOperand(param))
                    offset += 8
                else:
                    a = MovInstruction(type, RegisterOperand(Register(list(RegisterType)[i])), PseudoRegisterOperand(param))

                ASM_Instructions.append(a)
                
            ASM_parseInstructions(instructions, ASM_Instructions, symbolTable)
            return Function(identifier, global_, ASM_Instructions)

class asm_symtab_entry:
    pass

class ObjEntry(asm_symtab_entry):
    def __init__(self, assType, isStatic):
        self.assType = assType
        self.isStatic = isStatic

    def __str__(self):
        return "AssType: {self.assType} IsStatic: {self.isStatic}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class FunEntry(asm_symtab_entry):
    def __init__(self, defined):
        self.defined = defined
    

def ASM_parseAST(ast, symbolTable):
    funcDefList = []
    for topLevel in ast.topLevelList:
        function = ASM_parseTopLevel(topLevel, symbolTable)
        funcDefList.append(function)

    backendSymbolTable = {}

    for name, entry in symbolTable.items():
        #print(type(entry.attrs))

        type_ = None
        match entry.type:
            case parser.IntType():
                type_ = AssemblySize(AssemblyType.LONGWORD)

            case parser.LongType():
                type_ = AssemblySize(AssemblyType.QUADWORD)

        match entry.attrs:
            case typeChecker.FunAttributes(defined = defined, global_ = global_):
                backendSymbolTable[name] = FunEntry(defined=defined)
             
            case typeChecker.LocalAttributes():
                backendSymbolTable[name] = ObjEntry(assType=type_, isStatic=False)
                
            case typeChecker.StaticAttributes():
                backendSymbolTable[name] = ObjEntry(assType=type_, isStatic=True)
                
    

    return Program(funcDefList), backendSymbolTable


    
                    

        
    