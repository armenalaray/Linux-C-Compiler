from enum import Enum
import tacGenerator
import sys

class Program:
    
    def __init__(self, function):
        self.function = function

    def __str__(self):

        return "Asm Program\n\t{self.function}".format(self=self)


class Function:

    def __init__(self, identifier, insList):
        self.identifier = identifier
        self.insList = insList

    def __str__(self):
        
        return "Function {self.identifier} instructions:\n\t\t{self.insList}".format(self=self)
        

class ReturnInstruction:

    def __init__(self):
        pass

    def __str__(self):
        return "ret"
    
    """
    def __repr__(self):
        return self.__str__()
    """

class MovInstruction:

    def __init__(self, sourceO, destO):
        self.sourceO = sourceO
        self.destO = destO
        
    def __str__(self):
        return "movl {self.sourceO}, {self.destO}".format(self=self)
    
    """
    def __repr__(self):
        return self.__str__()
    """
class UnaryInstruction:
    def __init__(self, operator, dest):
        self.operator = operator
        self.dest = dest

class PseudoRegisterOperand:

    def __init__(self, pseudo):
        self.pseudo = pseudo
    
    def __str__(self):
        return r"%eax"


class RegisterOperand:

    def __init__(self, register):
        self.register = register
    
    def __str__(self):
        return r"%eax"
    """
    
    def __repr__(self):
        return self.__str__()
    """

class ImmediateOperand:
    def __init__(self, intVal):
        self.imm = intVal

    def __str__(self):
        return r"${self.imm}".format(self=self)
    
    """
    def __repr__(self):
        return self.__str__()
    """
class OperatorType(Enum):
    Not = 1
    Neg = 2
    

class UnaryOperator:
    def __init__(self, operator):
        self.operator = operator

class RegisterType(Enum):
    AX = 1
    

class Register:
    def __init__(self, register):
        self.register = register

def parseValue(v):
    match v:
        case tacGenerator.TAC_ConstantValue(intValue=i):
            return ImmediateOperand(i)
            
        case tacGenerator.TAC_VariableValue(identifier=i):
            return PseudoRegisterOperand(i)


def parseOperator(op):
    match op:
        case tacGenerator.TAC_UnaryOperator(operator=o):
            match o:
                case tacGenerator.OperatorType.NEGATE:
                    return UnaryOperator(OperatorType.Neg)
                case tacGenerator.OperatorType.COMPLEMENT:
                    return UnaryOperator(OperatorType.Not)
                case _:
                    print("Invalid TAC operator.")
                    sys.exit(1)
            

def ASM_parseInstructions(TAC_Instructions):
    ASM_Instructions = []

    for i in TAC_Instructions:
        match i:
            case tacGenerator.TAC_returnInstruction(Value=v):
                src = parseValue(v)
                dst = RegisterOperand(Register(RegisterType.AX))
                instruction0 = MovInstruction(src, dst)
                instruction1 = ReturnInstruction()
                
                ASM_Instructions.append(instruction0)
                ASM_Instructions.append(instruction1)
                 
            case tacGenerator.TAC_UnaryInstruction(operator=o, src=src_, dst=dst_):
                src = parseValue(src_)
                dst = parseValue(dst_)
                operator = parseOperator(o)

                instruction0 = MovInstruction(src, dst)
                instruction1 = UnaryInstruction(operator, dst)
                
                ASM_Instructions.append(instruction0)
                ASM_Instructions.append(instruction1)
                
    
    return ASM_Instructions
    
def ASM_parseFunction(astFunc):
    identifier = astFunc.identifier
    instructions = ASM_parseInstructions(astFunc.instructions)
    return Function(identifier, instructions)
    

def ASM_parseAST(ast):
    ast.function
    function = ASM_parseFunction(ast.function)
    return Program(function)
    