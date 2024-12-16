from src.window import Window
from src.point import Point
from src.maze import Maze

if __name__ == "__main__":
    window = Window(800, 600, "PyMaze")
    maze = Maze(window, Point(10, 10), rows=26, cols=19, cell_size=30)
    print(maze.solve())
    window.wait_for_close()
