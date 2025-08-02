
from assemblyGenerator import RegisterType, SSERegisterType

def buildGraph(instructions):
    pass

def addSpillCosts(interGraph, instructions):
    pass

def colorGraph(interGraph):
    pass

def createRegisterMap(interGraph):
    pass

def replacePseudoRegs(instructions, registerMap):
    pass

def allocateRegisters(instructions):

    intRegisters = list(RegisterType)
    print(intRegisters)
    doubleRegisters = list(SSERegisterType)

    allocateRegistersForType(instructions, intRegisters)
    allocateRegistersForType(instructions, doubleRegisters)

def allocateRegistersForType(instructions, registers):

    interGraph = buildGraph(instructions)

    addSpillCosts(interGraph, instructions)

    colorGraph(interGraph)

    registerMap = createRegisterMap(interGraph)

    replacedIns = replacePseudoRegs(instructions, registerMap)

    return replacedIns

