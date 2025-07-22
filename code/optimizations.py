import networkx as nx
import tacGenerator
import matplotlib.pyplot as plt
import numpy as np


class Node_ID():
    pass

class ENTRY(Node_ID):
    pass

class EXIT(Node_ID):
    pass

class BlockID(Node_ID):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return "{self.num}".format(self=self)


class Node():
    pass

class BasicBlock(Node):

    def __init__(self, id, instructions, predecessors = None, successors = None):
        self.id = id
        self.instructions = instructions
        self.predecessors = predecessors
        self.successors = successors

    def __str__(self):
        return "{self.id}: {self.instructions} {self.predecessors} {self.successors}".format(self=self)
    
    def __repr__(self):
        return self.__str__()


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
            
    if currentBlock == []:
        pass
    else:
        finishedBlocks.append(currentBlock)

    return finishedBlocks



def makeControlFlowGraph(functionBody):
    iBlocks = partitionIntoBasicBlocks(functionBody.instructions)

    blocks = []
    
    vis = nx.DiGraph()
    vis.add_node("Alejandro")
    vis.add_node("B")
    vis.add_node("C")
    vis.add_edge("Alejandro", "B")
    vis.add_edge("B", "C")

    nx.draw(vis, with_labels=True, node_color='skyblue', node_size=1000, edge_color='gray')

    plt.show()

    for i, instructions in enumerate(iBlocks):
        blocks.append(BasicBlock(BlockID(i), instructions))
        
        #vis.add_node(BasicBlock(BlockID(i), instructions))

    #nx.draw(vis)




    #print(blocks)
	

def unreachableCodeElimination(cfg):
	pass

def copyPropagation(cfg):
	pass

def deadStoreElimination(cfg):
	pass

def cfgToInstructions(cfg):
	pass