import sys
import parser
import tacGenerator

def makeLabel():
    return tacGenerator.makeTemp()

def labelStatement(statement, currentLabel):
    match statement:
        case parser.BreakStatement():
            if currentLabel:
                return parser.BreakStatement(currentLabel)
                
            print("Break statement outside of loop.")
            sys.exit(1)
        
        case parser.ContinueStatement():
            if currentLabel:
                return parser.ContinueStatement(currentLabel)
                
            print("Continue statement outside of loop.")
            sys.exit(1)

        case parser.ForStatement(forInit=forInit, condExp=condExp, postExp=postExp, statement=statement, identifier=identifier):
            newLabel = makeLabel()
            s = labelStatement(statement, newLabel)
            return parser.ForStatement(forInit, s, condExp, postExp, newLabel)

        case parser.WhileStatement(condExp=condExp, statement=statement, identifier=id):
            newLabel = makeLabel()
            #print(statement)
            s = labelStatement(statement, newLabel)
            return parser.WhileStatement(condExp, s, newLabel)

        case parser.DoWhileStatement(statement=statement, condExp=condExp):
            newLabel = makeLabel()
            #print(statement)
            s = labelStatement(statement, newLabel)
            return parser.DoWhileStatement(s, condExp, newLabel)

        case parser.CompoundStatement(block=block):
            b = labelBlock(block, currentLabel)
            return parser.CompoundStatement(b)
            pass
        
        case parser.ReturnStmt(expression=exp):
            return parser.ReturnStmt(exp)

        case parser.IfStatement(exp=expCond, thenS=thenS, elseS=elseS):
            t = labelStatement(thenS, currentLabel)
            
            e = None
            if elseS:
                e = labelStatement(elseS, currentLabel)

            return parser.IfStatement(expCond, t, e)
        
        case parser.ExpressionStmt(exp=exp):
            return parser.ExpressionStmt(exp)

        case parser.NullStatement():
            return parser.NullStatement()

def labelBlock(block, currentLabel):
    
    if block.blockItemList:
        blockItemList = []
        
        for i in block.blockItemList:
            match i:
                case parser.D(declaration=dec):
                    blockItemList.append(parser.D(dec))

                case parser.S(statement=statement):
                    s = labelStatement(statement, currentLabel)
                    blockItemList.append(parser.S(s))
        
        return parser.Block(blockItemList)

    return parser.Block()

    
    blockItemList = []

    for i in block.blockItemList:
        match i:
            case parser.D(declaration=dec):
                blockItemList.append(parser.D(dec))
                
            case parser.S(statement=statement):
                s = labelStatement(statement, currentLabel)
                blockItemList.append(parser.S(s))

    return parser.Block(blockItemList)

def labelFunctionDeclaration(funDecl, currentLabel):
    #aqui solo tienes que checar el bloque
    block = None
    if funDecl.block:
        block = labelBlock(funDecl.block, currentLabel)
        
    return parser.FunctionDecl(funDecl.iden, funDecl.paramList, block, funDecl.storageClass)

def labelDeclaration(decl):
    match decl:
        case parser.VarDecl(variableDecl = variableDecl):
            return parser.VarDecl(variableDecl)
            
        case parser.FunDecl(funDecl = funDecl):
            f = labelFunctionDeclaration(funDecl, None)
            return parser.FunDecl(f)

def labelProgram(pro):

    if pro.declList:
        declList = []
        for decl in pro.declList:
            f = labelDeclaration(decl)
            declList.append(f)
            
        return parser.Program(declList)

    return parser.Program()
    