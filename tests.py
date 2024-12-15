from .src.maze import Maze

import unittest


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        rows = 10
        cols = 12
        maze = Maze(0, 0, rows, cols, 10)
        self.assertEqual(len(maze.__cells), rows)
        self.assertEqual(len(maze.__cells[0]), cols)


if __name__ == "__main__":
    unittest.main()
