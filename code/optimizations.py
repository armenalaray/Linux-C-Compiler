import networkx as nx
import tacGenerator
import parser
import matplotlib.pyplot as plt
import numpy as np

import traceback
import sys

import copy

class DebugNode():
    def printNode(self):
        return ""

class Node_ID():
    pass

class ENTRY(Node_ID, DebugNode):
    def __init__(self):
        self.num = -2

    def __str__(self):
        return "ENTRY"
    
    def __repr__(self):
        return self.__str__()
    
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
    
    def __str__(self):
        return "EXIT"
    
    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return self.num
            
    def __eq__(self, value):
        #print(type(value))
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

    def __init__(self, id, instructions):
        self.id = id
        self.instructions = instructions
        self.predecessors = set()
        self.successors = set()

    def __str__(self):
        return "{self.id}: {self.instructions} Pred: {self.predecessors} Suc: {self.successors}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
    def printNode(self):
        output = ""

        output += self.id.printNode() + "\n\n"

        for i in self.instructions:
            output += i.printNode() + "\n"


        return output


class Entry(Node, DebugNode):

    def __init__(self):
        self.successors = set()
        self.id = ENTRY()

    def __str__(self):
        return "Entry: {self.id} {self.successors}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
        

class Exit(Node, DebugNode):

    def __init__(self):
        self.predecessors = set()
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

#va de la direccion 0 a 1
def addEdge(nodeID0, nodeID1, graph):

    print()
    #print(graph[nodeID1])

    entry0 = graph.blocks[nodeID0]
    entry1 = graph.blocks[nodeID1]

    match entry0:
        case Entry(successors = s):
            entry0.successors.add(nodeID1)
            

        case BasicBlock(id = id, instructions = instructions, successors = s):
            entry0.successors.add(nodeID1)

        case Exit():
            print("Error: Exit has no successors.")
            sys.exit(1)

    match entry1:
        case Entry():
            print("Error: Entry has no predecessors.")
            sys.exit(1)

        case BasicBlock(id = id, instructions = instructions, predecessors = p):
            entry1.predecessors.add(nodeID0)

        case Exit(predecessors = p):
            entry1.predecessors.add(nodeID0)

def removeEdge(nodeID0, nodeID1, graph):

    entry0 = graph.blocks[nodeID0]
    entry1 = graph.blocks[nodeID1]

    match entry0:
        case Entry(successors = s):

            newSet = set()
            for s in entry0.successors:
                if nodeID1 == s:
                    pass
                else:
                    newSet.add(s)
                
            entry0.successors = newSet

            #entry0.successors.add(nodeID1)
            

        case BasicBlock(id = id, instructions = instructions, successors = s):

            newSet = set()
            for s in entry0.successors:
                if nodeID1 == s:
                    pass
                else:
                    newSet.add(s)
                
            entry0.successors = newSet

            """
            if nodeID1 in entry0.successors:
                entry0.successors.remove(nodeID1)
                pass
            """
            #entry0.successors.add(nodeID1)

        case Exit():
            print("Error: Exit has no successors.")
            sys.exit(1)

    match entry1:
        case Entry():
            print("Error: Entry has no predecessors.")
            sys.exit(1)

        case BasicBlock(id = id, instructions = instructions, predecessors = p):

            newSet = set()

            for p in entry1.predecessors:
                if nodeID0 == p:
                    pass
                else:
                    newSet.add(p)
                
            entry1.predecessors = newSet

            """
            if nodeID0 in entry1.predecessors:
                entry1.predecessors.remove(nodeID0)
                pass
            """

            #entry1.predecessors.add(nodeID0)

        case Exit(predecessors = p):

            newSet = set()
            
            for p in entry1.predecessors:
                if nodeID0 == p:
                    pass
                else:
                    newSet.add(p)
                
            entry1.predecessors = newSet

            """
            if nodeID0 in entry1.predecessors:
                entry1.predecessors.remove(nodeID0)
                pass
            """

            #entry1.predecessors.add(nodeID0)


def maxBlockID(graph):
    pass

def addAllEdges(graph):

    addEdge(ENTRY(), BlockID(0), graph)

    #print(graph)

    for k, n in graph.blocks.items():

        if k == ENTRY() or k == EXIT():
            continue
        
        #aqui ya estas trabajando con blockids!
        if n.id == BlockID(graph.maxID):
            nextID = EXIT()
        else:
            nextID = BlockID(n.id.num + 1)

        i = n.instructions[-1]

        match i:
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

            case _:
                addEdge(n.id, nextID, graph)
    

    for k, n in graph.blocks.items():
        print(k, n)


class G():
    def __init__(self):
        self.maxID = -1
        self.blocks = {}
        self.labels = {}

def makeControlFlowGraph(functionBody):
    iBlocks = partitionIntoBasicBlocks(functionBody)

    g = G()

    #blocks = {}
    adjacency_dict = {}

    g.blocks[ENTRY()] = Entry()

    g.maxID = len(iBlocks) - 1

    for i, instructions in enumerate(iBlocks):
        g.blocks[BlockID(i)] = BasicBlock(BlockID(i), instructions)

        probLabel = instructions[0]

        print(probLabel)

        match probLabel:
            case tacGenerator.TAC_LabelInst(identifier = identifier):
                g.labels[identifier] = BasicBlock(BlockID(i), instructions)
        
        #adjacency_dict[i] = ()

    g.blocks[EXIT()] = Exit()

    #print(blocks)
    

    """
    names = {}
    for block in blocks:
        names[block.id.num] = block.printNode()

    print(adjacency_dict)

    DG = nx.Graph(adjacency_dict, day="Friday")

    nx.draw_networkx(DG, with_labels=True, node_color="pink", node_shape="s", labels=names, font_size=20)
    
    plt.show()
    """

    addAllEdges(g)

    return g

visitedList = []

def visit(a, cfg):
    global visitedList

    if a.id in visitedList:
        return 

    visitedList.append(a.id)

    if a.id == EXIT():
        return 
    
    for i in a.successors:
        d = cfg.blocks[i]
        visit(d, cfg)

def removeEmptyBlocks(cfg):
    global visitedList

    visitedList = []

    for k, n in cfg.blocks.items():

        if k == ENTRY() or k == EXIT():
            continue

        if n.instructions == []:
            
            for p in n.predecessors:
                removeEdge(p, k, cfg)

                for s in n.successors:
                    addEdge(p, s, cfg)

            for s in n.successors:
                removeEdge(k, s, cfg)    

            visitedList.append(k)

    newBlocks = {}
    
    for k, n in cfg.blocks.items():
        if k in visitedList:
            pass
        else:
            newBlocks[k] = n

    cfg.blocks = newBlocks
    
    for k, n in cfg.blocks.items():
        print(k,n)


def removeRedundantJumps(cfg):
    
    i = 1
    nodes = list(cfg.blocks.values())
    while i < len(nodes) - 2:
        #print(nodes[i])

        block = nodes[i]

        instruction = block.instructions[-1]

        #print(type(instruction))

        if type(instruction) == tacGenerator.TAC_JumpInst or type(instruction) == tacGenerator.TAC_JumpIfZeroInst or type(instruction) == tacGenerator.TAC_JumpIfNotZeroInst:

            keepJump = False
            nextBlock = nodes[i + 1]

            for sID in block.successors:

                if sID == nextBlock.id:
                    pass
                else:
                    keepJump = True
                    break
            

            if not keepJump:
                print("POP REDUNDANT JUMP")
                block.instructions.pop()

        i += 1

    removeEmptyBlocks(cfg)

    
def removeRedundantLabels(cfg):
    i = 1
    
    nodes = list(cfg.blocks.values())

    while i < len(nodes) - 1:

        block = nodes[i]

        instruction = block.instructions[0]

        if type(instruction) == tacGenerator.TAC_LabelInst:

            keepLabel = False
            prevBlock = nodes[i - 1]

            for sID in block.predecessors:

                if sID == prevBlock.id:
                    pass
                else:
                    keepLabel = True
                    break
            

            if not keepLabel:
                print("POP REDUNDANT LABEL")
                block.instructions.pop(0)

        i += 1

    removeEmptyBlocks(cfg)

    #for k, n in cfg.blocks.items():
    #    print(k,n)
    

def unreachableCodeElimination(cfg):
    #print(cfg.blocks[ENTRY()])
    global visitedList
	
    a = cfg.blocks[ENTRY()]

    visitedList = []
    
    visit(a, cfg)
    
    #print(visitedList)

    newBlocks = {}
    
    for k, n in cfg.blocks.items():
        if k in visitedList:
            newBlocks[k] = n
        else:
            pass


    for k, n in newBlocks.items():
        #print(k, n)

        match k:
            case ENTRY():
                newSet = set()
                for i in n.successors:
                    if i in visitedList:
                        newSet.add(i)
                    else:
                        pass
                        #n.successors.discard(i)
                
                n.successors = newSet
                        
            case BlockID():
                newSet = set()
                for i in n.successors:
                    if i in visitedList:
                        newSet.add(i)
                    else:
                        pass
                        #n.successors.discard(i)
                n.successors = newSet

                newSet = set()
                for i in n.predecessors:
                    if i in visitedList:
                        newSet.add(i)
                    else:
                        pass
                        #n.predecessors.discard(i)
                
                n.predecessors = newSet

            case EXIT():

                newSet = set()
                for i in n.predecessors:
                    if i in visitedList:
                        newSet.add(i)
                        pass
                    else:
                        pass
                        #n.predecessors.discard(i)

                n.predecessors = newSet
                

    
    cfg.blocks = newBlocks

    for k, n in cfg.blocks.items():
        print(k,n)

    removeRedundantJumps(cfg)

    removeRedundantLabels(cfg)

    return cfg

def copyPropagation(cfg):
	return cfg
	pass

def deadStoreElimination(cfg):
	return cfg
	pass

def cfgToInstructions(cfg):
    #ya estan sorteados
    list = []
    for k, n in cfg.blocks.items():
        if n.id == ENTRY() or n.id == EXIT():
            continue

        list.extend(n.instructions)

    #print(list)

    return list


def constantFolding(tac):
    print("CONSTANT FOLDING PASS")

    print("OLD LIST", tac)

    newList = []

    for i in tac:

        match i:
            case tacGenerator.TAC_JumpIfZeroInst(condition = condition, label = label):

                match condition:
                    case tacGenerator.TAC_ConstantValue(const = const):

                        match const:
                            case parser.ConstInt(int = int):

                                #traceback.print_stack()
                                #print(type(int))
                                #sys.exit(1)


                                if int == 0:
                                    newList.append(tacGenerator.TAC_JumpInst(label))
                                else:
                                    #aqui no se hace el append
                                    pass
                            
                            case _:
                                newList.append(i)        

                    case _:
                        newList.append(i)        
                        

            case tacGenerator.TAC_JumpIfNotZeroInst(condition = condition, label = label):
                match condition:
                    case tacGenerator.TAC_ConstantValue(const = const):

                        match const:
                            case parser.ConstInt(int = int):

                                #traceback.print_stack()
                                #print(type(int))
                                #sys.exit(1)


                                if int != 0:
                                    newList.append(tacGenerator.TAC_JumpInst(label))
                                else:
                                    #aqui no se hace el append
                                    pass
                            
                            case _:
                                newList.append(i)        

                    case _:
                        newList.append(i)        

            case _:
                newList.append(i)

    #traceback.print_stack()
    print("NEW LIST", newList)
    #sys.exit(1)

    return newList
    