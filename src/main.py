from window import Window
from point import Point
from line import Line

if __name__ == "__main__":
    win = Window(800, 600, "PyMaze")
    win.draw_line(Line(Point(100, 100), Point(700, 500)), "black")
    win.wait_for_close()
