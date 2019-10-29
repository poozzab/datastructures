#!/usr/bin/env python3

from bfMazeSolver import Maze

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