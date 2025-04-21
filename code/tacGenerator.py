
class Program:
    def __init__(self, function):
        self.function = function

class Function:
    instructions = []
    def __init__(self, identifier, instructions):
        self.identifier = identifier
        self.instructions = instructions

def parseInstructions(expression):
    instructions = []

    

    return instructions


def parseFunction(function):
    identifier = function.iden
    instructions = parseInstructions(function.statement.expression)
    return Function(identifier, instructions)
    

def parseProgram(AST_Program):
    function = parseFunction(AST_Program.function)
    return Program(function)