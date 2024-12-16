from src.window import Window
from src.point import Point
from src.line import Line


class Cell:
    def __init__(
            self,
            p1: Point,
            p2: Point,
            top: bool = True,
            bottom: bool = True,
            left: bool = True,
            right: bool = True
    ):
        self.p1: Point = p1
        self.p2: Point = p2
        self.top: bool = top
        self.bottom: bool = bottom
        self.left: bool = left
        self.right: bool = right
        self.visited: bool = False

    def draw(self, window: Window, fill_color: str):
        Line(Point(self.p1.x, self.p1.y),
             Point(self.p2.x, self.p1.y)).draw(
            window,
            fill_color if self.top else "white"
        )
        Line(Point(self.p1.x, self.p2.y),
             Point(self.p2.x, self.p2.y)).draw(
            window,
            fill_color if self.bottom else "white"
        )
        Line(Point(self.p1.x, self.p1.y),
             Point(self.p1.x, self.p2.y)).draw(
            window,
            fill_color if self.left else "white"
        )
        Line(Point(self.p2.x, self.p1.y),
             Point(self.p2.x, self.p2.y)).draw(
            window,
            fill_color if self.right else "white"
        )

    def draw_move(self, window, target, undo=False):
        p1 = self.p1 + ((self.p2 - self.p1) // 2)
        p2 = target.p1 + ((target.p2 - target.p1) // 2)
        fill_color = "red"
        if undo:
            fill_color = "grey"
        Line(p1, p2).draw(window, fill_color)
