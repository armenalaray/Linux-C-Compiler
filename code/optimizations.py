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
    def __init__(self):
        self.num = -2
    
    def __hash__(self):
        return self.num
    
    def __eq__(self, value):
        if isNodeID(value) and value.num == self.num:
            return True
        
        return False

def isNodeID(value):
    if type(value) == ENTRY or type(value) == EXIT or type(value) == BlockID:
        return True
    
    return False

class EXIT(Node_ID, DebugNode):
    def __init__(self):
        self.num = -1
    
    def __hash__(self):
        return self.num
            
    def __eq__(self, value):
        if isNodeID(value) and value.num == self.num:
            return True
        
        return False
        

class BlockID(Node_ID, DebugNode):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return "{self.num}".format(self=self)
    
    def __repr__(self):
        return self.__str__()

    def printNode(self):
        return str(self.num)

    def __hash__(self):
        return self.num
    
    def __eq__(self, value):
        if isNodeID(value) and value.num == self.num:
            return True
        
        return False

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

    def __init__(self, successors = None):
        self.successors = successors
        self.id = ENTRY()

    def __str__(self):
        return "Entry: {self.id} {self.successors}".format(self=self)
        

class Exit(Node, DebugNode):

    def __init__(self, predecessors = None):
        self.predecessors = predecessors
        self.id = EXIT()

    def __str__(self):
        return "Exit: {self.id} {self.predecessors}".format(self=self)


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

def addEdge(nodeID0, nodeID1, graph):

    print(graph[nodeID0])

    
    

def addAllEdges(graph):

    addEdge(ENTRY(), BlockID(0), graph)


    pass

def makeControlFlowGraph(functionBody):
    iBlocks = partitionIntoBasicBlocks(functionBody.instructions)

    blocks = {}
    adjacency_dict = {}

    blocks[ENTRY()] = Entry()

    for i, instructions in enumerate(iBlocks):
        blocks[BlockID(i)] = BasicBlock(BlockID(i), instructions)
        #blocks.append(BasicBlock(BlockID(i), instructions))
        adjacency_dict[i] = ()

    blocks[EXIT()] = Exit()


    print(blocks)
    

    """
    names = {}
    for block in blocks:
        names[block.id.num] = block.printNode()

    print(adjacency_dict)

    DG = nx.Graph(adjacency_dict, day="Friday")

    nx.draw_networkx(DG, with_labels=True, node_color="pink", node_shape="s", labels=names, font_size=20)
    
    plt.show()
    """

    addAllEdges(blocks)


	

def unreachableCodeElimination(cfg):
	pass

def copyPropagation(cfg):
	pass

def deadStoreElimination(cfg):
	pass

def cfgToInstructions(cfg):
	pass