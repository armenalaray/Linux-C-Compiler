from enum import Enum
import parser

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

class BinopType(Enum):
    ADD = 1
    SUBTRACT = 2
    MULTIPLY = 3
    DIVIDE = 4
    REMAINDER = 5

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

global_value = 0

def makeTemp():
    global global_value
    name = "tmp.{0}".format(global_value) 
    global_value += 1
    return name
    
def parseOperator(op):
    match op:
        case parser.UnaryOperator(operator=o):
            match o:
                case parser.UnopType.NEGATE:
                    return TAC_UnaryOperator(UnopType.NEGATE)
                case parser.UnopType.COMPLEMENT:
                    return TAC_UnaryOperator(UnopType.COMPLEMENT)
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
            src1 = TAC_parseInstructions(left, instructions)
            src2 = TAC_parseInstructions(right, instructions)

            dst = TAC_VariableValue(makeTemp())

            operator = parseOperator(op)

            instructions.append(TAC_BinaryInstruction(operator, src1, src2, dst))

            return dst



            

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