#!/usr/bin/env python3

from minPrior import MinPriorQueue

wall = 'x'

class Maze:
    def __init__(self,start,grid):
        self.start = start
        self.grid = grid
        self.correct_path = []
        self.adjacentCells = MinPriorQueue()
        self.parentCellDict = { start: start }
        self.solved = False

    def solve(self):
        if self.solved:
            return self.correct_path
        self.adjacentCells.add(0,self.start)
        while not self.adjacentCells.isEmpty():
            cellNode = self.adjacentCells.pop()
            if self.onEdge(*cellNode.value):
                cell = cellNode.value
                while cell in self.parentCellDict and cell != self.parentCellDict[cell]:
                    self.correct_path.append(cell)
                    cell = self.parentCellDict[cell]
                self.correct_path.append(cell)
                self.correct_path.reverse()
                self.solved = True
                return self.correct_path
            self.addAdjacentCells(*cellNode.value,cellNode.priority)
        self.solved = True
        return self.correct_path

    def addAdjacentCells(self,x,y,d):
        thisCell = (x,y)
        viableCells = list(filter(lambda n: self.isViable(*n), [getUp(x,y),getDown(x,y),getLeft(x,y), getRight(x,y)]))
        for cell in viableCells:
            self.parentCellDict[cell] = thisCell
        self.adjacentCells.addAll(d+1,viableCells)
        

    def isViable(self,x,y):
        return self.isOpen(x,y) and not (x,y) in self.parentCellDict

    def onEdge(self,x,y):
        return x == 0 or y == 0 or x == len(self.grid[0])-1 or y == len(self.grid)-1

    def withinGrid(self,x,y):
        return (x >= 0 and y >= 0) and (x < len(self.grid[0]) and y < len(self.grid))

    def isOpen(self,x,y):
        if self.withinGrid(x,y) or self.onEdge(x,y):
            return wall != self.grid[y][x]

def getUp(x,y):
    return (x,y-1)

def getDown(x,y):
    return (x,y+1)

def getLeft(x,y):
    return (x-1,y)

def getRight(x,y):
    return (x+1,y)