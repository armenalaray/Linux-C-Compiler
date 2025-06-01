import sys
from enum import Enum
import ctypes
import parser

class Entry:
    def __init__(self, name, attrs, type, funType=None):
        self.name = name
        self.attrs = attrs
        self.type = type
        
    def __str__(self):
        return "{self.name} {self.type} {self.attrs}".format(self=self)
    
    def __repr__(self):
        return self.__str__()


class IdentifierAttributes:
    pass

class FunAttributes(IdentifierAttributes):
    def __init__(self, defined, global_):
        self.defined = defined
        self.global_ = global_
    
    def __str__(self):
        return "Defined: {self.defined} Global: {self.global_}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

 
class StaticAttributes(IdentifierAttributes):
    def __init__(self, initialVal, global_):
        self.initialVal = initialVal
        self.global_ = global_
    
    def __str__(self):
        return "InitialVal: {self.initialVal} Global: {self.global_}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class LocalAttributes(IdentifierAttributes):
    pass

class InitialValue:
    pass

class Tentative(InitialValue):
    pass

class Initial(InitialValue):
    def __init__(self, staticInit):
        self.staticInit = staticInit

    def __str__(self):
        return "{self.staticInit}".format(self=self)

class NoInitializer(InitialValue):
    pass

class StaticInit:
    pass

class IntInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_int32(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)

class LongInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_int64(int(int_))

    def __str__(self):
        return "{self.int}".format(self=self)

class UIntInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_uint32(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)


class ULongInit(StaticInit):
    def __init__(self, int_):
        self.int = ctypes.c_uint64(int(int_))
    
    def __str__(self):
        return "{self.int}".format(self=self)

class DoubleInit(StaticInit):
    def __init__(self, double):
        self.double = ctypes.c_double(double)
    
    def __str__(self):
        return "{self.double}".format(self=self)

def getCommonType(type1, type2):
    if type(type1) == type(type2):
        return type1
    
    print("Ale")

    if type(type1) == parser.DoubleType or type(type2) == parser.DoubleType:
        return parser.DoubleType()
    
    print("Type 1:\n\tIs Signed:", type1.isSigned, "Size:", type1.size)
    print("Type 2:\n\tIs Signed:", type2.isSigned, "Size:", type2.size)

    if type1.size == type2.size:
        if type1.isSigned:
            return type2
        else:
            return type1
    
    if type1.size > type2.size:
        return type1
    else:
        return type2

#se hace explicito!
def convertTo(exp, resultType):
    if type(exp.retType) == type(resultType):
        return exp
    
    #print("Ale")
    return parser.Cast_Expression(resultType, exp, resultType)

def isNullPointerConstant(exp):
    match exp:
        case parser.Constant_Expression(const = const):
            match const:
                case parser.ConstInt(int = int):
                    if int == 0:
                        return True
                    
                case parser.ConstLong(int = int):
                    if int == 0:
                        return True
                    
                case parser.ConstUInt(int = int):
                    if int == 0:
                        return True
                    
                case parser.ConstULong(int = int):
                    if int == 0:
                        return True
        
    return False


def getCommonPointerType(exp1, exp2):
    #si los dos son punteros regresas puntero

    type1 = exp1.retType
    type2 = exp2.retType

    if type(type1) == type(type2):
        return type1
    elif isNullPointerConstant(exp1):
        return type2
    elif isNullPointerConstant(exp2):
        return type1
    
    print("Error: Expressions have incompatible types.")
    sys.exit(1)
    

def isArithmeticType(targetType):
    if type(targetType) == parser.IntType or type(targetType) == parser.LongType or type(targetType) == parser.UIntType or type(targetType) == parser.ULongType or type(targetType) == parser.DoubleType:
        return True
    
    return False
    

def convertByAssignment(exp, targetType):
    expType = type(exp.retType)
    
    if expType == type(targetType):
        return exp

    if isArithmeticType(exp.retType) and isArithmeticType(targetType):
        return convertTo(exp, targetType)

    if isNullPointerConstant(exp) and type(targetType) == parser.PointerType:
        return convertTo(exp, targetType)
    
    print("Error: Cannot convert type for assignment.")
    sys.exit(1)

    

def typeCheckExpression(exp, symbolTable):
    match exp:

        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            
            ## NEW CODE
            paramCount = 0
            if argumentList:
                paramCount = len(argumentList)

            #aqui estoy buscando la declaracion de la funcion
            match symbolTable[id].type:
                case parser.FunType(paramTypes = paramTypes, retType = retType):
                    if len(paramTypes) != paramCount:
                        print("Error: Function {0}() called with the wrong number of arguments.".format(id))
                        sys.exit(1)

                    if argumentList:

                        convertedArgs = []
                        for exp, targetType in zip(argumentList, paramTypes):
                            exp = typeCheckExpression(exp, symbolTable)

                            exp = convertByAssignment(exp, targetType)

                            convertedArgs.append(exp)
                        
                        print(convertedArgs)

                        return parser.FunctionCall_Exp(id, convertedArgs, retType)
                    
                    return parser.FunctionCall_Exp(id, None, retType)
                    
                case _:
                    print("Error: Variable {0} used as function name.".format(id))
                    sys.exit(1)

        case parser.Dereference(exp = exp):
            typedInner = typeCheckExpression(exp, symbolTable)
            
            match typedInner.retType:
                case parser.PointerType(referenceType = referenceType):
                    return parser.Dereference(typedInner, referenceType)

                case _:
                    print("Error: Cannot derefence a non-pointer.")
                    sys.exit(1)

        case parser.AddrOf(exp = exp):

            if type(exp) == parser.Var_Expression or type(exp) == parser.Dereference:

                typedInner = typeCheckExpression(exp, symbolTable)
                retType = parser.PointerType(typedInner.retType)
                return parser.AddrOf(typedInner, retType)

            else:
                print("Error: Can't take the address of a non-lvalue.")
                sys.exit(1)

        case parser.Cast_Expression(targetType = targetType, exp = exp):
            e = typeCheckExpression(exp, symbolTable)
            return parser.Cast_Expression(targetType, e, targetType)

        case parser.Var_Expression(identifier = id):
            if type(symbolTable[id].type) == parser.FunType:
                print("ERROR: Function {0}() used as variable.".format(id))
                sys.exit(1)
            
            return parser.Var_Expression(id, symbolTable[id].type)
        
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            if type(lvalue) == parser.Var_Expression or type(lvalue) == parser.Dereference:

                l = typeCheckExpression(lvalue, symbolTable)
                r = typeCheckExpression(exp, symbolTable)

                r = convertByAssignment(r, l.retType)

                return parser.Assignment_Expression(l, r, l.retType)
            
            else:
                print("Error: Can't take the address of a non-lvalue.")
                sys.exit(1)

        case parser.Constant_Expression(const=const):
            #print(type(const))
            match const:
                case parser.ConstInt():
                    return parser.Constant_Expression(const, parser.IntType())
                
                ##NOTE: Lo vas a hacer despues!
                case parser.ConstLong():
                    return parser.Constant_Expression(const, parser.LongType())
                
                case parser.ConstUInt():
                    return parser.Constant_Expression(const, parser.UIntType())
                
                case parser.ConstULong():
                    return parser.Constant_Expression(const, parser.ULongType())
                
                case parser.ConstDouble():
                    return parser.Constant_Expression(const, parser.DoubleType())

                case _:
                    print("Invalid Constant Type. {0}".format(type(const)))
                    sys.exit(1)

        case parser.Unary_Expression(operator=op, expression=exp):
            e = typeCheckExpression(exp, symbolTable)
            
            match op.operator:
                case parser.UnopType.COMPLEMENT:
                    if type(e.retType) == parser.DoubleType:
                        print("Error: Can't take the bitwise complement of a double.")
                        sys.exit(1)
                    
                    return parser.Unary_Expression(op, e, e.retType)

                case parser.UnopType.NOT:
                    return parser.Unary_Expression(op, e, parser.IntType())
                    
                case _:
                    return parser.Unary_Expression(op, e, e.retType)
                          

        case parser.Binary_Expression(operator=op, left=left, right=right):
            l = typeCheckExpression(left, symbolTable)
            r = typeCheckExpression(right, symbolTable)

            match op.operator:
                case parser.BinopType.MODULO:
                    if type(l.retType) == parser.DoubleType or type(r.retType) == parser.DoubleType:
                        print("Error: Can't take the modulo of a double.")
                        sys.exit(1)

                case parser.BinopType.AND:
                    return parser.Binary_Expression(op, l, r, parser.IntType())
                case parser.BinopType.OR:
                    return parser.Binary_Expression(op, l, r, parser.IntType())
            
            commonType = None

            if type(l.retType) == parser.PointerType or type(r.retType) == parser.PointerType:
                commonType = getCommonPointerType(l, r)
            else:
                commonType = getCommonType(l.retType, r.retType)

            l = convertTo(l, commonType)
            r = convertTo(r, commonType)

            match op.operator:
                case parser.BinopType.ADD:
                    return parser.Binary_Expression(op, l, r, commonType)
                case parser.BinopType.SUBTRACT:
                    return parser.Binary_Expression(op, l, r, commonType)
                    pass
                case parser.BinopType.MULTIPLY:
                    return parser.Binary_Expression(op, l, r, commonType)
                    pass
                case parser.BinopType.MODULO:
                    return parser.Binary_Expression(op, l, r, commonType)
                    pass
                case parser.BinopType.DIVIDE:
                    return parser.Binary_Expression(op, l, r, commonType)
                    pass
                case _:
                    return parser.Binary_Expression(op, l, r, parser.IntType())

                    
        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):

            condExp = typeCheckExpression(condExp, symbolTable)
            
            thenExp = typeCheckExpression(thenExp, symbolTable)
            elseExp = typeCheckExpression(elseExp, symbolTable)

            commonType = None

            if type(thenExp.retType) == parser.PointerType or type(elseExp.retType) == parser.PointerType:
                commonType = getCommonPointerType(thenExp, elseExp)
            else:
                commonType = getCommonType(thenExp.retType, elseExp.retType)

            thenExp = convertTo(thenExp, commonType)
            elseExp = convertTo(elseExp, commonType)

            return parser.Conditional_Expression(condExp, thenExp, elseExp, commonType)

        case _:
            print("Invalid expression type. {0}".format(type(exp)))
            sys.exit(1)


def GetStaticInitializer(varType, int):
    match varType:
        case parser.IntType():
            return Initial(IntInit(int))           

        case parser.LongType():
            return Initial(LongInit(int))
        
        case parser.UIntType():
            return Initial(UIntInit(int))

        case parser.ULongType():
            return Initial(ULongInit(int))

        case parser.DoubleType():
            return Initial(DoubleInit(int))

        case parser.PointerType():
            pass

        case _:
            print("Error: Invalid Variable Type. {0}".format(varType))
            sys.exit(1)


def AnnotateExpression(varDecl):

    match varDecl.exp:
        case parser.Constant_Expression(const = const):
            match const:
                case parser.ConstLong(int = int):

                    varDecl.exp = parser.Constant_Expression(const, parser.LongType())
                    
                    exp = convertByAssignment(varDecl.exp, varDecl.varType)

                    #exp = convertTo(varDecl.exp, varDecl.varType)

                    varDecl.exp = exp
                    
                    return GetStaticInitializer(varDecl.varType, int)                            

                case parser.ConstInt(int = int):
                    
                    #No lo tiene entonces lo agrega
                    varDecl.exp = parser.Constant_Expression(const, parser.IntType())

                    exp = convertByAssignment(varDecl.exp, varDecl.varType)
                    #exp = convertTo(varDecl.exp, varDecl.varType)

                    varDecl.exp = exp

                    return GetStaticInitializer(varDecl.varType, int)

                case parser.ConstULong(int = int):
                    varDecl.exp = parser.Constant_Expression(const, parser.ULongType())
                    exp = convertByAssignment(varDecl.exp, varDecl.varType)
                    #exp = convertTo(varDecl.exp, varDecl.varType)
                    varDecl.exp = exp

                    return GetStaticInitializer(varDecl.varType, int)
                    

                case parser.ConstUInt(int = int):
                    varDecl.exp = parser.Constant_Expression(const, parser.UIntType())
                    exp = convertByAssignment(varDecl.exp, varDecl.varType)
                    #exp = convertTo(varDecl.exp, varDecl.varType)
                    varDecl.exp = exp

                    return GetStaticInitializer(varDecl.varType, int)
                
                case parser.ConstDouble(double=double):
                    varDecl.exp = parser.Constant_Expression(const, parser.DoubleType())
                    exp = convertByAssignment(varDecl.exp, varDecl.varType)
                    #exp = convertTo(varDecl.exp, varDecl.varType)
                    varDecl.exp = exp

                    return GetStaticInitializer(varDecl.varType, double)
                    

                case _:
                    print("Error: Invalid Constant. {0}".format(type(const)))
                    sys.exit(1)
        
        case _:
            print("Error: Non constant expression.")
            sys.exit(1)

def typeCheckFileScopeVarDecl(varDecl, symbolTable):

    initialValue = None

    if varDecl.exp:
        initialValue = AnnotateExpression(varDecl)

    else:
        if varDecl.storageClass.storageClass == parser.StorageType.EXTERN:
            initialValue = NoInitializer()
        else:
            initialValue = Tentative()


    global_ = True
    if varDecl.storageClass.storageClass == parser.StorageType.STATIC:
        global_ = False
    
    if varDecl.identifier in symbolTable:

        oldDecl = symbolTable[varDecl.identifier]    

        if type(oldDecl.type) == parser.FunType:
            print("Error: Function redeclared as variable.")
            sys.exit(1)
        
        if type(oldDecl.type) != type(varDecl.varType):
            print("Error: Incompatible variable declarations.")
            sys.exit(1)

        if varDecl.storageClass.storageClass == parser.StorageType.EXTERN:
            #print(type(oldDecl[1]))
            global_ = oldDecl.attrs.global_
        
        elif oldDecl.attrs.global_ != global_:
            print("Error: Conflicting Variable Linkage.")
            sys.exit(1)

        match oldDecl.attrs.initialVal:
            case Initial():
                match initialValue:
                    case Initial():
                        print("Error: Conflicting File Scope variable definitions.")
                        sys.exit(1)
                    case _:
                        initialValue = oldDecl.attrs.initialVal
            case Tentative():
                if type(initialValue) != Initial:
                    #print("Ale")
                    initialValue = Tentative()

    vattr = StaticAttributes(initialVal=initialValue, global_=global_)
    symbolTable[varDecl.identifier] = Entry(varDecl.identifier, vattr, varDecl.varType)

    return parser.VariableDecl(varDecl.identifier, varDecl.varType, varDecl.exp, varDecl.storageClass)


    

def typeCheckLocalVarDecl(varDecl, symbolTable):

    if varDecl.storageClass.storageClass == parser.StorageType.EXTERN:
        if varDecl.exp:
            print("Error: Initializer on local extern variable declaration.")
            sys.exit(1)
        
        if varDecl.identifier in symbolTable:
            oldDecl = symbolTable[varDecl.identifier]
            
            if type(oldDecl.type) == parser.FunType:
                print("Error: Function redeclared as variable.")
                sys.exit(1)

            if type(oldDecl.type) != type(varDecl.varType):
                print("Error: Incompatible local variable declarations.")
                sys.exit(1)
            
        else:
            symbolTable[varDecl.identifier] = Entry(varDecl.identifier, StaticAttributes(NoInitializer(), global_=True), varDecl.varType)

        return parser.VariableDecl(varDecl.identifier, varDecl.varType, varDecl.exp, varDecl.storageClass)
    
    elif varDecl.storageClass.storageClass == parser.StorageType.STATIC:
        
        initialValue = None
        
        if varDecl.exp:
            initialValue = AnnotateExpression(varDecl)
        else:
            initialValue = GetStaticInitializer(varDecl.varType, 0)
        
        symbolTable[varDecl.identifier] = Entry(varDecl.identifier, StaticAttributes(initialVal=initialValue, global_=False), varDecl.varType)

        return parser.VariableDecl(varDecl.identifier, varDecl.varType, varDecl.exp, varDecl.storageClass)

            
    else:
        symbolTable[varDecl.identifier] = Entry(varDecl.identifier, LocalAttributes(), varDecl.varType)
        
        if varDecl.exp:
            e = typeCheckExpression(varDecl.exp, symbolTable)
            e = convertByAssignment(e, varDecl.varType)
            #e = convertTo(e, varDecl.varType)

            return parser.VariableDecl(varDecl.identifier, varDecl.varType, e, varDecl.storageClass)
        
        return parser.VariableDecl(varDecl.identifier, varDecl.varType, None, varDecl.storageClass)


def typeCheckVarDeclaration(varDecl, symbolTable, isBlockScope):
    if isBlockScope:
        return typeCheckLocalVarDecl(varDecl, symbolTable)
    else:
        return typeCheckFileScopeVarDecl(varDecl, symbolTable)
        
        
def typeCheckDeclaration(dec, symbolTable, isBlockScope):
    match dec:
        case parser.VarDecl(variableDecl = variableDecl):
            variableDecl = typeCheckVarDeclaration(variableDecl, symbolTable, isBlockScope)
            return parser.VarDecl(variableDecl)
            
        case parser.FunDecl(funDecl = funDecl):
            funDecl = typeCheckFunctionDeclaration(funDecl, symbolTable)
            return parser.FunDecl(funDecl)

def typeCheckForInit(forInit, symbolTable):
    match forInit:
        case parser.InitDecl(varDecl = varDecl):
            if varDecl.storageClass.storageClass != parser.StorageType.NULL:
                print("Error: Invalid Storage class specifier in variable declaration in for init.")
                sys.exit(1)

            varDecl = typeCheckVarDeclaration(varDecl, symbolTable, True)
            #este esta bien
            return parser.InitDecl(varDecl)
        
        case parser.InitExp(exp=exp):
            if exp:
                exp = typeCheckExpression(exp, symbolTable)
                return parser.InitExp(exp)
            
            return parser.InitExp()

def typeCheckStatement(statement, symbolTable, functionParentName):
    match statement:
        case parser.BreakStatement():
            return parser.BreakStatement()

        case parser.ContinueStatement():
            return parser.ContinueStatement()

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement):
            f = typeCheckForInit(forInit, symbolTable)
            
            c = None
            if condExp:
                c = typeCheckExpression(condExp, symbolTable)

            p = None
            if postExp:
                p = typeCheckExpression(postExp, symbolTable)

            s = typeCheckStatement(statement, symbolTable, functionParentName)

            return parser.ForStatement(f, s, c, p)
        
        case parser.DoWhileStatement(statement=statement, condExp=condExp):
            statement = typeCheckStatement(statement, symbolTable, functionParentName)
            condExp = typeCheckExpression(condExp, symbolTable)

            return parser.DoWhileStatement(statement, condExp)

        case parser.WhileStatement(condExp=condExp, statement=statement):
            condExp = typeCheckExpression(condExp, symbolTable)
            statement = typeCheckStatement(statement, symbolTable, functionParentName)

            return parser.WhileStatement(condExp, statement)

        case parser.ExpressionStmt(exp=exp):
            e = typeCheckExpression(exp, symbolTable)
            return parser.ExpressionStmt(e)

        case parser.ReturnStmt(expression=exp):
            e = typeCheckExpression(exp, symbolTable)

            e = convertByAssignment(e, symbolTable[functionParentName].type.retType)

            #e = convertTo(e, symbolTable[functionParentName].type.retType)

            return parser.ReturnStmt(e)
            
        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            exp = typeCheckExpression(exp, symbolTable)

            thenS = typeCheckStatement(thenS, symbolTable, functionParentName)

            if elseS:
                elseS = typeCheckStatement(elseS, symbolTable, functionParentName)
                return parser.IfStatement(exp, thenS, elseS)

            return parser.IfStatement(exp, thenS)
            
        case parser.CompoundStatement(block=block):
            block = typeCheckBlock(block, symbolTable, functionParentName)
            return parser.CompoundStatement(block)

        case parser.NullStatement():
            return parser.NullStatement()
        
        case _:
            print("Error: Invalid Statement {0}".format(statement))
            sys.exit(1)


def typeCheckBlock(block, symbolTable, functionParentName):
    
    if block.blockItemList:
        
        blockItemList = []

        for item in block.blockItemList:
            match item:
                case parser.D(declaration=dec):
                    dec = typeCheckDeclaration(dec, symbolTable, True)
                    blockItemList.append(parser.D(dec))
                    
                case parser.S(statement=statement):
                    statement = typeCheckStatement(statement, symbolTable, functionParentName)
                    blockItemList.append(parser.S(statement)) 
                
        return parser.Block(blockItemList)
    
    return parser.Block()      
        
def typeCheckFunctionDeclaration(funDec, symbolTable):
    
    funType = funDec.funType
    hasBody = funDec.block != None
    alreadyDefined = False
    global_ = True
    
    if funDec.storageClass.storageClass == parser.StorageType.STATIC:
        global_ = False
    

    if funDec.iden in symbolTable:
        oldDecl = symbolTable[funDec.iden]

        if type(oldDecl.type) != parser.FunType:
            print("Error: Variable redeclared as function.")
            sys.exit(1)

        if len(oldDecl.type.paramTypes) != len(funType.paramTypes):
            print("Error: Incompatible arity in function declarations.")
            sys.exit(1)
        
        if type(oldDecl.type.retType) != type(funType.retType):
            print("Error: Incompatible return type in function declarations.")
            sys.exit(1)

        for old, new in zip(oldDecl.type.paramTypes, funType.paramTypes):
            print("Old: ", old, "New:", new)
            if type(old) != type(new):
                print("Error: Incompatible parameter types in function declarations.")
                sys.exit(1)

        alreadyDefined = oldDecl.attrs.defined

        if alreadyDefined and hasBody:
            print("Error: function is defined more than once.")
            sys.exit(1)

        if oldDecl.attrs.global_ and funDec.storageClass.storageClass == parser.StorageType.STATIC:
            print("Static function declaration follows non-static.")
            sys.exit(1)

        global_ = oldDecl.attrs.global_

    fattr = FunAttributes(defined=(alreadyDefined or hasBody), global_=global_)

    symbolTable[funDec.iden] = Entry(funDec.iden, fattr, funType)

    if hasBody:
        for paramName, paramType in zip(funDec.paramNames, funType.paramTypes):
            symbolTable[paramName] = Entry(paramName, LocalAttributes(), paramType)
        
        block = typeCheckBlock(funDec.block, symbolTable, funDec.iden)

        return parser.FunctionDecl(funDec.iden, funType, funDec.paramNames, block, funDec.storageClass)
    
    return parser.FunctionDecl(funDec.iden, funType, funDec.paramNames, None, funDec.storageClass)
    

def typeCheckProgram(pro):
    symbolTable = {}
    if pro.declList:
        declList = []
        for decl in pro.declList:
            d = typeCheckDeclaration(decl, symbolTable, False)
            declList.append(d)

        return parser.Program(declList), symbolTable
    
    return parser.Program(), symbolTable
    
