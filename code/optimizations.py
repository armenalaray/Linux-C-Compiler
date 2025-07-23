import networkx as nx
import tacGenerator
import matplotlib.pyplot as plt
import numpy as np

class DebugNode():
    def printNode(self):
        return ""

class Node_ID():
    pass

class ENTRY(Node_ID, DebugNode):
    pass

class EXIT(Node_ID, DebugNode):
    pass

class BlockID(Node_ID, DebugNode):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return "{self.num}".format(self=self)
    
    def printNode(self):
        return str(self.num)


class Node():
    pass

class BasicBlock(Node, DebugNode):

    def __init__(self, id, instructions, predecessors = None, successors = None):
        self.id = id
        self.instructions = instructions
        self.predecessors = predecessors
        self.successors = successors

    def __str__(self):
        return "{self.id}: {self.instructions} {self.predecessors} {self.successors}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
    def printNode(self):
        output = ""

        output += self.id.printNode() + "\n\n"

        for i in self.instructions:
            output += i.printNode() + "\n"


        return output


class Entry(Node, DebugNode):

    def __init__(self, successors):
        self.successors = successors
        

class Exit(Node, DebugNode):

    def __init__(self, predecessors):
        self.predecessors = predecessors


class Graph(DebugNode):
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
            
    if currentBlock == []:
        pass
    else:
        finishedBlocks.append(currentBlock)

    return finishedBlocks



def makeControlFlowGraph(functionBody):
    iBlocks = partitionIntoBasicBlocks(functionBody.instructions)

    blocks = []
    adjacency_dict = {}

    for i, instructions in enumerate(iBlocks):
        blocks.append(BasicBlock(BlockID(i), instructions))
        adjacency_dict[i] = ()

    names = {}
    for block in blocks:
        names[block.id.num] = block.printNode()

    print(adjacency_dict)

    DG = nx.Graph(adjacency_dict, day="Friday")

    nx.draw_networkx(DG, with_labels=True, node_color="pink", node_shape="s", labels=names, font_size=20)
    
    plt.show()
	

def unreachableCodeElimination(cfg):
	pass

def copyPropagation(cfg):
	pass

def deadStoreElimination(cfg):
	pass

def cfgToInstructions(cfg):
	pass