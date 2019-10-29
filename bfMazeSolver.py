#!/usr/bin/env python3

from minPrior import MinPriorQueue

wall = 'x'

class Maze:
    def __init__(self,start,grid):
        self.start = start
        self.grid = grid
        self.correct_path = []
        self.adjacentNodes = MinPriorQueue()
        self.inQueueGrid = []
        self.solved = False

    def solve(self):
        if self.solved:
            return self.correct_path
        self.inQueueGrid = []
        for row in range(len(self.grid)):
            self.inQueueGrid.append([])
            for col in range(len(self.grid[row])):
                self.inQueueGrid[row].append(False)
        self.inQueueGrid[self.start[1]][self.start[0]] = self.start
        self.adjacentNodes.add(0,self.start)
        while not self.adjacentNodes.isEmpty():
            node = self.adjacentNodes.pop()
            if self.onEdge(*node.value):
                node = node.value
                while node != self.inQueueGrid[node[1]][node[0]]:
                    self.correct_path.append(node)
                    node = self.inQueueGrid[node[1]][node[0]]
                self.correct_path.append(node)
                self.correct_path.reverse()
                self.solved = True
                return self.correct_path
            self.addAdjacentNodes(*node.value,node.priority)
        self.solved = True
        return self.correct_path

    def addAdjacentNodes(self,x,y,d):
        thisNode = (x,y)
        nodesToAdd = []
        if self.isViable(*getUp(x,y)):
            up = getUp(x,y)
            nodesToAdd.append(up)
            self.inQueueGrid[up[1]][up[0]] = thisNode
        if self.isViable(*getDown(x,y)):
            down = getDown(x,y)
            nodesToAdd.append(down)
            self.inQueueGrid[down[1]][down[0]] = thisNode
        if self.isViable(*getLeft(x,y)):
            left = getLeft(x,y)
            nodesToAdd.append(left)
            self.inQueueGrid[left[1]][left[0]] = thisNode
        if self.isViable(*getRight(x,y)):
            right = getRight(x,y)
            nodesToAdd.append(right)
            self.inQueueGrid[right[1]][right[0]] = thisNode
        self.adjacentNodes.addAll(d+1,nodesToAdd)
        

    def isViable(self,x,y):
        return self.isOpen(x,y) and not self.inQueueGrid[y][x]

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

grid0 = [['x','x','x','x','x'],
         ['x',' ',' ',' ','x'],
         ['x',' ','x',' ','x'],
         ['x',' ','x',' ','x'],
         ['x','x',' ',' ','x'],
         ['x','x',' ','x','x'],
         ['x',' ',' ',' ','x'],
         ['x','x','x',' ','x']]
grid0Start = (1,1)

expectedPath0 = [grid0Start,(2,1),(3,1),(3,2),(3,3),(3,4),(2,4),(2,5),(2,6),(3,6),(3,7)]

maze = Maze(grid0Start,grid0)
actualPath0 = maze.solve()
print("Expected Path for Maze0 == Actual Path: " + str(expectedPath0==actualPath0))
print(actualPath0)

grid1 = [['x','x','x','x','x'],
         ['x',' ',' ',' ','x'],
         ['x',' ','x',' ','x'],
         ['x',' ','x','x','x'],
         ['x','x',' ',' ','x'],
         ['x','x',' ','x','x'],
         ['x',' ',' ',' ','x'],
         ['x','x','x',' ','x']]
grid1Start = (1,1)

maze1 = Maze(grid1Start,grid1)
expectedPath1 = []
actualPath1 = maze1.solve()

print("Expected Path for Maze1 == Actual Path: " + str(expectedPath1 == actualPath1))
print(actualPath1)