from src.window import Window
from src.point import Point
from src.cell import Cell

import random
import time


class Maze:
    def __init__(
            self,
            window: Window,
            p: Point,
            rows: int,
            cols: int,
            cell_size: int,
            seed: int = None
    ):
        self.__window: Window = window
        self.__point: Point = p
        self.rows: int = rows
        self.cols: int = cols
        self.cell_size: int = cell_size
        self.__cells: list[list[Cell]] = [
            [None for _ in range(cols)] for _ in range(rows)
        ]
        if seed is not None:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)

    def __create_cells(self) -> None:
        for y in range(self.cols):
            for x in range(self.rows):
                row_offset = self.__point.x + (x * self.cell_size)
                col_offset = self.__point.y + (y * self.cell_size)
                self.__cells[y][x] = Cell(
                    Point(row_offset, col_offset),
                    Point(row_offset + self.cell_size,
                          col_offset + self.cell_size)
                )
                self.__draw_cell(x, y)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].top = False
        self.__cells[self.rows-1][self.cols-1].bottom = False

    def __break_walls_r(self, x: int, y: int) -> None:
        self.__cells[y][x].visited = True
        adjacent = [(-1, 0,), (0, -1,), (1, 0,), (0, 1,)]
        while True:
            queue: list[set[int, int]] = []
            for adj in adjacent:
                xx = x + adj[0]
                yy = y + adj[1]
                if xx < 0 or xx >= self.rows or yy < 0 or yy >= self.cols:
                    continue
                if not self.__cells[yy][xx].visited:
                    queue.append((xx, yy,))
            if len(queue) == 0:
                self.__draw_cell(x, y)
                break
            xx, yy = queue[random.randrange(0, len(queue))]
            if xx == x:
                if yy > y:
                    self.__cells[y][x].bottom = False
                    self.__cells[yy][xx].top = False
                else:
                    self.__cells[y][x].top = False
                    self.__cells[yy][xx].bottom = False
            else:
                if xx > x:
                    self.__cells[y][x].right = False
                    self.__cells[yy][xx].left = False
                else:
                    self.__cells[y][x].left = False
                    self.__cells[yy][xx].right = False
            self.__break_walls_r(xx, yy)

    def __draw_cell(self, x: int, y: int) -> None:
        self.__cells[y][x].draw(self.__window, "black")
        self.__animate()

    def __animate(self) -> None:
        self.__window.redraw()
        time.sleep(0.05)

    def cells(self) -> list[list[Cell]]:
        """Exists for testing only because why not..."""
        return self.__cells
