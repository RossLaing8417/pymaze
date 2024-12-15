from src.point import Point
from src.maze import Maze

import unittest


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        rows = 10
        cols = 12
        maze = Maze(Point(0, 0), rows, cols, 10)
        self.assertEqual(len(maze.cells()), rows)
        self.assertEqual(len(maze.cells()[0]), cols)


if __name__ == "__main__":
    unittest.main()
