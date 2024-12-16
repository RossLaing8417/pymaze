from src.point import Point
from src.maze import Maze

import unittest


class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        rows = 10
        cols = 12
        maze = Maze(None, Point(0, 0), rows, cols, 10)
        self.assertEqual(len(maze.cells), cols)
        self.assertEqual(len(maze.cells[0]), rows)

    def test_maze_entrance_and_exit(self):
        maze = Maze(None, Point(0, 0), 10, 10, 10)
        self.assertFalse(maze.cells[0][0].top)
        self.assertFalse(maze.cells[9][9].top)

    def test_maze_reset_visited(self):
        rows = 10
        cols = 10
        maze = Maze(None, Point(0, 0), rows, cols, 10, 0)
        for row in maze.cells:
            for cell in row:
                self.assertFalse(cell.visited)


if __name__ == "__main__":
    unittest.main()
