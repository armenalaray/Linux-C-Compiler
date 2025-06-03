import sys
from enum import Enum
import parser
import semanticAnalysis
import typeChecker

class TAC_Program:
    def __init__(self, topLevelList):
        self.topLevelList = topLevelList
    
    def __str__(self):
        return "TAC Program:{self.topLevelList}".format(self=self)

class TopLevel:
    pass

class StaticVariable(TopLevel):
    def __init__(self, identifier, global_, type, init):
        self.identifier = identifier
        self.global_ = global_
        self.type = type
        self.init = init
    
    def __str__(self):
        return "Global: {self.global_} {self.identifier} = {self.init}".format(self=self)

    def __repr__(self):
        return self.__str__()

class TAC_FunctionDef(TopLevel):
    def __init__(self, identifier, global_, params, instructions):
        self.identifier = identifier
        self.global_ = global_
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

class TAC_signExtendInstruction(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __str__(self):
        return "SignExtend {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class TAC_zeroExtendInstruction(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "ZeroExtend {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_DoubleToInt(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "DoubleToInt {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_DoubleToUInt(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "DoubleToUInt {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_IntToDouble(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "IntToDouble {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_UIntToDouble(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst
    
    def __str__(self):
        return "UIntToDouble {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()


class TAC_truncateInstruction(instruction):
    def __init__(self, src, dst):
        self.src = src
        self.dst = dst

    def __str__(self):
        return "Truncate {self.dst} = {self.src}".format(self=self)
    
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
        return "Copy {self.dst} = {self.src}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_GetAddress(instruction):
    def __init__(self, src, dst):
        self.src = src 
        self.dst = dst

    def __str__(self):
        return "{self.dst} = Get Address {self.src} ".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
class TAC_Load(instruction):
    def __init__(self, src, dst):
        self.src = src 
        self.dst = dst

    def __str__(self):
        return "{self.dst} = Load {self.src} ".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class TAC_Store(instruction):
    def __init__(self, src, dst):
        self.src = src 
        self.dst = dst
    
    def __str__(self):
        return "{self.dst} = Store {self.src} ".format(self=self)
    
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
    def __init__(self, const):
        self.const = const
    
    def __str__(self):
        return "{self.const}".format(self=self)

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
    #NOTE this are not serialized
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


class ExpResult:
    pass

class PlainOperand(ExpResult):
    def __init__(self, val):
        self.val = val
    

class DereferencedPointer(ExpResult):
    def __init__(self, val):
        self.val = val
    
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

def makeTempVariable(type, symbolTable):
    dstName = makeTemp()
    symbolTable[dstName] = typeChecker.Entry(dstName, typeChecker.LocalAttributes(), type)
    return TAC_VariableValue(dstName)

"""
def makeStaticConstant(type, symbolTable):
    dstName = makeTemp()
    symbolTable[dstName] = typeChecker.Entry(dstName, typeChecker.StaticAttributes(None, None), type)
    return dstName
"""

def CastBetweenIntegers(targetType, sourceType, result, dst, instructions):

    if type(targetType) == parser.PointerType:
        targetType = parser.ULongType()
    elif type(sourceType) == parser.PointerType:
        sourceType = parser.ULongType()

    if targetType.size == sourceType.size:
        instructions.append(TAC_CopyInstruction(result, dst))
    elif targetType.size < sourceType.size:
        instructions.append(TAC_truncateInstruction(result, dst))
    elif sourceType.isSigned:
        instructions.append(TAC_signExtendInstruction(result, dst))
    else:
        instructions.append(TAC_zeroExtendInstruction(result, dst))

def TAC_emitTackyAndConvert(exp, instructions, symbolTable):
    result = TAC_parseInstructions(exp, instructions, symbolTable)

    match result:
        case PlainOperand(val=val):
            return val
            pass
        case DereferencedPointer(val=ptr):
            tmp = makeTempVariable(exp.retType, symbolTable)
            instructions.append(TAC_Load(ptr, tmp))
            return tmp

def TAC_parseInstructions(expression, instructions, symbolTable):
    
    match expression:
        case parser.Constant_Expression(const = const):
            return PlainOperand(TAC_ConstantValue(const))
        
        case parser.Cast_Expression(targetType = targetType, exp = exp):
            result = TAC_emitTackyAndConvert(exp, instructions, symbolTable)
            
            if type(targetType) == type(exp.retType):
                return PlainOperand(result)
            
            dst = makeTempVariable(targetType, symbolTable)
            
            match exp.retType:
                case parser.DoubleType():
                    match targetType:
                        case parser.IntType():
                            instructions.append(TAC_DoubleToInt(result, dst))

                        case parser.LongType():
                            instructions.append(TAC_DoubleToInt(result, dst))

                        case parser.UIntType():
                            instructions.append(TAC_DoubleToUInt(result, dst))

                        case parser.ULongType():
                            instructions.append(TAC_DoubleToUInt(result, dst))
                        
                        case parser.PointerType():
                            pass
                    
                case parser.IntType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_IntToDouble(result, dst))
                        
                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)
                            
                
                case parser.LongType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_IntToDouble(result, dst))

                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)
                            

                case parser.UIntType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_UIntToDouble(result, dst))

                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)
                            

                case parser.ULongType():
                    match targetType:
                        case parser.DoubleType():
                            instructions.append(TAC_UIntToDouble(result, dst))
                        
                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)

                case parser.PointerType():
                    match targetType:
                        case parser.DoubleType():
                            print("Cannot cast pointer to double.")
                            sys.exit(1)

                        case _:
                            CastBetweenIntegers(targetType, exp.retType, result, dst, instructions)

                case _:
                    print("Invalid Cast Type.")
                    sys.exit(1)
                            
            return PlainOperand(dst)
            
        case parser.Unary_Expression(operator=op, expression=inner):

            #src = TAC_parseInstructions(inner, instructions, symbolTable)
            src = TAC_emitTackyAndConvert(inner, instructions, symbolTable)

            dst = makeTempVariable(expression.retType, symbolTable)

            operator = parseOperator(op)
            instructions.append(TAC_UnaryInstruction(operator, src, dst))

            return PlainOperand(dst)
        
        case parser.Binary_Expression(operator=op, left=left, right=right):
            match op:
                case parser.BinaryOperator(operator=o):
                    
                    match o:
                        case parser.BinopType.AND:
                            
                            v1 = TAC_emitTackyAndConvert(left, instructions, symbolTable)
                            #v1 = TAC_parseInstructions(left, instructions, symbolTable)
                            
                            false_label = makeTemp()

                            instructions.append(TAC_JumpIfZeroInst(v1, false_label))

                            v2 = TAC_emitTackyAndConvert(right, instructions, symbolTable)
                            #v2 = TAC_parseInstructions(right, instructions, symbolTable)

                            instructions.append(TAC_JumpIfZeroInst(v2, false_label))

                            result = makeTempVariable(expression.retType,symbolTable)

                            end = makeTemp()

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(1)), result))

                            instructions.append(TAC_JumpInst(end))

                            instructions.append(TAC_LabelInst(false_label))

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(0)), result))

                            instructions.append(TAC_LabelInst(end))

                            return PlainOperand(result)


                        case parser.BinopType.OR:
                            
                            v1 = TAC_emitTackyAndConvert(left, instructions, symbolTable)
                            #v1 = TAC_parseInstructions(left, instructions, symbolTable)
                            
                            true_label = makeTemp()

                            instructions.append(TAC_JumpIfNotZeroInst(v1, true_label))

                            v2 = TAC_emitTackyAndConvert(right, instructions, symbolTable)
                            #v2 = TAC_parseInstructions(right, instructions, symbolTable)

                            instructions.append(TAC_JumpIfNotZeroInst(v2, true_label))

                            result = makeTempVariable(expression.retType, symbolTable)
                            
                            end = makeTemp()

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(0)), result))

                            instructions.append(TAC_JumpInst(end))

                            instructions.append(TAC_LabelInst(true_label))

                            instructions.append(TAC_CopyInstruction(TAC_ConstantValue(parser.ConstInt(1)), result))

                            instructions.append(TAC_LabelInst(end))

                            return PlainOperand(result)

                        
                        case _:
                            
                            src1 = TAC_emitTackyAndConvert(left, instructions, symbolTable)
                            #src1 = TAC_parseInstructions(left, instructions, symbolTable)

                            src2 = TAC_emitTackyAndConvert(right, instructions, symbolTable)
                            #src2 = TAC_parseInstructions(right, instructions, symbolTable)

                            dst = makeTempVariable(expression.retType, symbolTable)                            

                            operator = parseOperator(op)
                            instructions.append(TAC_BinaryInstruction(operator, src1, src2, dst))

                            return PlainOperand(dst)
                            

                case parser.UnaryOperator():
                    print("Invalid operator.")
                    sys.exit(1)
                     
        case parser.Var_Expression(identifier=id):
            return PlainOperand(TAC_VariableValue(id))
            

        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            lval = TAC_parseInstructions(lvalue, instructions, symbolTable)
            rval = TAC_emitTackyAndConvert(exp, instructions, symbolTable)

            match lval:
                case PlainOperand(val=obj):
                    instructions.append(TAC_CopyInstruction(rval, obj))
                    return lval
                
                case DereferencedPointer(val=ptr):
                    instructions.append(TAC_Store(rval, ptr))
                    return PlainOperand(rval)


        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            a = []

            #retType fun()
            if argumentList:
                for exp in argumentList:
                    src = TAC_emitTackyAndConvert(exp, instructions, symbolTable)
                    #src = TAC_parseInstructions(exp, instructions, symbolTable)
                    
                    realType = None

                    match src:
                        case TAC_ConstantValue(const=const):
                            print(type(const))
                            match const:
                                case parser.ConstInt():
                                    realType = parser.IntType() 
                                    
                                case parser.ConstLong():
                                    realType = parser.LongType()

                                case parser.ConstULong():
                                    realType = parser.ULongType()

                                case parser.ConstUInt():
                                    realType = parser.UIntType()
                                
                                case parser.ConstDouble():
                                    realType = parser.DoubleType()

                                case _:
                                    print("Invalid TAC argument type. {0}".format(type(const)))
                                    sys.exit(1)
                                            
                        case TAC_VariableValue(identifier=iden):
                            realType = symbolTable[iden].type

                        case _:
                            print("Invalid TAC Value.")
                            sys.exit(1)
                    
                    dst = makeTempVariable(realType, symbolTable)
                            
                    instructions.append(TAC_CopyInstruction(src, dst))
                    a.append(dst)
                
            dst = makeTempVariable(expression.retType, symbolTable)
            
            instructions.append(TAC_FunCallInstruction(id, a, dst))
            
            return PlainOperand(dst)

        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            cond = TAC_emitTackyAndConvert(condExp, instructions, symbolTable)
            #cond = TAC_parseInstructions(condExp, instructions, symbolTable)

            c = makeTempVariable(expression.retType, symbolTable)
            
            instructions.append(TAC_CopyInstruction(cond, c))

            e2_label = makeTemp()
            instructions.append(TAC_JumpIfZeroInst(c, e2_label))

            thenE = TAC_emitTackyAndConvert(thenExp, instructions, symbolTable)
            #thenE = TAC_parseInstructions(thenExp, instructions, symbolTable)

            v1 = makeTempVariable(expression.retType, symbolTable)
            
            instructions.append(TAC_CopyInstruction(thenE, v1))

            result = makeTempVariable(expression.retType, symbolTable)
            
            instructions.append(TAC_CopyInstruction(v1, result))

            end = makeTemp()
            instructions.append(TAC_JumpInst(end))

            instructions.append(TAC_LabelInst(e2_label))

            elseE = TAC_emitTackyAndConvert(elseExp, instructions, symbolTable)
            #elseE = TAC_parseInstructions(elseExp, instructions, symbolTable)
            
            v2 = makeTempVariable(expression.retType, symbolTable)
            
            instructions.append(TAC_CopyInstruction(elseE, v2))

            instructions.append(TAC_CopyInstruction(v2, result))

            instructions.append(TAC_LabelInst(end))

            return PlainOperand(result)
        
        case parser.AddrOf(exp = exp):
            
            v = TAC_parseInstructions(exp, instructions, symbolTable)

            match v:
                case PlainOperand(val=obj):
                    dst = makeTempVariable(expression.retType, symbolTable)
                    instructions.append(TAC_GetAddress(obj, dst))
                    return PlainOperand(dst)
                
                case DereferencedPointer(val=ptr):
                    return PlainOperand(ptr)
                    

        case parser.Dereference(exp=exp):
            dst = TAC_emitTackyAndConvert(exp, instructions, symbolTable)
            return DereferencedPointer(dst)

        case _:
            print("Invalid Expression. {0}".format(type(expression)))
            sys.exit(1)           
    
def TAC_parseForInit(forInit, instructions, symbolTable):
    match forInit:
        case parser.InitExp(exp=exp):
            if exp:
                TAC_emitTackyAndConvert(exp, instructions, symbolTable)
                #TAC_parseInstructions(exp, instructions, symbolTable)
            
        case parser.InitDecl(varDecl=varDecl):
            TAC_parseVarDeclarations(varDecl, instructions, symbolTable)

        case _:
            print("Invalid For init")
            sys.exit(1)
            
    

    
def TAC_parseStatement(statement, instructions, symbolTable, end=None):
    match statement:
        case parser.ExpressionStmt(exp=exp):
            TAC_emitTackyAndConvert(exp, instructions, symbolTable)
            #TAC_parseInstructions(exp, instructions, symbolTable)

        case parser.ReturnStmt(expression=exp):
            Val = TAC_emitTackyAndConvert(exp, instructions, symbolTable)
            #Val = TAC_parseInstructions(exp, instructions, symbolTable)
            instructions.append(TAC_returnInstruction(Val))

        case parser.CompoundStatement(block=block):
            #print(block.blockItemList)
            TAC_parseBlock(block, instructions, symbolTable)

        case parser.BreakStatement(identifier=id):
            instructions.append(TAC_JumpInst('break_{0}'.format(id)))
             
        case parser.ContinueStatement(identifier=id):
            instructions.append(TAC_JumpInst('continue_{0}'.format(id)))

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=id):
            #print(forInit)
            TAC_parseForInit(forInit, instructions, symbolTable)
            
            #print(instructions)

            #jump label
            startLabel = makeTemp()
            instructions.append(TAC_LabelInst(startLabel))
            
            
            breakLabel = "break_{0}".format(id)

            if condExp:
                Val = TAC_emitTackyAndConvert(condExp, instructions, symbolTable)
                #Val = TAC_parseInstructions(condExp, instructions, symbolTable)

                v = makeTempVariable(condExp.retType, symbolTable)
                instructions.append(TAC_CopyInstruction(Val, v))

                instructions.append(TAC_JumpIfZeroInst(v, breakLabel))


            TAC_parseStatement(statement, instructions, symbolTable)

            continueLabel = "continue_{0}".format(id)
            instructions.append(TAC_LabelInst(continueLabel))

            if postExp:
                TAC_emitTackyAndConvert(postExp, instructions, symbolTable)
                #TAC_parseInstructions(postExp, instructions, symbolTable)

            instructions.append(TAC_JumpInst(startLabel))

            instructions.append(TAC_LabelInst(breakLabel))
            
        

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):

            startLabel = "continue_{0}".format(id)

            instructions.append(TAC_LabelInst(startLabel))

            Val = TAC_emitTackyAndConvert(condExp, instructions, symbolTable)
            #Val = TAC_parseInstructions(condExp, instructions, symbolTable)

            v = makeTempVariable(condExp.retType, symbolTable)

            instructions.append(TAC_CopyInstruction(Val, v))

            endLabel = "break_{0}".format(id)
            instructions.append(TAC_JumpIfZeroInst(v, endLabel))

            TAC_parseStatement(statement, instructions, symbolTable)

            instructions.append(TAC_JumpInst(startLabel))

            instructions.append(TAC_LabelInst(endLabel))
            

        case parser.DoWhileStatement(statement=statement, condExp=condExp, identifier=id):    
            
            startLabel = makeTemp()

            instructions.append(TAC_LabelInst(startLabel))

            TAC_parseStatement(statement, instructions, symbolTable)

            instructions.append(TAC_LabelInst('continue_{0}'.format(id)))

            Val = TAC_emitTackyAndConvert(condExp, instructions, symbolTable)
            #Val = TAC_parseInstructions(condExp, instructions, symbolTable)

            v = makeTempVariable(condExp.retType, symbolTable)
            
            instructions.append(TAC_CopyInstruction(Val, v))

            instructions.append(TAC_JumpIfNotZeroInst(v, startLabel))

            instructions.append(TAC_LabelInst('break_{0}'.format(id)))
            

        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            val = TAC_emitTackyAndConvert(exp, instructions, symbolTable)
            #val = TAC_parseInstructions(exp, instructions, symbolTable)

            #print(type(val))
            c = makeTempVariable(exp.retType, symbolTable)
            
            ins0 = TAC_CopyInstruction(val, c)

            instructions.append(ins0)

            if end == None:
                end = makeTemp()

            if elseS:

                else_label = makeTemp()

                ins1 = TAC_JumpIfZeroInst(c, else_label)
                instructions.append(ins1)
                
                TAC_parseStatement(thenS, instructions, symbolTable)

                instructions.append(TAC_JumpInst(end))

                instructions.append(TAC_LabelInst(else_label))

                #print(type(elseS))

                TAC_parseStatement(elseS, instructions, symbolTable, end)

                if type(elseS) != parser.IfStatement:
                    instructions.append(TAC_LabelInst(end))

                
            else:
                ins1 = TAC_JumpIfZeroInst(c, end)
                instructions.append(ins1)

                #aqui nunca pasa porq no tiene un else
                TAC_parseStatement(thenS, instructions, symbolTable, end)

                instructions.append(TAC_LabelInst(end))


            

        case parser.NullStatement():
            pass

        case _:
            print("Invalid Statement")
            sys.exit(1)

def TAC_parseVarDeclarations(variableDecl, instructions, symbolTable):

    if variableDecl.storageClass.storageClass != parser.StorageType.NULL:
        pass
    else:
        if variableDecl.exp:
            
            src = TAC_emitTackyAndConvert(variableDecl.exp, instructions, symbolTable)

            #src = TAC_parseInstructions(variableDecl.exp, instructions, symbolTable)

            dst = TAC_VariableValue(variableDecl.identifier)
            instructions.append(TAC_CopyInstruction(src, dst))
            print(dst)

def TAC_parseDeclarations(decl, instructions, symbolTable):
    match decl:
        case parser.VarDecl(variableDecl = variableDecl):
            TAC_parseVarDeclarations(variableDecl, instructions, symbolTable)
                    
def TAC_parseBlock(block, instructions, symbolTable):
    if block.blockItemList:        
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    TAC_parseDeclarations(dec, instructions, symbolTable)

                case parser.S(statement=statement):
                    TAC_parseStatement(statement, instructions, symbolTable)

def TAC_parseFunctionDefinition(functionDef, symbolTable):
    if functionDef.block:
        identifier = functionDef.iden

        instructions = []

        TAC_parseBlock(functionDef.block, instructions, symbolTable)
        
        Val = TAC_ConstantValue(parser.ConstInt(0))
        instructions.append(TAC_returnInstruction(Val))
        
        if functionDef.iden in symbolTable:
            decl = symbolTable[functionDef.iden]
            #print(decl[2].global_)
            global_ = decl.attrs.global_
            return TAC_FunctionDef(identifier, global_, functionDef.paramNames, instructions)

        print("ERROR: function is not in symbol table.")
        sys.exit(1)

def TAC_parseTopLevel(decl, symbolTable):
    match decl:
        case parser.VarDecl(variableDecl = variableDecl):
            pass

        case parser.FunDecl(funDecl = funDecl):
            return TAC_parseFunctionDefinition(funDecl, symbolTable)


def TAC_convertSymbolsToTAC(symbolTable):
    tacDefs = []
    for name, entry in symbolTable.items():
        #print(type(entry.attrs))
        match entry.attrs:
            case typeChecker.StaticAttributes(initialVal = initialVal, global_ = global_):
                #print(type(initialVal))
                match initialVal:
                    case typeChecker.Tentative():
                        #print(type(entry.type))
                        
                        init = None
                        match entry.type:
                            case parser.IntType():
                                init = typeChecker.IntInit(0)
                                
                            case parser.LongType():
                                init = typeChecker.LongInit(0)
                            
                            case parser.UIntType():
                                init = typeChecker.UIntInit(0)
                            
                            case parser.ULongType():
                                init = typeChecker.ULongInit(0)

                            case parser.DoubleType():
                                init = typeChecker.DoubleInit(0)
                                
                            case _:
                                print("Error: Invalid Tentative Initializer. {0}".format(entry.type))
                                sys.exit(1)
                                
                                    
                        tacDefs.append(StaticVariable(name, global_, entry.type, init))

                    case typeChecker.Initial(staticInit=staticInit):
                        tacDefs.append(StaticVariable(name, global_, entry.type, staticInit))
                    
                    case _:
                        print("Invalid")
                        sys.exit(1)

    #print(tacDefs)
    return tacDefs 
                
def TAC_parseProgram(pro, symbolTable):
    topLevelList = []
    if pro.declList:
        for decl in pro.declList:
            topLevel = TAC_parseTopLevel(decl, symbolTable)
            if topLevel:
                topLevelList.append(topLevel)

    ast = TAC_Program(topLevelList)
    tacDefs = TAC_convertSymbolsToTAC(symbolTable)

    ast.topLevelList.extend(tacDefs)

    return ast

    