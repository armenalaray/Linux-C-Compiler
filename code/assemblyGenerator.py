from parser import Statement
from parser import ReturnStmt
from parser import Expression
from parser import Constant_Expression
from parser import Null_Expression

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
        

def parseOperand(astExpression):

    if issubclass(type(astExpression), Expression):
        if type(astExpression) == Null_Expression:
            return RegisterOperand('EAX')
        elif type(astExpression) == Constant_Expression:
            return ImmediateOperand(astExpression.intValue)
    

def parseInstructions(astStment):
    instList = []

    #breakpoint()
    if issubclass(type(astStment),Statement):
        
        if type(astStment.expression) == Constant_Expression:
            SourceOperand = parseOperand(astStment.expression)
            DestOperand = parseOperand(Null_Expression())
            instList.append(MovInstruction(SourceOperand, DestOperand))

        if type(astStment) == ReturnStmt:
            instList.append(ReturnInstruction())
    
    return instList
    

def parseFunction(astFunc):

    identifier = astFunc.iden
    insList = parseInstructions(astFunc.statement)
    return Function(identifier, insList)
    

def parseAST(ast):
    ast.function
    function = parseFunction(ast.function)
    return Program(function)
    