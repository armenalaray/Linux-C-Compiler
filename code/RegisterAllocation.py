
import copy
import assemblyGenerator
from assemblyGenerator import RegisterType, SSERegisterType
import typeChecker

import optimizations as op

class Node():
    def __init__(self, operandID):
        self.operandID = operandID
        self.neighbors = []

        self.spillCost = 0.0
        self.color = None
        self.pruned = False

    def printNode(self, level):

        print("    " * level + "{self.operandID} spillCost: {self.spillCost} color: {self.color} pruned: {self.pruned}".format(self=self))

        for n in self.neighbors:
            print("    " * (level + 1) + "{n}".format(n=n))



class Graph():
    def __init__(self):
        self.nodes = {}

    def __str__(self):
        return "{self.nodes}".format(self=self)
    
    def printNode(self, level):
        print("Interference Graph:")

        for k, n in self.nodes.items():
            print(k)
            n.printNode(level + 1)

            
class BaseGraph(Graph):
    def __init__(self):
        super().__init__()

        self.nodes[RegisterType.AX] = Node(RegisterType.AX)
        self.nodes[RegisterType.BX] = Node(RegisterType.BX)
        self.nodes[RegisterType.CX] = Node(RegisterType.CX)
        self.nodes[RegisterType.DX] = Node(RegisterType.DX)
        self.nodes[RegisterType.DI] = Node(RegisterType.DI)
        self.nodes[RegisterType.SI] = Node(RegisterType.SI)
        self.nodes[RegisterType.R8] = Node(RegisterType.R8)
        self.nodes[RegisterType.R9] = Node(RegisterType.R9)
        self.nodes[RegisterType.R12] = Node(RegisterType.R12)
        self.nodes[RegisterType.R13] = Node(RegisterType.R13)
        self.nodes[RegisterType.R14] = Node(RegisterType.R14)
        self.nodes[RegisterType.R15] = Node(RegisterType.R15)

        self.nodes[RegisterType.AX].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.AX].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.BX].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.BX].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.CX].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.CX].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.DX].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.DX].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.DI].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.DI].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.SI].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.SI].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.R8].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.R8].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.R9].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.R9].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.R12].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.R12].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.R13].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.R14)
        self.nodes[RegisterType.R13].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.R14].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.R14].neighbors.append(RegisterType.R15)

        self.nodes[RegisterType.R15].neighbors.append(RegisterType.AX)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.BX)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.CX)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.DX)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.DI)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.SI)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.R8)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.R9)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.R12)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.R13)
        self.nodes[RegisterType.R15].neighbors.append(RegisterType.R14)


def isStatic(identifier, symbolTable):
    a = symbolTable[identifier]

    match a.attrs:
        case typeChecker.StaticAttributes(initialVal = initialVal, global_ = global_):
            return True
    
    return False


def addPseudoRegisters(interferenceGraph, instructions, symbolTable):

    for i in instructions:
        match i:
            case assemblyGenerator.MovInstruction(assType = assType, sourceO = sourceO, destO = destO):
                if isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and not isStatic(sourceO.pseudo, symbolTable):
                    interferenceGraph.nodes[sourceO.pseudo] = Node(sourceO.pseudo)

                if isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and not isStatic(destO.pseudo, symbolTable):
                    interferenceGraph.nodes[destO.pseudo] = Node(destO.pseudo)

            case assemblyGenerator.BinaryInstruction(operator = operator, assType = assType, src = src, dest = dest):
                if isinstance(src, assemblyGenerator.PseudoRegisterOperand) and not isStatic(src.pseudo, symbolTable):
                    interferenceGraph.nodes[src.pseudo] = Node(src.pseudo)
                if isinstance(dest, assemblyGenerator.PseudoRegisterOperand) and not isStatic(dest.pseudo, symbolTable):
                    interferenceGraph.nodes[dest.pseudo] = Node(dest.pseudo)

            case assemblyGenerator.UnaryInstruction(operator = operator, assType = assType, dest = dest):
                if isinstance(dest, assemblyGenerator.PseudoRegisterOperand) and not isStatic(dest.pseudo, symbolTable):
                    interferenceGraph.nodes[dest.pseudo] = Node(dest.pseudo)

            case assemblyGenerator.CompInst(assType = assType, operand0 = operand0, operand1 = operand1):
                if isinstance(operand0, assemblyGenerator.PseudoRegisterOperand) and not isStatic(operand0.pseudo, symbolTable):
                    interferenceGraph.nodes[operand0.pseudo] = Node(operand0.pseudo)
                if isinstance(operand1, assemblyGenerator.PseudoRegisterOperand) and not isStatic(operand1.pseudo, symbolTable):
                    interferenceGraph.nodes[operand1.pseudo] = Node(operand1.pseudo)

            case assemblyGenerator.IDivInstruction(assType = assType, divisor = divisor):
                if isinstance(divisor, assemblyGenerator.PseudoRegisterOperand) and not isStatic(divisor.pseudo, symbolTable):
                    interferenceGraph.nodes[divisor.pseudo] = Node(divisor.pseudo)

            case assemblyGenerator.SetCCInst(conc_code = conc_code, operand = operand):
                if isinstance(operand, assemblyGenerator.PseudoRegisterOperand) and not isStatic(operand.pseudo, symbolTable):
                    interferenceGraph.nodes[operand.pseudo] = Node(operand.pseudo)

            case assemblyGenerator.PushInstruction(operand = operand):
                if isinstance(operand, assemblyGenerator.PseudoRegisterOperand) and not isStatic(operand.pseudo, symbolTable):
                    interferenceGraph.nodes[operand.pseudo] = Node(operand.pseudo)

def partitionIntoBasicBlocks(instructions):

    finishedBlocks = []
    currentBlock = []

    for i in instructions:
        
        match i:
            case assemblyGenerator.LabelInst():
                if currentBlock == []:
                    pass
                else:
                    finishedBlocks.append(currentBlock)

                currentBlock = [i]
            
            case assemblyGenerator.JumpInst():
                currentBlock.append(i)
                finishedBlocks.append(currentBlock)
                currentBlock = []

            case assemblyGenerator.JumpCCInst():
                currentBlock.append(i)
                finishedBlocks.append(currentBlock)
                currentBlock = []

            case assemblyGenerator.ReturnInstruction():
                currentBlock.append(i)
                finishedBlocks.append(currentBlock)
                currentBlock = []
 
            case _:
                currentBlock.append(i)
            
    if currentBlock == []:
        pass
    else:
        finishedBlocks.append(currentBlock)

    return finishedBlocks

"""
case tacGenerator.TAC_LabelInst(identifier = identifier):
                if currentBlock == []:
                    pass
                else:
                    finishedBlocks.append(currentBlock)

                currentBlock = [i]

            case tacGenerator.TAC_JumpIfNotZeroInst():
                currentBlock.append(i)
                finishedBlocks.append(currentBlock)
                currentBlock = []
                
            case tacGenerator.TAC_JumpInst():
                currentBlock.append(i)
                finishedBlocks.append(currentBlock)
                currentBlock = []
            
            case tacGenerator.TAC_JumpIfZeroInst():
                currentBlock.append(i)
                finishedBlocks.append(currentBlock)
                currentBlock = []
            
            case tacGenerator.TAC_returnInstruction():
                currentBlock.append(i)
                finishedBlocks.append(currentBlock)
                currentBlock = []
"""

def addAllEdgesToCFG(cfg):

    op.addEdge(op.ENTRY(), op.BlockID(0), cfg)

    for k, n in cfg.blocks.items():

        if k == op.ENTRY() or k == op.EXIT():
            continue
        
        #aqui ya estas trabajando con blockids!
        if n.id == op.BlockID(cfg.maxID):
            nextID = op.EXIT()
        else:
            nextID = op.BlockID(n.id.num + 1)

        i = n.instructions[-1]

        match i:

            case assemblyGenerator.ReturnInstruction():
                op.addEdge(n.id, op.EXIT(), cfg)

            case assemblyGenerator.JumpInst(identifier = identifier):
                obj = cfg.labels[identifier]
                op.addEdge(n.id, obj.id, cfg)

            case assemblyGenerator.JumpCCInst(conc_code = conc_code, identifier = identifier):
                obj = cfg.labels[identifier]
                op.addEdge(n.id, obj.id, cfg)
                op.addEdge(n.id, nextID, cfg)

            case _:
                op.addEdge(n.id, nextID, cfg)

    print("-------------CONNECTED BLOCKS-----------------")
    for k, n in cfg.blocks.items():
        print(k, n)    

"""
case tacGenerator.TAC_returnInstruction(Value = Value):
                addEdge(n.id, EXIT(), graph)

            case tacGenerator.TAC_JumpInst(label = label):
                #print(label, graph.labels[label])
                obj = graph.labels[label]
                addEdge(n.id, obj.id, graph)

            case tacGenerator.TAC_JumpIfZeroInst(condition = condition, label = label):
                obj = graph.labels[label]
                addEdge(n.id, obj.id, graph)
                addEdge(n.id, nextID, graph)

            case tacGenerator.TAC_JumpIfNotZeroInst(condition = condition, label = label):
                obj = graph.labels[label]
                addEdge(n.id, obj.id, graph)
                addEdge(n.id, nextID, graph)
"""

def makeControlFlowGraph(functionBody):

    iBlocks = partitionIntoBasicBlocks(functionBody)

    g = op.G()

    g.blocks[op.ENTRY()] = op.Entry()

    g.maxID = len(iBlocks) - 1

    for i, instructions in enumerate(iBlocks):
        g.blocks[op.BlockID(i)] = op.BasicBlock(op.BlockID(i), instructions)

        
        probLabel = instructions[0]

        print(probLabel)

        match probLabel:
            case assemblyGenerator.LabelInst(identifier = identifier):
                g.labels[identifier] = op.BasicBlock(op.BlockID(i), instructions)

    g.blocks[op.EXIT()] = op.Exit()

    print("-------------LABELS-----------------")

    for k, w in g.labels.items():
        print(k,w)

    addAllEdgesToCFG(g)

    return g
    
def meetLive(n, cfg):
    liveVars = set()

    for sID in n.successors:
        match sID:
            case op.ENTRY():
                print("Error: Malformed control graph.")
                sys.exit(1)

            case op.EXIT():
                liveVars.add(RegisterType.AX)

            case op.BlockID(num = num):
                node = cfg.blocks[sID]
                liveVars.update(node.reachingCopies)

    return liveVars

def findUsedAndUpdated(instruction, backendSymbolTable):
    used = []
    updated = []

    match instruction:
        case assemblyGenerator.MovInstruction(sourceO = sourceO, destO = destO):
            used = [sourceO]
            updated = [destO]

        case assemblyGenerator.BinaryInstruction(src = src, dest = dest):
            used = [src, dest]
            updated = [dest]

        case assemblyGenerator.UnaryInstruction(dest = dest):
            used = [dest]
            updated = [dest]

        case assemblyGenerator.CompInst(operand0 = operand0, operand1 = operand1):
            used = [operand0, operand1]
            updated = []

        case assemblyGenerator.SetCCInst(operand = operand):
            used = []
            updated = [operand]
        
        case assemblyGenerator.PushInstruction(operand = operand):
            used = [operand]
            updated = []

        case assemblyGenerator.IDivInstruction(divisor = divisor):
            used = [divisor, RegisterType.AX, RegisterType.DX]
            updated = [RegisterType.AX, RegisterType.DX]

        case assemblyGenerator.CDQInstruction():
            used = [RegisterType.AX]
            updated = [RegisterType.DX]
        
        case assemblyGenerator.CallInstruction(identifier = identifier):
            funEntry = backendSymbolTable[identifier]
            
            used = list(funEntry.paramInt)
            updated = [RegisterType.DI, RegisterType.SI, RegisterType.DX, RegisterType.CX, RegisterType.R8, RegisterType.R9, RegisterType.AX]

        case _:
            used = []
            updated = []
    
    return used, updated

def transferLive(n, endLiveRegisters, backendSymbolTable):

    currentLiveRegisters = endLiveRegisters

    print("--------------LIVE for block {0}-------------------".format(n.id))

    a = list(n.iMap.items())
    a.reverse()

    #print(a)

    for i, set0 in a:

        set0.clear()
        set0.update(currentLiveRegisters)

        print(i, set0)

    findUsedAndUpdated(n.instructions[0], backendSymbolTable)


def analyzeLiveness(cfg, backendSymbolTable):
    #allStaticVariables = addAllStaticVariables(cfg, symbolTable)

    workList = []

    a = list(cfg.blocks.items())
    a.reverse()

    for k, n in a:
        if k == op.ENTRY() or k == op.EXIT():
            continue
        
        workList.append(n)
        n.reachingCopies.clear()

    while workList != []:
        n = workList.pop(0)
        
        oldAnnot = copy.deepcopy(n.reachingCopies)

        liveVars = meetLive(n, cfg)
        transferLive(n, liveVars, backendSymbolTable)

        """

        print("OLD ANNOT:", oldAnnot)
        print("NEW ANNOT:", n.reachingCopies)

        if oldAnnot != n.reachingCopies:


            for pID in n.predecessors:

                match pID:

                    case EXIT():
                        print("Error: Malformed control flow graph.")
                        sys.exit(1)

                    case ENTRY():
                        continue

                    case BlockID(num = num):

                        
                        block = cfg.blocks[pID]

                        if block in workList:
                            pass
                        else:
                            print("ADD PREDECESSORS.")
                            workList.append(block)
        """
    

def addEdges(cfg, interferenceGraph):
    pass

def buildInterferenceGraph(instructions, symbolTable, backendSymbolTable):

    print("-----------Building interference graph.------------------")

    interferenceGraph = BaseGraph()

    addPseudoRegisters(interferenceGraph, instructions, symbolTable)

    interferenceGraph.printNode(0)
    
    ########################### es diferente

    cfg = makeControlFlowGraph(instructions)

    analyzeLiveness(cfg, backendSymbolTable)

    addEdges(cfg, interferenceGraph)

    return interferenceGraph

def addSpillCosts(interGraph, instructions):
    pass

def colorGraph(interGraph):
    pass

def createRegisterMap(interGraph):
    pass

def replacePseudoRegs(instructions, registerMap):
    pass

def allocateRegistersForType(instructions, registers, symbolTable, backendSymbolTable):

    interGraph = buildInterferenceGraph(instructions, symbolTable, backendSymbolTable)

    addSpillCosts(interGraph, instructions)

    colorGraph(interGraph)

    registerMap = createRegisterMap(interGraph)

    replacedIns = replacePseudoRegs(instructions, registerMap)

    return replacedIns

def allocateRegisters(instructions, symbolTable, backendSymbolTable):

    intRegisters = list(RegisterType)
    print(intRegisters)
    doubleRegisters = list(SSERegisterType)

    allocateRegistersForType(instructions, intRegisters, symbolTable, backendSymbolTable)
    #allocateRegistersForType(instructions, doubleRegisters, symbolTable)
