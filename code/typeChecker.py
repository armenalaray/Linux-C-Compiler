import sys
from enum import Enum

import parser

class IDType(Enum):
    FUNCTION = 1
    INT = 2

class FunType:
    def __init__(self, paramCount):
        self.paramCount = paramCount
    
    def __ne__(self, value):
        #print(self, value)
        result = self.paramCount != value.paramCount
        #print(result)
        return result
    
    def __str__(self):
        return "FunType(int {self.paramCount})".format(self=self)
    
    def __repr__(self):
        return self.__str__()

class Entry:
    def __init__(self, name, attrs, type, funType=None):
        self.name = name
        self.attrs = attrs
        self.type = type
        self.funType = funType
    
    def __str__(self):
        return "{self.type} {self.name} = {self.attrs} {self.funType}".format(self=self)

#TODO: Change the entry in symboltable into entry class

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
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "{self.value}".format(self=self)

class NoInitializer(InitialValue):
    pass

def typeCheckExpression(exp, symbolTable):
    match exp:
        case parser.FunctionCall_Exp(identifier=id, argumentList = argumentList):
            
            if symbolTable[id].type == IDType.INT:
                print("Error: Variable {0} used as function name.".format(id))
                sys.exit(1)

            #es una funcion, parametrizaje
            paramCount = 0
            if argumentList:
                paramCount = len(argumentList)

            if symbolTable[id].funType.paramCount != paramCount:
                #print(paramCount)
                print("Error: Function {0}() called with the wrong number of arguments.".format(id))
                sys.exit(1)
            
            if argumentList:
                for exp in argumentList:
                    typeCheckExpression(exp, symbolTable)
                    

        case parser.Var_Expression(identifier=id):
            if symbolTable[id].type != IDType.INT:
                #symbolTable[id][1]
                print("ERROR: Function {0}() used as variable.".format(id))
                sys.exit(1)
        
        case parser.Assignment_Expression(lvalue=lvalue, exp=exp):
            typeCheckExpression(lvalue, symbolTable)
            typeCheckExpression(exp, symbolTable)

        case parser.Constant_Expression(intValue=intValue):
            pass 

        case parser.Unary_Expression(operator=op, expression=exp):
            typeCheckExpression(exp, symbolTable)
                          

        case parser.Binary_Expression(operator=op, left=left, right=right):
            typeCheckExpression(left, symbolTable)
            typeCheckExpression(right, symbolTable)


        case parser.Conditional_Expression(condExp=condExp, thenExp=thenExp, elseExp=elseExp):
            typeCheckExpression(condExp, symbolTable)
            typeCheckExpression(thenExp, symbolTable)
            typeCheckExpression(elseExp, symbolTable)

        case _:
            print(type(exp))
            print("Invalid expression type.")
            sys.exit(1)


def typeCheckFileScopeVarDecl(varDecl, symbolTable):

    initialValue = None

    if varDecl.exp:
        match varDecl.exp:
            case parser.Constant_Expression(intValue = intValue):
                
                #print(intValue)

                initialValue = Initial(intValue)
            
            case _:
                print("Error: Non constant initializer.")
                sys.exit(1)
    else:
        #print(varDecl.storageClass)
        if varDecl.storageClass[1] == parser.StorageType.EXTERN:
            initialValue = NoInitializer()
        
        else:
            initialValue = Tentative()
            pass

    #print(initialValue)                   

    global_ = True
    if varDecl.storageClass[1] and varDecl.storageClass[1] == parser.StorageType.STATIC:
        global_ = False


    #print(global_)
    
    if varDecl.identifier in symbolTable:
        #print(varDecl.identifier)

        oldDecl = symbolTable[varDecl.identifier]    

        if oldDecl.type != IDType.INT:
            print("Error: Function redeclared as variable.")
            sys.exit(1)
        
        if varDecl.storageClass[1] == parser.StorageType.EXTERN:
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


    #print(initialValue)

    vattr = StaticAttributes(initialVal=initialValue, global_=global_)

    symbolTable[varDecl.identifier] = Entry(varDecl.identifier, vattr, IDType.INT)
    

def typeCheckLocalVarDecl(varDecl, symbolTable):
    if varDecl.storageClass[1] == parser.StorageType.EXTERN:
        if varDecl.exp:
            print("Error: Initializer on local extern variable declaration.")
            sys.exit(1)
        
        if varDecl.identifier in symbolTable:
            oldDecl = symbolTable[varDecl.identifier]
            #print(varDecl.identifier, oldDecl)

            if oldDecl.type != IDType.INT:
                print("Error: Function redeclared as variable.")
                sys.exit(1)
                
        else:
            #print("Ale")
            symbolTable[varDecl.identifier] = Entry(varDecl.identifier, StaticAttributes(NoInitializer(), global_=True), IDType.INT)
            
    
    elif varDecl.storageClass[1] == parser.StorageType.STATIC:
        initialValue = None
        if varDecl.exp:
            match varDecl.exp:
                case parser.Constant_Expression(intValue = intValue):
                    initialValue = Initial(intValue)
                case _:
                    print("Error: Non constant initializer on local static variable.")
                    sys.exit(1)
                    
        else:
            initialValue = Initial("0")
        
        symbolTable[varDecl.identifier] = Entry(varDecl.identifier, StaticAttributes(initialVal=initialValue, global_=False), IDType.INT)
            

        #print(initialValue)
    else:
        symbolTable[varDecl.identifier] = Entry(varDecl.identifier, LocalAttributes(), IDType.INT)
        
        if varDecl.exp:
            typeCheckExpression(varDecl.exp, symbolTable)


def typeCheckVarDeclaration(varDecl, symbolTable, isBlockScope):
    if isBlockScope:
        typeCheckLocalVarDecl(varDecl, symbolTable)
    else:
        typeCheckFileScopeVarDecl(varDecl, symbolTable)
        
        
def typeCheckDeclaration(dec, symbolTable, isBlockScope):
    match dec:
        case parser.VarDecl(variableDecl = variableDecl):
            typeCheckVarDeclaration(variableDecl, symbolTable, isBlockScope)
            
        case parser.FunDecl(funDecl = funDecl):
            typeCheckFunctionDeclaration(funDecl, symbolTable)

def typeCheckForInit(forInit, symbolTable):
    match forInit:
        case parser.InitDecl(varDecl = varDecl):
            if varDecl.storageClass[1]:
                print("Error: Invalid Storage class specifier in variable declaration in for init.")
                sys.exit(1)

            typeCheckVarDeclaration(varDecl, symbolTable, True)
        
        case parser.InitExp(exp=exp):
            if exp:
                typeCheckExpression(exp, symbolTable)

def typeCheckStatement(statement, symbolTable):
    match statement:
        case parser.BreakStatement():
            pass

        case parser.ContinueStatement():
            pass

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=identifier):
            typeCheckForInit(forInit, symbolTable)
            
            if condExp:
                typeCheckExpression(condExp, symbolTable)

            if postExp:
                typeCheckExpression(postExp, symbolTable)

            typeCheckStatement(statement, symbolTable)
        
        case parser.DoWhileStatement(statement=statement, condExp=condExp, identifier=id):
            typeCheckStatement(statement, symbolTable)
            typeCheckExpression(condExp, symbolTable)

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):
            typeCheckExpression(condExp, symbolTable)
            typeCheckStatement(statement, symbolTable)

        case parser.ExpressionStmt(exp=exp):
            typeCheckExpression(exp, symbolTable)
            

        case parser.ReturnStmt(expression=exp):
            typeCheckExpression(exp, symbolTable)
            
        case parser.IfStatement(exp=exp, thenS=thenS, elseS=elseS):
            typeCheckExpression(exp, symbolTable)
            typeCheckStatement(thenS, symbolTable)

            if elseS:
                typeCheckStatement(elseS, symbolTable)

            
        case parser.CompoundStatement(block=block):
            typeCheckBlock(block, symbolTable)

        case parser.NullStatement():
            pass


def typeCheckBlock(block, symbolTable):
    if block.blockItemList:
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    typeCheckDeclaration(dec, symbolTable, True)
                    
                case parser.S(statement=statement):
                    typeCheckStatement(statement, symbolTable)
                    
        
def typeCheckFunctionDeclaration(funDec, symbolTable):
    funType = FunType(len(funDec.paramList))
    hasBody = funDec.block != None

    #print(hasBody)

    alreadyDefined = False

    global_ = True
    
    if funDec.storageClass[1] and funDec.storageClass[1] == parser.StorageType.STATIC:
        global_ = False
    

    if funDec.iden in symbolTable:
        oldDecl = symbolTable[funDec.iden]
        #print(funDec.iden, oldDecl[0])
        #tu ya checaste que no es una variable!
        #aqui si son funciones

        if oldDecl.type != IDType.FUNCTION:
            print("Error: Variable redeclared as function.")
            sys.exit(1)

        if oldDecl.funType != funType:
            print("Error: Incompatible function declarations.")
            sys.exit(1)

        alreadyDefined = oldDecl.attrs.defined

        if alreadyDefined and hasBody:
            print("Error: function is defined more than once.")
            sys.exit(1)

        if oldDecl.attrs.global_ and funDec.storageClass[1] == parser.StorageType.STATIC:
            print("Static function declaration follows non-static.")
            sys.exit(1)

        #print("Global: ", global_)
        #print("Old Global: ", oldDecl[2].global_)

        global_ = oldDecl.attrs.global_

    fattr = FunAttributes(defined=(alreadyDefined or hasBody), global_=global_)

    symbolTable[funDec.iden] = Entry(funDec.iden, fattr, IDType.FUNCTION, funType)

    if hasBody:
        for param in funDec.paramList:
            symbolTable[param] = Entry(param, LocalAttributes(), IDType.INT)
        
        typeCheckBlock(funDec.block, symbolTable)
    

def typeCheckProgram(pro):
    symbolTable = {}
    if pro.declList:
        for decl in pro.declList:
            typeCheckDeclaration(decl, symbolTable, False)

    return pro, symbolTable
