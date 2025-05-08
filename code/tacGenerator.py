import sys
from enum import Enum
import parser
import semanticAnalysis

class TAC_Program:
    def __init__(self, funcDefList):
        self.funcDefList = funcDefList
    
    def __str__(self):
        return "TAC Program:{self.funcDefList}".format(self=self)

class TAC_FunctionDef:
    instructions = []
    def __init__(self, identifier, params, instructions):
        self.identifier = identifier
        self.params = params
        self.instructions = instructions

    def __str__(self):
        return "Function: {self.identifier} ({self.params}) instructions:{self.instructions}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

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

class TAC_FunCallInstruction:
    def __init__(self, funName, arguments, dst):
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
    def __init__(self, intValue):
        self.intValue = intValue
    
    def __str__(self):
        return "{self.intValue}".format(self=self)

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
                
                


        case parser.Var_Expression(identifier=id):
            return TAC_VariableValue(id)
            

        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            src = TAC_parseInstructions(exp, instructions)
            dst = TAC_parseInstructions(lvalue, instructions)
            instructions.append(TAC_CopyInstruction(src, dst))
            return dst

        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            a = []

            if argumentList:
                for exp in argumentList:
                    src = TAC_parseInstructions(exp, instructions)
                    dst = TAC_VariableValue(makeTemp())
                    instructions.append(TAC_CopyInstruction(src, dst))
                    a.append(dst)
                
            dst = TAC_VariableValue(makeTemp())
            instructions.append(TAC_FunCallInstruction(id, a, dst))
            
            return dst        

        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            cond = TAC_parseInstructions(condExp, instructions)
            c = TAC_VariableValue(makeTemp())
            #print(dst)
            instructions.append(TAC_CopyInstruction(cond, c))

            e2_label = makeTemp()
            instructions.append(TAC_JumpIfZeroInst(c, e2_label))

            #print(type(thenExp))
            thenE = TAC_parseInstructions(thenExp, instructions)

            v1 = TAC_VariableValue(makeTemp())
            instructions.append(TAC_CopyInstruction(thenE, v1))

            result = TAC_VariableValue(makeTemp())
            instructions.append(TAC_CopyInstruction(v1, result))

            end = makeTemp()
            instructions.append(TAC_JumpInst(end))

            instructions.append(TAC_LabelInst(e2_label))

            elseE = TAC_parseInstructions(elseExp, instructions)

            v2 = TAC_VariableValue(makeTemp())
            instructions.append(TAC_CopyInstruction(elseE, v2))

            instructions.append(TAC_CopyInstruction(v2, result))

            instructions.append(TAC_LabelInst(end))

            return result
            
            

    #if type(expression_) == Unary_Expression:
    #    expression_ = expression_.expression
    
def TAC_parseForInit(forInit, instructions):
    print(type(forInit))
    match forInit:
        case parser.InitExp(exp=exp):
            if exp:
                TAC_parseInstructions(exp, instructions)
            
        case parser.InitDecl(decl=decl):
            TAC_parseDeclarations(decl, instructions)
            
    

    
def TAC_parseStatement(statement, instructions, end=None):
    match statement:
        case parser.ExpressionStmt(exp=exp):
            TAC_parseInstructions(exp, instructions)

        case parser.ReturnStmt(expression=exp):
            Val = TAC_parseInstructions(exp, instructions)
            instructions.append(TAC_returnInstruction(Val))

        case parser.CompoundStatement(block=block):
            #print(block.blockItemList)
            TAC_parseBlock(block, instructions)

        case parser.BreakStatement(identifier=id):
            instructions.append(TAC_JumpInst('break_{0}'.format(id)))
             
        case parser.ContinueStatement(identifier=id):
            instructions.append(TAC_JumpInst('continue_{0}'.format(id)))

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=id):

            TAC_parseForInit(forInit, instructions)

            #jump label
            startLabel = makeTemp()
            instructions.append(TAC_LabelInst(startLabel))
            
            breakLabel = "break_{0}".format(id)

            if condExp:
                Val = TAC_parseInstructions(condExp, instructions)

                v = TAC_VariableValue(makeTemp())
                instructions.append(TAC_CopyInstruction(Val, v))

                instructions.append(TAC_JumpIfZeroInst(v, breakLabel))


            TAC_parseStatement(statement, instructions)

            continueLabel = "continue_{0}".format(id)
            instructions.append(TAC_LabelInst(continueLabel))

            if postExp:
                TAC_parseInstructions(postExp, instructions)

            instructions.append(TAC_JumpInst(startLabel))

            instructions.append(TAC_LabelInst(breakLabel))
            pass
        

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):

            startLabel = "continue_{0}".format(id)

            instructions.append(TAC_LabelInst(startLabel))

            Val = TAC_parseInstructions(condExp, instructions)

            v = TAC_VariableValue(makeTemp())
            instructions.append(TAC_CopyInstruction(Val, v))

            endLabel = "break_{0}".format(id)
            instructions.append(TAC_JumpIfZeroInst(v, endLabel))

            TAC_parseStatement(statement, instructions)

            instructions.append(TAC_JumpInst(startLabel))

            instructions.append(TAC_LabelInst(endLabel))
            

        case parser.DoWhileStatement(statement=statement, condExp=condExp, identifier=id):    
            
            startLabel = makeTemp()

            instructions.append(TAC_LabelInst(startLabel))

            TAC_parseStatement(statement, instructions)

            instructions.append(TAC_LabelInst('continue_{0}'.format(id)))

            Val = TAC_parseInstructions(condExp, instructions)

            v = TAC_VariableValue(makeTemp())
            instructions.append(TAC_CopyInstruction(Val, v))

            instructions.append(TAC_JumpIfNotZeroInst(v, startLabel))

            instructions.append(TAC_LabelInst('break_{0}'.format(id)))
            

        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            val = TAC_parseInstructions(exp, instructions)
            #print(type(val))
            c = TAC_VariableValue(makeTemp())
            ins0 = TAC_CopyInstruction(val, c)

            instructions.append(ins0)

            if end == None:
                end = makeTemp()

            if elseS:

                else_label = makeTemp()

                ins1 = TAC_JumpIfZeroInst(c, else_label)
                instructions.append(ins1)
                
                TAC_parseStatement(thenS, instructions)

                instructions.append(TAC_JumpInst(end))

                instructions.append(TAC_LabelInst(else_label))

                print(type(elseS))

                TAC_parseStatement(elseS, instructions, end)

                if type(elseS) != parser.IfStatement:
                    instructions.append(TAC_LabelInst(end))

                
            else:
                ins1 = TAC_JumpIfZeroInst(c, end)
                instructions.append(ins1)

                #aqui nunca pasa porq no tiene un else
                TAC_parseStatement(thenS, instructions, end)

                instructions.append(TAC_LabelInst(end))


            

        case parser.NullStatement():
            pass

def TAC_parseVarDeclarations(variableDecl, instructions):
    if variableDecl.exp:
        src = TAC_parseInstructions(variableDecl.exp, instructions)
        dst = TAC_VariableValue(variableDecl.identifier)
        instructions.append(TAC_CopyInstruction(src, dst))

def TAC_parseDeclarations(decl, instructions):
    match decl:
        case parser.VarDecl(variableDecl = variableDecl):
            TAC_parseVarDeclarations(variableDecl, instructions)
                    
def TAC_parseBlock(block, instructions):
    if block.blockItemList:        
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    TAC_parseDeclarations(dec, instructions)

                case parser.S(statement=statement):
                    TAC_parseStatement(statement, instructions)

def TAC_parseFunctionDefinition(functionDef):
    if functionDef.block:
        identifier = functionDef.iden

        instructions = []

        TAC_parseBlock(functionDef.block, instructions)

        Val = TAC_ConstantValue(0)
        instructions.append(TAC_returnInstruction(Val))
        
        return TAC_FunctionDef(identifier, functionDef.paramList, instructions)
        

def TAC_parseProgram(pro):
    funcDecList = []
    if pro.funcDeclList:
        for funDec in pro.funcDeclList:
            f = TAC_parseFunctionDefinition(funDec)
            if f:
                funcDecList.append(f)

    return TAC_Program(funcDecList)