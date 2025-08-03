
import copy
import assemblyGenerator
from assemblyGenerator import RegisterType, SSERegisterType, RegisterOperand, Register
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

        self.nodes[RegisterOperand(Register(RegisterType.AX))] = Node(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))] = Node(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))] = Node(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))] = Node(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))] = Node(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))] = Node(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))] = Node(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))] = Node(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))] = Node(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))] = Node(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))] = Node(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))] = Node(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.append(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.append(RegisterOperand(Register(RegisterType.R14)))


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
                liveVars.add(RegisterOperand(Register(RegisterType.AX)))

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
            used = [divisor, RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))]

            updated = [RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))]

        case assemblyGenerator.CDQInstruction():
            used = [RegisterOperand(Register(RegisterType.AX))]

            updated = [RegisterOperand(Register(RegisterType.DX))]

        case assemblyGenerator.CallInstruction(identifier = identifier):
            funEntry = backendSymbolTable[identifier]
            
            used = list(funEntry.paramInt)

            updated = [RegisterOperand(Register(RegisterType.DI)), 
                       RegisterOperand(Register(RegisterType.SI)), 
                       RegisterOperand(Register(RegisterType.DX)), 
                       RegisterOperand(Register(RegisterType.CX)), 
                       RegisterOperand(Register(RegisterType.R8)), 
                       RegisterOperand(Register(RegisterType.R9)), 
                       RegisterOperand(Register(RegisterType.AX))]

        case _:
            used = []
            updated = []
    
    return used, updated

def isRegister(operand):

    match operand:

        case assemblyGenerator.RegisterOperand():
            return True
        
        case assemblyGenerator.PseudoRegisterOperand():
            return True
        
        case _:
            return False

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
        
        used, updated = findUsedAndUpdated(i, backendSymbolTable)

        for v in updated:
            if isRegister(v):
                currentLiveRegisters.discard(v)
                

        for v in used:
            if isRegister(v):
                currentLiveRegisters.add(v)

    n.reachingCopies.clear()
    n.reachingCopies.update(currentLiveRegisters)

def analyzeLiveness(cfg, backendSymbolTable):
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

        print("OLD ANNOT:", oldAnnot)
        print("NEW ANNOT:", n.reachingCopies)

        if oldAnnot != n.reachingCopies:

            for pID in n.predecessors:

                match pID:

                    case op.EXIT():
                        print("Error: Malformed control flow graph.")
                        sys.exit(1)

                    case op.ENTRY():
                        continue

                    case op.BlockID(num = num):

                        block = cfg.blocks[pID]

                        if block in workList:
                            pass
                        else:
                            print("ADD PREDECESSORS.")
                            workList.append(block)
        
    

def addEdges(cfg, interferenceGraph, backendSymbolTable):
    print("-----------Adding edges to interference graph.------------------")

    for k, n in cfg.blocks.items():
        if k == op.ENTRY() or k == op.EXIT():
            continue

        for i, set0 in n.iMap.items():

            used, updated = findUsedAndUpdated(i, backendSymbolTable)

            for l in set0:
                if isinstance(i, assemblyGenerator.MovInstruction) and l == i.sourceO:
                    continue

                for u in updated:
                    if l in interferenceGraph.nodes and u in interferenceGraph.nodes and not (l == u):
                        addEdge(l, u, interferenceGraph)

                    
                
            


        
    

def buildInterferenceGraph(instructions, symbolTable, backendSymbolTable):

    print("-----------Building interference graph.------------------")

    interferenceGraph = BaseGraph()

    addPseudoRegisters(interferenceGraph, instructions, symbolTable)

    interferenceGraph.printNode(0)
    
    ########################### es diferente

    cfg = makeControlFlowGraph(instructions)

    analyzeLiveness(cfg, backendSymbolTable)

    addEdges(cfg, interferenceGraph, backendSymbolTable)

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
