from src.window import Window
from src.point import Point
from src.cell import Cell

import time


class Maze:
    def __init__(
            self,
            p: Point,
            rows: int,
            cols: int,
            cell_size: int
    ):
        self.__point: Point = p
        self.rows: int = rows
        self.cols: int = cols
        self.cell_size: int = cell_size
        self.__cells: list[list[Cell]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]
        self.__create_cells()

    def __create_cells(self) -> None:
        for row in range(self.rows):
            for col in range(self.rows):
                row_offset = self.__point.x + (row * self.cell_size)
                col_offset = self.__point.y + (col * self.cell_size)
                self.__cells[row][col] = Cell(
                    Point(row_offset, col_offset),
                    Point(row_offset + self.cell_size,
                          col_offset + self.cell_size)
                )
        self.__break_entrance_and_exit()

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].top = False
        self.__cells[self.rows-1][self.cols-1].bottom = False

    def __draw_cells(self, window: Window) -> None:
        for y in range(self.cols):
            for x in range(self.rows):
                self.__cells[x][y].draw(window, "black")
                self.__animate(window)

    def __animate(self, window: Window) -> None:
        window.redraw()
        time.sleep(0.05)

    def draw(self, window: Window) -> None:
        self.__draw_cells(window)

    def cells(self) -> list[list[Cell]]:
        """Exists for testing only because why not..."""
        return self.__cells
