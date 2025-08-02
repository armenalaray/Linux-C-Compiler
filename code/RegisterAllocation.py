
from assemblyGenerator import RegisterType, SSERegisterType


class Node():
    def __init__(self, operandID):
        self.operandID = operandID
        self.neighbors = []

        self.spillCost = 0.0
        self.color = None
        self.pruned = False



class Graph():
    def __init__(self):
        self.nodes = {}

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


def addPseudoRegisters(interferenceGraph, instructions):
    pass

def makeControlFlowGraph(instructions):
    pass

def analyzeLiveness(cfg):
    pass

def addEdges(cfg, interferenceGraph):
    pass

def buildGraph(instructions):
    interferenceGraph = Graph()
    
    addPseudoRegisters(interferenceGraph, instructions)
    
    cfg = makeControlFlowGraph(instructions)
    
    analyzeLiveness(cfg)

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

def allocateRegistersForType(instructions, registers):

    interGraph = buildGraph(instructions)

    addSpillCosts(interGraph, instructions)

    colorGraph(interGraph)

    registerMap = createRegisterMap(interGraph)

    replacedIns = replacePseudoRegs(instructions, registerMap)

    return replacedIns

def allocateRegisters(instructions):

    intRegisters = list(RegisterType)
    print(intRegisters)
    doubleRegisters = list(SSERegisterType)

    allocateRegistersForType(instructions, intRegisters)
    allocateRegistersForType(instructions, doubleRegisters)
