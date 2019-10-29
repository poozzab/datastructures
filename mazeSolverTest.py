#!/usr/bin/env python3

import unittest
from mazeSolver import Maze

class TestMazeSolver(unittest.TestCase):
    def test_mazeWithPathToExit_findsExit(self):
        grid = [['x','x','x','x','x'],
                ['x',' ',' ',' ','x'],
                ['x',' ','x',' ','x'],
                ['x',' ','x',' ','x'],
                ['x','x',' ',' ','x'],
                ['x','x',' ','x','x'],
                ['x',' ',' ',' ','x'],
                ['x','x','x',' ','x']]
        gridStart = (1,1)
        expectedPath = [gridStart,(2,1),(3,1),(3,2),(3,3),(3,4),(2,4),(2,5),(2,6),(3,6),(3,7)]

        maze = Maze(gridStart,grid)

        actualPath = maze.solve()
        self.assertEqual(actualPath, expectedPath)

    def test_mazeWithoutPathToExit_emptyPath(self):
        grid = [['x','x','x','x','x'],
                ['x',' ',' ',' ','x'],
                ['x',' ','x',' ','x'],
                ['x',' ','x','x','x'],
                ['x','x',' ',' ','x'],
                ['x','x',' ','x','x'],
                ['x',' ',' ',' ','x'],
                ['x','x','x',' ','x']]
        gridStart = (1,1)
        expectedPath = []

        maze = Maze(gridStart,grid)

        actualPath = maze.solve()
        self.assertEqual(actualPath,expectedPath)

if __name__=='__main__':
    unittest.main()