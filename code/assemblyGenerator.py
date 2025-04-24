from enum import Enum
import tacGenerator
import sys

class Program:
    
    def __init__(self, function):
        self.function = function

    def __str__(self):

        return "ASM Program\n\t{self.function}".format(self=self)


class Function:

    def __init__(self, identifier, insList):
        self.identifier = identifier
        self.insList = insList

    def __str__(self):
        
        return "Function {self.identifier} instructions:\n\t\t{self.insList}".format(self=self)
        

class ReturnInstruction:

    def __init__(self):
        pass
    
    #debuggear
    def __str__(self):
        return "ret"
    
    
    def __repr__(self):
        return self.__str__()
    

class MovInstruction:

    def __init__(self, sourceO, destO):
        self.sourceO = sourceO
        self.destO = destO
        
    def __str__(self):
        return "Mov({self.sourceO}, {self.destO})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()
    

class UnaryInstruction:
    def __init__(self, operator, dest):
        self.operator = operator
        self.dest = dest
    
    def __str__(self):
        return "Unary({self.operator}, {self.dest})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()
    
class BinaryInstruction:
    def __init__(self, operator, src, dest):
        self.operator = operator
        self.src = src
        self.dest = dest
    
    def __str__(self):
        return "Binary({self.operator}, {self.src}, {self.dest})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()

#(operator, src2, dst)

class IDivInstruction:
    def __init__(self, divisor):
        self.divisor = divisor
    
    def __str__(self):
        return "Idiv({self.divisor})".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    

class CDQInstruction:
    pass

    def __str__(self):
        return "Cdq"
    
    
    def __repr__(self):
        return self.__str__()

class AllocateStackInstruction:
    def __init__(self, offset):
        self.offset = offset
    
    def __str__(self):
        return "AllocateStack({self.offset})".format(self=self)
    
    
    def __repr__(self):
        return self.__str__()

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
    AX = 1
    DX = 3
    R10 = 2
    R11 = 4

class Register:
    def __init__(self, register):
        self.register = register

    def __str__(self):
        match self.register:
            case RegisterType.AX:
                return "AX"
            case RegisterType.R10:
                return "R10d"
            case RegisterType.DX:
                return "DX"
            case RegisterType.R11:
                return "R11d"

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

            case tacGenerator.TAC_BinaryInstruction(operator=op, src1=src1_, src2=src2_, dst=dst_):
                
                
                match op.operator:
                    case tacGenerator.BinopType.DIVIDE:
                        src1 = parseValue(src1_)
                        src2 = parseValue(src2_)
                        dst = parseValue(dst_)

                        instruction0 = MovInstruction(src1, RegisterOperand(Register(RegisterType.AX)))
                        instruction1 = CDQInstruction()
                        instruction2 = IDivInstruction(src2)
                        instruction3 = MovInstruction(RegisterOperand(Register(RegisterType.AX)), dst)

                        ASM_Instructions.append(instruction0)
                        ASM_Instructions.append(instruction1)
                        ASM_Instructions.append(instruction2)
                        ASM_Instructions.append(instruction3)
                        
                    case tacGenerator.BinopType.REMAINDER:
                        src1 = parseValue(src1_)
                        src2 = parseValue(src2_)
                        dst = parseValue(dst_)

                        instruction0 = MovInstruction(src1, RegisterOperand(Register(RegisterType.AX)))
                        instruction1 = CDQInstruction()
                        instruction2 = IDivInstruction(src2)
                        instruction3 = MovInstruction(RegisterOperand(Register(RegisterType.DX)), dst)

                        ASM_Instructions.append(instruction0)
                        ASM_Instructions.append(instruction1)
                        ASM_Instructions.append(instruction2)
                        ASM_Instructions.append(instruction3)

                    case _:
                        src1 = parseValue(src1_)
                        src2 = parseValue(src2_)
                        dst = parseValue(dst_)
                        operator = parseOperator(op)

                        instruction0 = MovInstruction(src1, dst)
                        instruction1 = BinaryInstruction(operator, src2, dst)
                        
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

# Replace Pseudos #2
def ReplacePseudoRegisters(ass):
    offset = 0
    table = {}
    for i in ass.function.insList:
        #print(type(i))
        match i:
            case MovInstruction(sourceO=src, destO=dst):
                match src:
                    case PseudoRegisterOperand(pseudo=id):

                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.sourceO = StackOperand(value)
                        
                match dst:
                    case PseudoRegisterOperand(pseudo=id):
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.destO = StackOperand(value)
                        
            

            case UnaryInstruction(operator=o, dest=dst):
                match dst:
                    case PseudoRegisterOperand(pseudo=id):
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.dest = StackOperand(value)

            case BinaryInstruction(operator=op, src=src, dest=dst):
                
                match src:
                    case PseudoRegisterOperand(pseudo=id):

                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.src = StackOperand(value)
                        
                match dst:
                    case PseudoRegisterOperand(pseudo=id):
                        
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.dest = StackOperand(value)
            
            case IDivInstruction(divisor=div):  
                match div:
                    case PseudoRegisterOperand(pseudo=id):
                        
                        if table.get(id) == None:
                            offset -= 4
                            table.update({id : offset})
                            
                        value = table[id] 
                        
                        i.divisor = StackOperand(value)

    return offset

def FixingUpInstructions(ass, offset):
    ass.function.insList.insert(0,AllocateStackInstruction(-offset))
    newList = []
    oldSize = len(newList)

    for index, i in enumerate(ass.function.insList):
        
        match i:
            case MovInstruction(sourceO=src, destO=dst):
                if type(src) == StackOperand and type(dst) == StackOperand:
                    
                    i.destO = RegisterOperand(Register(RegisterType.R10))

                    instruction = MovInstruction(RegisterOperand(Register(RegisterType.R10)),dst)

                    newList.append(i)
                    newList.append(instruction)
                
            
            case IDivInstruction(divisor=div):
                match div:
                    case ImmediateOperand():
                        i.divisor = RegisterOperand(Register(RegisterType.R10))
                        instruction = MovInstruction(div, RegisterOperand(Register(RegisterType.R10)))

                        newList.append(instruction)
                        newList.append(i)
                    

            case BinaryInstruction(operator=op, src=src, dest=dst):
                
                if type(dst) == StackOperand:
                    match op:
                            case BinaryOperator(operator=o):
                                #print(o)
                                if o == BinopType.Mult:
                                    instruction0 = MovInstruction(i.dest, RegisterOperand(Register(RegisterType.R11)))

                                    instruction1 = MovInstruction(RegisterOperand(Register(RegisterType.R11)), i.dest)

                                    i.dest = RegisterOperand(Register(RegisterType.R11))



                                    newList.append(instruction0)
                                    newList.append(i)
                                    newList.append(instruction1)


                if type(src) == StackOperand and type(dst) == StackOperand:
                    match op:
                        case BinaryOperator(operator=o):
                            #print(o)
                            if o == BinopType.Sub or o == BinopType.Add:

                                instruction = MovInstruction(i.src, RegisterOperand(Register(RegisterType.R10)))

                                i.src = RegisterOperand(Register(RegisterType.R10))

                                newList.append(instruction)
                                newList.append(i)
                                
                            
        if len(newList) == oldSize:
            newList.append(i)

        oldSize = len(newList)

    ass.function.insList = newList
    
                    

        
    