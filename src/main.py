from window import Window
from point import Point
from cell import Cell
from line import Line

if __name__ == "__main__":
    win = Window(800, 600, "PyMaze")
    win.draw_line(Line(Point(100, 100), Point(700, 500)), "black")
    win.draw_cell(Cell(Point(200, 200), Point(600, 400)), "black")
    win.draw_cell(Cell(Point(300, 275), Point(500, 325),
                  top=True, bottom=False, left=False, right=False), "red")
    win.draw_cell(Cell(Point(300, 275), Point(500, 325),
                  top=False, bottom=True, left=False, right=False), "green")
    win.draw_cell(Cell(Point(300, 275), Point(500, 325),
                  top=False, bottom=False, left=True, right=False), "blue")
    win.draw_cell(Cell(Point(300, 275), Point(500, 325),
                  top=False, bottom=False, left=False, right=True), "pink")
    win.wait_for_close()
