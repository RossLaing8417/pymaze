from src.window import Window
from src.point import Point
from src.cell import Cell
from src.line import Line
from src.maze import Maze

if __name__ == "__main__":
    window = Window(800, 600, "PyMaze")
    Line(Point(100, 100), Point(700, 500)).draw(window, "black")
    Cell(Point(200, 200), Point(600, 400)).draw(window, "black")
    cell1 = Cell(Point(350, 50), Point(400, 100))
    cell2 = Cell(Point(400, 50), Point(450, 100))
    cell3 = Cell(Point(350, 100), Point(450, 150))
    cell1.draw(window, "black")
    cell2.draw(window, "black")
    cell3.draw(window, "black")
    cell1.draw_move(window, cell2)
    cell1.draw_move(window, cell3, True)
    cell2.draw_move(window, cell3, True)
    maze = Maze(window, Point(10, 10), 10, 10, 10, 69)
    window.wait_for_close()
