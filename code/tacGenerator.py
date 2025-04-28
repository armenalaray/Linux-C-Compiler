import sys
from enum import Enum
import parser
import semanticAnalysis
#from semanticAnalysis import global_value

class TAC_Program:
    def __init__(self, function):
        self.function = function
    
    def __str__(self):
        return "TAC Program:\n\t{self.function}".format(self=self)

class TAC_Function:
    instructions = []
    def __init__(self, identifier, instructions):
        self.identifier = identifier
        self.instructions = instructions

    def __str__(self):
        return "Function: {self.identifier} instructions:\n\t\t{self.instructions}".format(self=self)
        
class instruction:
    pass

class TAC_returnInstruction(instruction):
    def __init__(self, Value):
        self.Value = Value
    
    def __str__(self):
        return "Return {self.Value}".format(self=self)
    
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
        return "{self.dst} = {self.src}".format(self=self)
    
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

#(operator, src1, src2, dst)

class Value:
    pass

class TAC_ConstantValue(Value):
    def __init__(self, intValue):
        self.intValue = intValue
    
    def __str__(self):
        return "{self.intValue}".format(self=self)

class TAC_VariableValue(Value):
    def __init__(self, identifier):
        self.identifier = identifier

    def __str__(self):
        return "{self.identifier}".format(self=self)
    
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

def TAC_parseInstructions(expression, instructions):
    
    match expression:
        case parser.Constant_Expression(intValue=c):
            return TAC_ConstantValue(c)
            

        case parser.Unary_Expression(operator=op, expression=inner):
            src = TAC_parseInstructions(inner, instructions)

            dst = TAC_VariableValue(makeTemp())
            operator = parseOperator(op)
            instructions.append(TAC_UnaryInstruction(operator, src, dst))

            return dst
        
        case parser.Binary_Expression(operator=op, left=left, right=right):
            #print(op)
            match op:
                case parser.BinaryOperator(operator=o):
                    
                    match o:
                        case parser.BinopType.AND:
                            
                            v1 = TAC_parseInstructions(left, instructions)
                            
                            false_label = makeTemp()

                            instructions.append(TAC_JumpIfZeroInst(v1, false_label))
                            v2 = TAC_parseInstructions(right, instructions)
                            instructions.append(TAC_JumpIfZeroInst(v2, false_label))

                            result = TAC_VariableValue(makeTemp())
                            end = makeTemp()

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(1), result))

                            instructions.append(TAC_JumpInst(end))

                            instructions.append(TAC_LabelInst(false_label))

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(0), result))


                            instructions.append(TAC_LabelInst(end))

                            return result


                        case parser.BinopType.OR:
                            
                            v1 = TAC_parseInstructions(left, instructions)
                            
                            true_label = makeTemp()

                            instructions.append(TAC_JumpIfNotZeroInst(v1, true_label))
                            v2 = TAC_parseInstructions(right, instructions)
                            instructions.append(TAC_JumpIfNotZeroInst(v2, true_label))

                            result = TAC_VariableValue(makeTemp())
                            end = makeTemp()

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(0), result))

                            instructions.append(TAC_JumpInst(end))

                            instructions.append(TAC_LabelInst(true_label))

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(1), result))


                            instructions.append(TAC_LabelInst(end))

                            return result

                        
                        case _:
                            
                            src1 = TAC_parseInstructions(left, instructions)
                            src2 = TAC_parseInstructions(right, instructions)

                            dst = TAC_VariableValue(makeTemp())

                            operator = parseOperator(op)

                            instructions.append(TAC_BinaryInstruction(operator, src1, src2, dst))

                            return dst
                            

                case parser.UnaryOperator():
                    print("Invalid operator.")
                    sys.exit(1)



            

    #if type(expression_) == Unary_Expression:
    #    expression_ = expression_.expression
    
    
def TAC_parseStatement(statement):
    instructions = []

    if type(statement) == parser.ReturnStmt:
        Val = TAC_parseInstructions(statement.expression, instructions)

        instructions.append(TAC_returnInstruction(Val))

    return instructions

def TAC_parseFunction(function):
    identifier = function.iden
    instructions = TAC_parseStatement(function.statement)
    return TAC_Function(identifier, instructions)
    

def TAC_parseProgram(AST_Program):
    function = TAC_parseFunction(AST_Program.function)
    return TAC_Program(function)