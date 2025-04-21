from enum import Enum
import parser

class TAC_Program:
    def __init__(self, function):
        self.function = function

class TAC_Function:
    instructions = []
    def __init__(self, identifier, instructions):
        self.identifier = identifier
        self.instructions = instructions

class instruction:
    pass

class TAC_returnInstruction(instruction):
    def __init__(self, Value):
        self.Value = Value

class TAC_UnaryInstruction(instruction):
    def __init__(self, operator, src, dst):
        self.operator = operator
        self.src = src 
        self.dst = dst   

class Value:
    pass

class TAC_ConstantValue(Value):
    def __init__(self, intValue):
        self.intValue = intValue

class TAC_VariableValue(Value):
    def __init__(self, identifier):
        self.identifier = identifier

class OperatorType(Enum):
    NEGATE = 1
    COMPLEMENT = 2

class Operator:
    pass

class TAC_UnaryOperator(Operator):
    def __init__(self, operator):
        self.operator = operator
    


global_value = 0

def makeTemp():
    global global_value
    name = "tmp.{0}".format(global_value) 
    global_value += 1
    return name
    

def TAC_parseInstructions(expression, instructions):
    
    match expression:
        case parser.Constant_Expression(intValue=c):
            return TAC_ConstantValue(c)
            

        case parser.Unary_Expression(operator=op, expression=inner):
            src = TAC_parseInstructions(inner, instructions)

            dst = TAC_VariableValue(makeTemp())
            
            instructions.append(TAC_UnaryInstruction(TAC_UnaryOperator(op.operator), src, dst))

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