import sys
import copy
import assemblyGenerator
import tacGenerator
from assemblyGenerator import RegisterType, SSERegisterType, RegisterOperand, Register, PseudoRegisterOperand
import typeChecker


class Node():
    def __init__(self, operandID):
        self.operandID = operandID

        self.neighbors = set()

        self.spillCost = 0.0
        self.color = None
        self.pruned = False

    def __str__(self):
        return "{self.operandID} spillCost: {self.spillCost} color: {self.color} pruned: {self.pruned}".format(self=self)
    def printNode(self, level):

        print("    " * level + "{self.operandID} spillCost: {self.spillCost} color: {self.color} pruned: {self.pruned}".format(self=self))

        for n in self.neighbors:
            print("    " * (level + 1) + "{n}".format(n=n))



class Graph():
    def __init__(self):
        self.nodes = {}
        self.k = None

    def areNeighbors(self, x, y):
        if y in self.nodes[x].neighbors or x in self.nodes[y].neighbors:
            return True
    
        return False    

    def briggsTest(self, x, y):
        significantNeighbors = 0

        xNode = self.nodes[x]
        yNode = self.nodes[y]

        allNeighbors = xNode.neighbors | yNode.neighbors


        for nID in allNeighbors:
            node = self.nodes[nID]

            degree = len(node.neighbors)
            if self.areNeighbors(nID, x) and self.areNeighbors(nID, y):
                degree -= 1
                
            if degree >= self.k:
                significantNeighbors += 1

        return significantNeighbors < self.k

    def addEdge(self, v0, v1):
        if v0 in self.nodes and v1 in self.nodes:
            self.nodes[v0].neighbors.add(v1)
            self.nodes[v1].neighbors.add(v0)

    def removeEdge(self, v0, v1):
        if v0 in self.nodes and v1 in self.nodes:
            self.nodes[v1].neighbors.discard(v0)
        
    def __str__(self):
        return "{self.nodes}".format(self=self)
    
    def printNode(self, level):
        print("Interference Graph:")

        for k, n in self.nodes.items():
            print(k)
            n.printNode(level + 1)

class DoubleBaseGraph(Graph):
    def __init__(self):
        super().__init__()
        self.k = 14
    
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))] = Node(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))] = Node(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))] = Node(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))] = Node(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))] = Node(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))] = Node(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))] = Node(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))] = Node(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))] = Node(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))] = Node(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))] = Node(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))] = Node(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))] = Node(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))] = Node(RegisterOperand(Register(SSERegisterType.XMM13)))


        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM13)))

        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM0)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM1)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM2)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM3)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM4)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM5)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM6)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM7)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM8)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM9)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM10)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM11)))
        self.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].neighbors.add(RegisterOperand(Register(SSERegisterType.XMM12)))

        
class IntegerBaseGraph(Graph):
    def __init__(self):
        super().__init__()
        self.k = 12

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

        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.AX))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.BX))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.CX))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.DX))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.DI))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.SI))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R8))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R9))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R12))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))
        self.nodes[RegisterOperand(Register(RegisterType.R13))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R14))].neighbors.add(RegisterOperand(Register(RegisterType.R15)))

        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.AX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.BX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.CX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.DX)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.DI)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.SI)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.R8)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.R9)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.R12)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.R13)))
        self.nodes[RegisterOperand(Register(RegisterType.R15))].neighbors.add(RegisterOperand(Register(RegisterType.R14)))


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
        return hash((self.num))

    def __eq__(self, value):
        if not isinstance(value, ENTRY):
            return NotImplemented
        
        return self.num == value.num
    

class EXIT(Node_ID, DebugNode):
    def __init__(self):
        self.num = -1
    
    def __str__(self):
        return "EXIT"
    
    def __repr__(self):
        return self.__str__()

    def __hash__(self):
        return hash((self.num))
    
    def __eq__(self, value):
        if not isinstance(value, EXIT):
            return NotImplemented
        
        return self.num == value.num
        

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
        return hash((self.num))
    
    def __eq__(self, value):
        if not isinstance(value, BlockID):
            return NotImplemented
        
        return self.num == value.num
    

class CFGNode():
    pass

class BasicBlock(CFGNode, DebugNode):

    def regenerateIMAP(self, instructions):

        newList = []
        for i in instructions:
            newList.append((i, set()))

        self.iMap = newList
        self.reachingCopies = set()

    def updateInstructions(self, instructions):
        self.instructions = instructions
        self.regenerateIMAP(self.instructions)

    def __init__(self, id, instructions):
        self.id = id
        self.predecessors = set()
        self.successors = set()
        self.updateInstructions(instructions)

    def __str__(self):
        return "{self.id}: {self.instructions} Pred: {self.predecessors} Suc: {self.successors} iMap: {self.iMap} ReachingCopies: {self.reachingCopies}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
    def printNode(self):
        output = ""

        output += self.id.printNode() + "\n\n"

        for i in self.instructions:
            output += i.printNode() + "\n"


        return output
    
    def __hash__(self):
        return hash((self.id))

    def __eq__(self, value):
        if not isinstance(value, BasicBlock):
            return NotImplemented
        
        return self.id == value.id


class Entry(CFGNode, DebugNode):

    def __init__(self):
        self.successors = set()
        self.id = ENTRY()

    def __str__(self):
        return "Entry: {self.id} {self.successors}".format(self=self)
    
    def __repr__(self):
        return self.__str__()
    
    def __hash__(self):
        return hash((self.id))

    def __eq__(self, value):
        if not isinstance(value, Entry):
            return NotImplemented
        
        return self.id == value.id

class Exit(CFGNode, DebugNode):

    def __init__(self):
        self.predecessors = set()
        self.id = EXIT()

    def __str__(self):
        return "Exit: {self.id} {self.predecessors}".format(self=self)
    
    def __hash__(self):
        return hash((self.id))

    def __eq__(self, value):
        if not isinstance(value, Exit):
            return NotImplemented
        
        return self.id == value.id


class G():
    def __init__(self):
        self.maxID = -1
        self.blocks = {}
        self.labels = {}


def isStatic(identifier, symbolTable):
    a = symbolTable[identifier]

    match a.attrs:
        case typeChecker.StaticAttributes(initialVal = initialVal, global_ = global_):
            return True
    
    return False

def isIntegerScalar(identifier, backendSymbolTable):
    a = backendSymbolTable[identifier]
    match a.assType:

        case assemblyGenerator.Byte():
            return True

        case assemblyGenerator.Longword():
            return True

        case assemblyGenerator.Quadword():
            return True

        case _:
            return False
        
def isDouble(identifier, backendSymbolTable):
    a = backendSymbolTable[identifier]
    match a.assType:

        case assemblyGenerator.Double():
            return True
        
        case _:
            return False

def addPseudoRegistersDouble(interferenceGraph, instructions, symbolTable, backendSymbolTable, aliasedVars):

    for i in instructions:
        match i:
            case assemblyGenerator.MovInstruction(assType = assType, sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)

            case assemblyGenerator.BinaryInstruction(operator = operator, assType = assType, src = src, dest = dest):
                if (
                    isinstance(src, assemblyGenerator.PseudoRegisterOperand) and
                    isDouble(src.pseudo, backendSymbolTable) and
                    (not tacGenerator.TAC_VariableValue(src.pseudo) in aliasedVars)
                    ):
                    interferenceGraph.nodes[src] = Node(src)

                if (isinstance(dest, assemblyGenerator.PseudoRegisterOperand) and
                    isDouble(dest.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(dest.pseudo) in aliasedVars)
                    ):
                    interferenceGraph.nodes[dest] = Node(dest)

            case assemblyGenerator.UnaryInstruction(operator = operator, assType = assType, dest = dest):
                if (
                    isinstance(dest, assemblyGenerator.PseudoRegisterOperand) and
                    isDouble(dest.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(dest.pseudo) in aliasedVars)

                    ):
                    interferenceGraph.nodes[dest] = Node(dest)

            case assemblyGenerator.CompInst(assType = assType, operand0 = operand0, operand1 = operand1):
                if (
                    isinstance(operand0, assemblyGenerator.PseudoRegisterOperand) and
                    isDouble(operand0.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand0.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand0] = Node(operand0)

                if (
                    isinstance(operand1, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(operand1.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand1.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand1] = Node(operand1)

            case assemblyGenerator.IDivInstruction(assType = assType, divisor = divisor):
                if (
                    isinstance(divisor, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(divisor.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(divisor.pseudo) in aliasedVars)
                    ):
                    interferenceGraph.nodes[divisor] = Node(divisor)

            case assemblyGenerator.SetCCInst(conc_code = conc_code, operand = operand):
                if (
                    isinstance(operand, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(operand.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand] = Node(operand)

            case assemblyGenerator.PushInstruction(operand = operand):
                if (
                    isinstance(operand, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(operand.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand] = Node(operand)



            case assemblyGenerator.MovSXInstruction(srcType = srcType, dstType = dstType,sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)

            
            case assemblyGenerator.MovZeroExtendIns(sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)


            case assemblyGenerator.LeaInstruction(sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)


            case assemblyGenerator.Cvttsd2si(assType = assType, sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)

            
            case assemblyGenerator.Cvtsi2sd(assType = assType, sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)


            case assemblyGenerator.DivInstruction(divisor = divisor):
                if (
                    isinstance(divisor, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(divisor.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(divisor.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[divisor] = Node(divisor)


            case assemblyGenerator.Pop(reg = reg):
                if (
                    isinstance(reg, assemblyGenerator.PseudoRegisterOperand) and 
                    isDouble(reg.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(reg.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[reg] = Node(reg)



def addPseudoRegistersIntegerScalar(interferenceGraph, instructions, symbolTable, backendSymbolTable, aliasedVars):

    for i in instructions:
        match i:
            case assemblyGenerator.MovInstruction(assType = assType, sourceO = sourceO, destO = destO):
                
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):
                    
                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)

            case assemblyGenerator.BinaryInstruction(operator = operator, assType = assType, src = src, dest = dest):
                if (
                    isinstance(src, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(src.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(src.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[src] = Node(src)

                if (
                    isinstance(dest, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(dest.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(dest.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[dest] = Node(dest)

            case assemblyGenerator.UnaryInstruction(operator = operator, assType = assType, dest = dest):

                if (
                    isinstance(dest, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(dest.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(dest.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[dest] = Node(dest)

            case assemblyGenerator.CompInst(assType = assType, operand0 = operand0, operand1 = operand1):

                if (
                    isinstance(operand0, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(operand0.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand0.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand0] = Node(operand0)

                if (
                    isinstance(operand1, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(operand1.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand1.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand1] = Node(operand1)

            case assemblyGenerator.IDivInstruction(assType = assType, divisor = divisor):

                if (
                    isinstance(divisor, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(divisor.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(divisor.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[divisor] = Node(divisor)

            case assemblyGenerator.SetCCInst(conc_code = conc_code, operand = operand):
                if (
                    isinstance(operand, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(operand.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand] = Node(operand)

            case assemblyGenerator.PushInstruction(operand = operand):
                if (
                    isinstance(operand, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(operand.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(operand.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[operand] = Node(operand)



            case assemblyGenerator.MovSXInstruction(srcType = srcType, dstType = dstType,sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)

            
            case assemblyGenerator.MovZeroExtendIns(sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)


            case assemblyGenerator.LeaInstruction(sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)


            case assemblyGenerator.Cvttsd2si(assType = assType, sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)

            
            case assemblyGenerator.Cvtsi2sd(assType = assType, sourceO = sourceO, destO = destO):
                if (
                    isinstance(sourceO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(sourceO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(sourceO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[sourceO] = Node(sourceO)

                if (
                    isinstance(destO, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(destO.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(destO.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[destO] = Node(destO)


            case assemblyGenerator.DivInstruction(divisor = divisor):
                if (
                    isinstance(divisor, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(divisor.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(divisor.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[divisor] = Node(divisor)


            case assemblyGenerator.Pop(reg = reg):
                if (
                    isinstance(reg, assemblyGenerator.PseudoRegisterOperand) and 
                    isIntegerScalar(reg.pseudo, backendSymbolTable) and 
                    (not tacGenerator.TAC_VariableValue(reg.pseudo) in aliasedVars)
                    ):

                    interferenceGraph.nodes[reg] = Node(reg)


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


def addAllEdgesToCFG(cfg):

    addEdge(ENTRY(), BlockID(0), cfg)

    for k, n in cfg.blocks.items():

        if k == ENTRY() or k == EXIT():
            continue
        
        #aqui ya estas trabajando con blockids!
        if n.id == BlockID(cfg.maxID):
            nextID = EXIT()
        else:
            nextID = BlockID(n.id.num + 1)

        i = n.instructions[-1]

        match i:

            case assemblyGenerator.ReturnInstruction():
                addEdge(n.id, EXIT(), cfg)

            case assemblyGenerator.JumpInst(identifier = identifier):
                obj = cfg.labels[identifier]
                addEdge(n.id, obj.id, cfg)

            case assemblyGenerator.JumpCCInst(conc_code = conc_code, identifier = identifier):
                obj = cfg.labels[identifier]
                addEdge(n.id, obj.id, cfg)
                addEdge(n.id, nextID, cfg)

            case _:
                addEdge(n.id, nextID, cfg)

    print("-------------CONNECTED BLOCKS-----------------")
    for k, n in cfg.blocks.items():
        print(k, n)    


def makeControlFlowGraph(functionBody):

    iBlocks = partitionIntoBasicBlocks(functionBody)

    g = G()

    g.blocks[ENTRY()] = Entry()

    g.maxID = len(iBlocks) - 1

    for i, instructions in enumerate(iBlocks):
        g.blocks[BlockID(i)] = BasicBlock(BlockID(i), instructions)

        probLabel = instructions[0]

        print(probLabel)

        match probLabel:
            case assemblyGenerator.LabelInst(identifier = identifier):
                g.labels[identifier] = BasicBlock(BlockID(i), instructions)

    g.blocks[EXIT()] = Exit()

    print("-------------LABELS-----------------")

    for k, w in g.labels.items():
        print(k,w)

    addAllEdgesToCFG(g)

    return g
    
def meetLive(n, cfg, funName, backendSymbolTable):
    liveVars = set()

    for sID in n.successors:
        match sID:
            case ENTRY():
                print("Error: Malformed control graph.")
                sys.exit(1)

            case EXIT():
                a = backendSymbolTable[funName]
                
                liveVars.update(a.returnInt)
                liveVars.update(a.returnDouble)

            case BlockID(num = num):
                node = cfg.blocks[sID]
                liveVars.update(node.reachingCopies)

    return liveVars

def findUsedAndUpdated(instruction, backendSymbolTable):
    used = []
    updated = []

    match instruction:
        case assemblyGenerator.MovInstruction(sourceO = sourceO, destO = destO):
            used = []
            updated = []

            match sourceO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(sourceO)

            match destO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(destO)

            #used = [sourceO]
            #updated = [destO]

        case assemblyGenerator.BinaryInstruction(src = src, dest = dest):
            
            used = []
            updated = []

            match src:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(src)
                    used.append(dest)

            match dest:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(dest)

            #used = [src, dest]
            #updated = [dest]

        case assemblyGenerator.UnaryInstruction(dest = dest):

            used = []
            updated = []

            match dest:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(dest)
                    updated.append(dest)

            #used = [dest]
            #updated = [dest]

        case assemblyGenerator.CompInst(operand0 = operand0, operand1 = operand1):

            used = []
            updated = []

            match operand0:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(operand0)
                    used.append(operand1)


            match operand1:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    pass

            #used = [operand0, operand1]
            #updated = []

        case assemblyGenerator.SetCCInst(operand = operand):

            used = []
            updated = []

            match operand:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(operand)

            #used = []
            #updated = [operand]
        
        case assemblyGenerator.PushInstruction(operand = operand):

            used = []
            updated = []

            match operand:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(operand)

            #used = [operand]
            #updated = []

        case assemblyGenerator.IDivInstruction(divisor = divisor):

            used = []
            updated = []

            match divisor:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.extend([divisor, RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))])

                    updated.extend([RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))])

            #used = [divisor, RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))]

            #updated = [RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))]

        case assemblyGenerator.CDQInstruction():
            used = [RegisterOperand(Register(RegisterType.AX))]
            updated = [RegisterOperand(Register(RegisterType.DX))]

        case assemblyGenerator.CallInstruction(identifier = identifier):

            funEntry = backendSymbolTable[identifier]
            
            used = list(funEntry.paramInt)

            updated = [
                        RegisterOperand(Register(RegisterType.DI)), 
                       RegisterOperand(Register(RegisterType.SI)), 
                       RegisterOperand(Register(RegisterType.DX)), 
                       RegisterOperand(Register(RegisterType.CX)), 
                       RegisterOperand(Register(RegisterType.R8)), 
                       RegisterOperand(Register(RegisterType.R9)), 
                       RegisterOperand(Register(RegisterType.AX)),

                       RegisterOperand(Register(SSERegisterType.XMM0)),
                       RegisterOperand(Register(SSERegisterType.XMM1)),
                       RegisterOperand(Register(SSERegisterType.XMM2)),
                       RegisterOperand(Register(SSERegisterType.XMM3)),
                       RegisterOperand(Register(SSERegisterType.XMM4)),
                       RegisterOperand(Register(SSERegisterType.XMM5)),
                       RegisterOperand(Register(SSERegisterType.XMM6)),
                       RegisterOperand(Register(SSERegisterType.XMM7)),
                       RegisterOperand(Register(SSERegisterType.XMM8)),
                       RegisterOperand(Register(SSERegisterType.XMM9)),
                       RegisterOperand(Register(SSERegisterType.XMM10)),
                       RegisterOperand(Register(SSERegisterType.XMM11)),
                       RegisterOperand(Register(SSERegisterType.XMM12)),
                       RegisterOperand(Register(SSERegisterType.XMM13)),
                       RegisterOperand(Register(SSERegisterType.XMM14)),
                       RegisterOperand(Register(SSERegisterType.XMM15))
                       ]

        case assemblyGenerator.MovSXInstruction(srcType = srcType, dstType = dstType,sourceO = sourceO, destO = destO):
            used = []
            updated = []

            match sourceO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(sourceO)

            match destO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(destO)
            
        
        case assemblyGenerator.MovZeroExtendIns(sourceO = sourceO, destO = destO):
            used = []
            updated = []

            match sourceO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(sourceO)

            match destO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(destO)
        
        case assemblyGenerator.LeaInstruction(sourceO = sourceO, destO = destO):
            used = []
            updated = []

            match sourceO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(sourceO)
                    
                    #print("ERROR: Invalid source operand for lea instruction. {0}".format(type(sourceO)))
                    #sys.exit(1)
                    #used.append(sourceO)

            match destO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(destO)

        case assemblyGenerator.Cvttsd2si(assType = assType, sourceO = sourceO, destO = destO):
            used = []
            updated = []

            match sourceO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(sourceO)

            match destO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(destO)

        case assemblyGenerator.Cvtsi2sd(assType = assType, sourceO = sourceO, destO = destO):
            used = []
            updated = []

            match sourceO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.append(sourceO)

            match destO:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    updated.append(destO)

        case assemblyGenerator.DivInstruction(divisor = divisor):
            used = []
            updated = []

            match divisor:
                case assemblyGenerator.MemoryOperand(reg = reg, int = int):
                    used.append(RegisterOperand(reg))

                case assemblyGenerator.Indexed(base = base, index = index, scale = scale):
                    used.append(RegisterOperand(base))
                    used.append(RegisterOperand(index))

                case _:
                    used.extend([divisor, RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))])

                    updated.extend([RegisterOperand(Register(RegisterType.AX)), RegisterOperand(Register(RegisterType.DX))])
        
        case assemblyGenerator.Pop(reg = reg):
            used = []
            updated = [reg]

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

#esta es la que va a cambiar!
def transferLive(block, endLiveRegisters, backendSymbolTable):

    print("--------------LIVE for block {0}-------------------".format(block.id))

    currentLiveRegisters = endLiveRegisters

    reversed = block.iMap[::-1]

    for i, set0 in reversed:

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

    #print("--------------ACTUALIZED IMAP for block {0}-------------------".format(block.id))

    #for i, set0 in block.iMap:
    #    print(i, set0)

    block.reachingCopies.clear()
    block.reachingCopies.update(currentLiveRegisters)

def analyzeLiveness(cfg, backendSymbolTable, funName):
    workList = []

    a = list(cfg.blocks.items())
    a.reverse()

    for k, n in a:
        if k == ENTRY() or k == EXIT():
            continue
        
        workList.append(n)
        n.reachingCopies.clear()


    while workList != []:
        n = workList.pop(0)
        
        oldAnnot = copy.deepcopy(n.reachingCopies)

        liveVars = meetLive(n, cfg, funName, backendSymbolTable)
        transferLive(n, liveVars, backendSymbolTable)

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
    

def addEdges(cfg, interferenceGraph, backendSymbolTable):
    print("-----------Adding edges to interference graph.------------------")

    for k, n in cfg.blocks.items():
        if k == ENTRY() or k == EXIT():
            continue
        
        for i, set0 in n.iMap:

            used, updated = findUsedAndUpdated(i, backendSymbolTable)

            for l in set0:
                if isinstance(i, assemblyGenerator.MovInstruction) and l == i.sourceO:
                    continue

                for u in updated:
                    if l in interferenceGraph.nodes and u in interferenceGraph.nodes and not (l == u):
                        interferenceGraph.addEdge(l, u)
                 
                
def addEdge(nodeID0, nodeID1, graph):

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
        
    

def buildInterferenceGraphInteger(instructions, symbolTable, backendSymbolTable, aliasedVars, funName):

    print("-----------Building INTEGER interference graph.------------------")

    interferenceGraph = IntegerBaseGraph()

    addPseudoRegistersIntegerScalar(interferenceGraph, instructions, symbolTable, backendSymbolTable, aliasedVars)

    ########################### es diferente

    cfg = makeControlFlowGraph(instructions)

    analyzeLiveness(cfg, backendSymbolTable, funName)

    addEdges(cfg, interferenceGraph, backendSymbolTable)

    interferenceGraph.printNode(0)

    return interferenceGraph

def buildInterferenceGraphDouble(instructions, symbolTable, backendSymbolTable, aliasedVars, funName):

    print("-----------Building DOUBLE interference graph.------------------")

    interferenceGraph = DoubleBaseGraph()

    addPseudoRegistersDouble(interferenceGraph, instructions, symbolTable, backendSymbolTable, aliasedVars)

    ########################### es diferente

    cfg = makeControlFlowGraph(instructions)

    analyzeLiveness(cfg, backendSymbolTable, funName)

    addEdges(cfg, interferenceGraph, backendSymbolTable)

    interferenceGraph.printNode(0)

    return interferenceGraph

def addSpillCostsToPseudos(interGraph, instructions):
    for k,n in interGraph.nodes.items():
        match k:
            case assemblyGenerator.PseudoRegisterOperand():

                spillCost = 0.0

                for i in instructions:

                    match i:

                        case assemblyGenerator.MovInstruction(sourceO = sourceO, destO = destO):

                            if sourceO == k:
                                spillCost += 1.0

                            if destO == k:
                                spillCost += 1.0

                        case assemblyGenerator.BinaryInstruction(src = src, dest = dest):
                            if src == k:
                                spillCost += 1.0

                            if dest == k:
                                spillCost += 1.0
                            

                        case assemblyGenerator.UnaryInstruction(dest = dest):
                            if dest == k:
                                spillCost += 1.0

                        case assemblyGenerator.CompInst(operand0 = operand0, operand1 = operand1):
                            if operand0 == k:
                                spillCost += 1.0

                            if operand1 == k:
                                spillCost += 1.0
                            pass

                        case assemblyGenerator.SetCCInst(operand = operand):
                            if operand == k:
                                spillCost += 1.0


                        case assemblyGenerator.PushInstruction(operand = operand):
                            if operand == k:
                                spillCost += 1.0

                        case assemblyGenerator.IDivInstruction(divisor = divisor):
                            if divisor == k:
                                spillCost += 1.0

                        case assemblyGenerator.MovSXInstruction(sourceO = sourceO, destO = destO):
                            if sourceO == k:
                                spillCost += 1.0

                            if destO == k:
                                spillCost += 1.0
                        
                        case assemblyGenerator.MovZeroExtendIns(sourceO = sourceO, destO = destO):
                            if sourceO == k:
                                spillCost += 1.0

                            if destO == k:
                                spillCost += 1.0
                        
                        case assemblyGenerator.LeaInstruction(sourceO = sourceO, destO = destO):
                            if sourceO == k:
                                spillCost += 1.0

                            if destO == k:
                                spillCost += 1.0

                        case assemblyGenerator.Cvttsd2si(sourceO = sourceO, destO = destO):
                            if sourceO == k:
                                spillCost += 1.0

                            if destO == k:
                                spillCost += 1.0

                        case assemblyGenerator.Cvtsi2sd(sourceO = sourceO, destO = destO):
                            if sourceO == k:
                                spillCost += 1.0

                            if destO == k:
                                spillCost += 1.0

                        case assemblyGenerator.DivInstruction(divisor = divisor):
                            if divisor == k:
                                spillCost += 1.0
                        
                        case assemblyGenerator.Pop(reg = reg):
                            if reg == k:
                                spillCost += 1.0

                n.spillCost = spillCost

def addSpillCostsInteger(interGraph, instructions):
    print("----------------ADD SPILL COSTS INTEGER.-------------------")

    interGraph.nodes[RegisterOperand(Register(RegisterType.AX))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.BX))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.CX))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.DX))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.DI))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.SI))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.R8))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.R9))].spillCost = float('inf')  
    interGraph.nodes[RegisterOperand(Register(RegisterType.R12))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(RegisterType.R13))].spillCost = float('inf')
    interGraph.nodes[RegisterOperand(Register(RegisterType.R14))].spillCost = float('inf')
    interGraph.nodes[RegisterOperand(Register(RegisterType.R15))].spillCost = float('inf')

    #pseudoregisters

    addSpillCostsToPseudos(interGraph, instructions)

    for k,n in interGraph.nodes.items():
        print(k,n)


def addSpillCostsDouble(interGraph, instructions):
    print("----------------ADD SPILL COSTS DOUBLE.-------------------")

    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM0))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM1))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM2))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM3))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM4))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM5))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM6))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM7))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM8))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM9))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM10))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM11))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM12))].spillCost = float('inf') 
    interGraph.nodes[RegisterOperand(Register(SSERegisterType.XMM13))].spillCost = float('inf') 
    
    
    addSpillCostsToPseudos(interGraph, instructions)

    for k,n in interGraph.nodes.items():
        print(k,n)
    
def getUnprunedNeighborsofNode(node, interGraph):
    unPrunedList = []
    
    for k in node.neighbors:
        node = interGraph.nodes[k]
        if node.pruned == False:
            unPrunedList.append(node)
    
    return unPrunedList


def isCalleeSavedHardRegInt(operandID):

    if isinstance(operandID, RegisterOperand):

        match operandID.register.register:
            case RegisterType.BX:
                return True

            case RegisterType.R12:
                return True

            case RegisterType.R13:
                return True
            
            case RegisterType.R14:
                return True

            case RegisterType.R15:
                return True
            
            case _:
                return False

    return False

def colorGraphInteger(interGraph, backendSymbolTable, funName):
    print("------------------COLOR GRAPH INTEGER.---------------------")
    

    remainingNodes = [n for k,n in interGraph.nodes.items() if n.pruned == False] 
    
    k = 12

    print("Reamining Nodes:", remainingNodes)

    if remainingNodes == []:
        return 
    

    chosenNode = None

    for node in remainingNodes:

        degree = len(getUnprunedNeighborsofNode(node, interGraph))

        if degree < k:
            chosenNode = node
            break

    if chosenNode == None:

        bestSpillMetric = float('inf')

        for node in remainingNodes:
            degree = len(getUnprunedNeighborsofNode(node, interGraph))

            spillMetric = node.spillCost / degree

            if spillMetric < bestSpillMetric:
                chosenNode = node
                bestSpillMetric = spillMetric
        

    chosenNode.pruned = True


    colorGraphInteger(interGraph, backendSymbolTable, funName)
    #el ultimo que fue pruneado va a ser el primero que va a ser coloreado!

    colors = set(range(1, k + 1))

    print(colors)

    for nID in chosenNode.neighbors:

        node = interGraph.nodes[nID]

        if node.color:
            colors.discard(node.color)

    if colors != set():
        if isCalleeSavedHardRegInt(chosenNode.operandID):
            chosenNode.color = max(colors)
        else:
            chosenNode.color = min(colors)

        chosenNode.pruned = False

    return

def colorGraphDouble(interGraph, backendSymbolTable, funName):

    print("------------------COLOR GRAPH DOUBLE.---------------------")
    

    remainingNodes = [n for k,n in interGraph.nodes.items() if n.pruned == False] 
    
    k = 14

    print("Reamining Nodes:", remainingNodes)

    if remainingNodes == []:
        return 
    

    chosenNode = None

    for node in remainingNodes:

        degree = len(getUnprunedNeighborsofNode(node, interGraph))

        if degree < k:
            chosenNode = node
            break

    if chosenNode == None:

        bestSpillMetric = float('inf')

        for node in remainingNodes:
            degree = len(getUnprunedNeighborsofNode(node, interGraph))

            spillMetric = node.spillCost / degree

            if spillMetric < bestSpillMetric:
                chosenNode = node
                bestSpillMetric = spillMetric
        

    chosenNode.pruned = True

    colorGraphDouble(interGraph, backendSymbolTable, funName)

    #el ultimo que fue pruneado va a ser el primero que va a ser coloreado!

    colors = set(range(1, k + 1))

    print(colors)

    for nID in chosenNode.neighbors:

        node = interGraph.nodes[nID]

        if node.color:
            colors.discard(node.color)

    if colors != set():
        chosenNode.color = min(colors)
        chosenNode.pruned = False

    return


def createRegisterMap(coloredGraph, backendSymbolTable, funName):
    print("---------------CREATE REGISTER MAP.-------------------")

    colorMap = {}
    for k,n in coloredGraph.nodes.items():

        match n.operandID:
            case RegisterOperand(register = register):
                colorMap[n.color] = n.operandID

            case assemblyGenerator.PseudoRegisterOperand():
                continue
    
    print(colorMap)

    calleeSavedRegs = set()
    registerMap = {}
    for k,n in coloredGraph.nodes.items():
        
        match n.operandID:
            case assemblyGenerator.PseudoRegisterOperand(pseudo = pseudo):
                if n.color:
                    hardReg = colorMap[n.color]
                    registerMap[n.operandID] = hardReg

                    if isCalleeSavedHardRegInt(hardReg):
                        calleeSavedRegs.add(hardReg)

            case RegisterOperand(register = register):
                continue
    
    a = backendSymbolTable[funName]
    a.calleeSavedRegs.update(calleeSavedRegs)

    print("Calle Saved Registers for {0}: {1}".format(funName, a.calleeSavedRegs))
    return registerMap
            
        
    

def replacePseudoRegs(instructions, registerMap):

    for i in instructions:

        match i:

            case assemblyGenerator.MovInstruction(sourceO = sourceO, destO = destO):

                if isinstance(sourceO, PseudoRegisterOperand) and sourceO in registerMap:
                    i.sourceO = registerMap[sourceO]
                
                if isinstance(destO, PseudoRegisterOperand) and destO in registerMap:
                    i.destO = registerMap[destO]

            case assemblyGenerator.BinaryInstruction(src = src, dest = dest):
                if isinstance(src, PseudoRegisterOperand) and src in registerMap:
                    i.src = registerMap[src]
                
                if isinstance(dest, PseudoRegisterOperand) and dest in registerMap:
                    i.dest = registerMap[dest]

            case assemblyGenerator.UnaryInstruction(dest = dest):
                if isinstance(dest, PseudoRegisterOperand) and dest in registerMap:
                    i.dest = registerMap[dest]

            case assemblyGenerator.CompInst(operand0 = operand0, operand1 = operand1):
                if isinstance(operand0, PseudoRegisterOperand) and operand0 in registerMap:
                    i.operand0 = registerMap[operand0]
                
                if isinstance(operand1, PseudoRegisterOperand) and operand1 in registerMap:
                    i.operand1 = registerMap[operand1]

            case assemblyGenerator.SetCCInst(operand = operand):
                if isinstance(operand, PseudoRegisterOperand) and operand in registerMap:
                    i.operand = registerMap[operand]
            
            case assemblyGenerator.PushInstruction(operand = operand):
                if isinstance(operand, PseudoRegisterOperand) and operand in registerMap:
                    i.operand = registerMap[operand]

            case assemblyGenerator.IDivInstruction(divisor = divisor):
                if isinstance(divisor, PseudoRegisterOperand) and divisor in registerMap:
                    i.divisor = registerMap[divisor]

            case assemblyGenerator.MovSXInstruction(sourceO = sourceO, destO = destO):
                if isinstance(sourceO, PseudoRegisterOperand) and sourceO in registerMap:
                    i.sourceO = registerMap[sourceO]
                
                if isinstance(destO, PseudoRegisterOperand) and destO in registerMap:
                    i.destO = registerMap[destO]
                            
            case assemblyGenerator.MovZeroExtendIns(sourceO = sourceO, destO = destO):
                if isinstance(sourceO, PseudoRegisterOperand) and sourceO in registerMap:
                    i.sourceO = registerMap[sourceO]
                
                if isinstance(destO, PseudoRegisterOperand) and destO in registerMap:
                    i.destO = registerMap[destO]
            
            case assemblyGenerator.LeaInstruction(sourceO = sourceO, destO = destO):
                if isinstance(sourceO, PseudoRegisterOperand) and sourceO in registerMap:
                    i.sourceO = registerMap[sourceO]
                
                if isinstance(destO, PseudoRegisterOperand) and destO in registerMap:
                    i.destO = registerMap[destO]

            case assemblyGenerator.Cvttsd2si(sourceO = sourceO, destO = destO):
                if isinstance(sourceO, PseudoRegisterOperand) and sourceO in registerMap:
                    i.sourceO = registerMap[sourceO]
                
                if isinstance(destO, PseudoRegisterOperand) and destO in registerMap:
                    i.destO = registerMap[destO]

            case assemblyGenerator.Cvtsi2sd(sourceO = sourceO, destO = destO):
                if isinstance(sourceO, PseudoRegisterOperand) and sourceO in registerMap:
                    i.sourceO = registerMap[sourceO]
                
                if isinstance(destO, PseudoRegisterOperand) and destO in registerMap:
                    i.destO = registerMap[destO]

            case assemblyGenerator.DivInstruction(divisor = divisor):
                if isinstance(divisor, PseudoRegisterOperand) and divisor in registerMap:
                    i.divisor = registerMap[divisor]
            
            case assemblyGenerator.Pop(reg = reg):
                if isinstance(reg, PseudoRegisterOperand) and reg in registerMap:
                    i.reg = registerMap[reg]

    #REMOVE ANY MOV INSTRU

    newList = []
    for i in instructions:

        match i:

            case assemblyGenerator.MovInstruction(sourceO = sourceO, destO = destO):
                if sourceO == destO:
                    pass
                else:
                    newList.append(i)

            case _:
                newList.append(i)

    return newList

def initDisjointSets():
    return {}

def find(r, regMap):
    if r in regMap:
        mapping = regMap[r]
        result = find(mapping, regMap)
        return result

    return r

def union(x, y, regMap):
    regMap[x] = y

def nothingWasCoalesced(regMap):
    if regMap == {}:
        return True
    
    return False

"""
def areNeighbors(interGraph, src, dst):
    if dst in interGraph.nodes[src].neighbors or src in interGraph.nodes[dst].neighbors:
        return True
    
    return False

def notAreNeighbors(interGraph, src, dst):
    if dst in interGraph.nodes[src].neighbors or src in interGraph.nodes[dst].neighbors:
        return False
    
    return True
"""

"""
def briggsTestDouble(interGraph, x, y):
    k = 12
    significantNeighbors = 0

    xNode = interGraph.nodes[x]
    yNode = interGraph.nodes[y]

    allNeighbors = xNode.neighbors | yNode.neighbors


    for nID in allNeighbors:
        node = interGraph.nodes[nID]
        
        degree = len(node.neighbors)
        if areNeighbors(interGraph, nID, x) and areNeighbors(interGraph, nID, y):
            degree -= 1
            
        if degree >= k:
            significantNeighbors += 1

    return significantNeighbors < k


def briggsTestInteger(interGraph, x, y):
    k = 12
    significantNeighbors = 0

    xNode = interGraph.nodes[x]
    yNode = interGraph.nodes[y]

    allNeighbors = xNode.neighbors | yNode.neighbors


    for nID in allNeighbors:
        node = interGraph.nodes[nID]

        degree = len(node.neighbors)
        if areNeighbors(interGraph, nID, x) and areNeighbors(interGraph, nID, y):
            degree -= 1
            
        if degree >= k:
            significantNeighbors += 1

    return significantNeighbors < k
"""

def georgeTest(interGraph, src, dst):
    pass

def conservativeCoalesceable(interGraph, src, dst):
    if interGraph.briggsTest(src, dst):
        return True
    
    if isinstance(src, RegisterOperand):
        return georgeTest(interGraph, src, dst)
    
    if isinstance(dst, RegisterOperand):
        return georgeTest(interGraph, dst, src)
    
    return False


def updateGraph(interGraph, x, y):
    node = interGraph.nodes[x]
    
    nodesToRemove = set()
    for nodeID in node.neighbors:
        interGraph.addEdge(y, nodeID)
        interGraph.removeEdge(x, nodeID)

    del interGraph.nodes[x]
    

        

def coalesce(interGraph, instructions):

    coalescedRegs = initDisjointSets()

    for i in instructions:
        match i:
            case assemblyGenerator.MovInstruction(sourceO = sourceO, destO = destO):
                src = find(sourceO, coalescedRegs)
                dst = find(destO, coalescedRegs)

                if (src in interGraph.nodes and 
                    dst in interGraph.nodes and 
                    not (src == dst) and 
                    not interGraph.areNeighbors(src, dst) and 
                    conservativeCoalesceable(interGraph, src, dst)
                    ):

                    #AQui ya sabes que son pseudos

                    if isinstance(src, RegisterOperand):
                        toKeep = src
                        toMerge = dst
                    else:
                        toKeep = dst
                        toMerge = src

                    print("COALESCING {0} INTO {1}".format(toMerge, toKeep))

                    union(toMerge, toKeep, coalescedRegs)
                    updateGraph(interGraph, toMerge, toKeep)

            case _:
                continue

    return coalescedRegs

def rewriteCoalesced(instructions, coalescedRegs):
    return instructions

def allocateRegistersForInteger(instructions, symbolTable, backendSymbolTable, aliasedVars, funName):

    oldInstructions = copy.deepcopy(instructions)

    while True:

        interGraph = buildInterferenceGraphInteger(instructions, symbolTable, backendSymbolTable, aliasedVars, funName)
        coalescedRegs = coalesce(interGraph, instructions)
        
        if nothingWasCoalesced(coalescedRegs):
            break

        instructions = rewriteCoalesced(instructions, coalescedRegs)


    addSpillCostsInteger(interGraph, instructions)

    colorGraphInteger(interGraph, backendSymbolTable, funName)

    print("-----------------COLORED INTEGER INTER GRAPH.------------------")

    for k, n in interGraph.nodes.items():
        print(k,n)

    registerMap = createRegisterMap(interGraph, backendSymbolTable, funName)

    print("------------------REGISTER INTEGER MAP.--------------------")

    print(registerMap)

    replacedIns = replacePseudoRegs(instructions, registerMap)

    print("------------------REPLACED INTEGER INTRUCTIONS.--------------------")

    for n, o in zip(replacedIns, oldInstructions):
        print("{:<70} {:<1}".format(str(n), str(o)))

    return replacedIns

def allocateRegistersForDouble(instructions, symbolTable, backendSymbolTable, aliasedVars, funName):

    oldInstructions = copy.deepcopy(instructions)

    interGraph = buildInterferenceGraphDouble(instructions, symbolTable, backendSymbolTable, aliasedVars, funName)

    addSpillCostsDouble(interGraph, instructions)

    colorGraphDouble(interGraph, backendSymbolTable, funName)

    print("-----------------COLORED DOUBLE INTER GRAPH.------------------")

    for k, n in interGraph.nodes.items():
        print(k,n)

    registerMap = createRegisterMap(interGraph, backendSymbolTable, funName)

    print("------------------REGISTER DOUBLE MAP.--------------------")

    print(registerMap)

    replacedIns = replacePseudoRegs(instructions, registerMap)

    print("------------------REPLACED DOUBLE INTRUCTIONS.--------------------")

    for n, o in zip(replacedIns, oldInstructions):
        print("{:<70} {:<1}".format(str(n), str(o)))

    return replacedIns


def allocateRegisters(instructions, symbolTable, backendSymbolTable, aliasedVars, funName):

    instructions = allocateRegistersForInteger(instructions, symbolTable, backendSymbolTable, aliasedVars, funName)

    instructions = allocateRegistersForDouble(instructions, symbolTable, backendSymbolTable, aliasedVars, funName)

    return instructions
