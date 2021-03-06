#!/usr/bin/env python3

wall = 'x'

class Maze:
    def __init__(self,start,grid):
        self.start = start
        self.grid = grid
        self.correctPath = []
        self.solved = False

    def solve(self):
        if self.solved:
            return self.correctPath
        # to help solve the maze, keep track of where we've been
        self.wasHere = []
        for row in range(len(self.grid)):
            self.wasHere.append([])
            for col in range(len(self.grid[row])):
                self.wasHere[row].append(False)
        solution = self.recursiveSolveMaze(*self.start)
        self.solved = True
        if solution:
            self.correctPath.reverse()
        return self.correctPath
    
    def recursiveSolveMaze(self,x,y):
        self.wasHere[y][x] = True
        if self.onEdge(x,y) and self.isOpen(x,y):
            self.correctPath.append((x,y))
            return True
        if self.canGo(up(x,y)):
            if self.recursiveSolveMaze(*up(x,y)):
                self.correctPath.append((x,y))
                return True
        if self.canGo(left(x,y)):
            if self.recursiveSolveMaze(*left(x,y)):
                self.correctPath.append((x,y))
                return True
        if self.canGo(right(x,y)):
            if self.recursiveSolveMaze(*right(x,y)):
                self.correctPath.append((x,y))
                return True
        if self.canGo(down(x,y)):
            if self.recursiveSolveMaze(*down(x,y)):
                self.correctPath.append((x,y))
                return True
        return False

    def onEdge(self,x,y):
        return x == 0 or y == 0 or x == len(self.grid[0])-1 or y == len(self.grid)-1

    def withinGrid(self,x,y):
        return (x >= 0 and y >= 0) and (x < len(self.grid[0]) and y < len(self.grid))

    def isOpen(self,x,y):
        if self.withinGrid(x,y) or self.onEdge(x,y):
            return wall != self.grid[y][x]

    def canGo(self,xyPair):
        return ( self.onEdge(*xyPair) or self.withinGrid(*xyPair) ) and self.isOpen(*xyPair) and not self.wasHere[xyPair[1]][xyPair[0]]

def up(x,y):
    return (x,y-1)

def down(x,y):
    return (x,y+1)

def left(x,y):
    return (x-1,y)

def right(x,y):
    return (x+1,y)