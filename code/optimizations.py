import tacGenerator

class Node_ID():
    pass

class ENTRY(Node_ID):
    pass

class EXIT(Node_ID):
    pass

class BlockID(Node_ID):
    def __init__(self, num):
        self.num = num


class Node():
    pass

class BasicBlock(Node):

    def __init__(self, id, instructions, predecessors, successors):
        self.id = id
        self.instructions = instructions
        self.predecessors = predecessors
        self.successors = successors


class Entry(Node):

    def __init__(self, successors):
        self.successors = successors
        

class Exit(Node):

    def __init__(self, predecessors):
        self.predecessors = predecessors


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes


def partitionIntoBasicBlocks(instructions):

    finishedBlocks = []
    currentBlock = []

    for i in instructions:
        print(type(i))
        
        match i:
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
             
            case _:
                currentBlock.append(i)
            
    

def makeControlFlowGraph(functionBody):
    partitionIntoBasicBlocks(functionBody.instructions)
	

def unreachableCodeElimination(cfg):
	pass

def copyPropagation(cfg):
	pass

def deadStoreElimination(cfg):
	pass

def cfgToInstructions(cfg):
	pass