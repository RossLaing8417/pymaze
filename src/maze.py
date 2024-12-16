from src.window import Window
from src.point import Point
from src.cell import Cell

import random
import time


class Maze:
    def __init__(self,
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
        self.__adjacent: list[set[int, int]] = [
            (-1, 0,), (0, -1,), (1, 0,), (0, 1,)
        ]
        self.cells: list[list[Cell]] = [
            [None for _ in range(rows)] for _ in range(cols)
        ]
        if seed is not None:
            random.seed(seed)
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_visited_cells()

    def __create_cells(self) -> None:
        for y in range(self.cols):
            for x in range(self.rows):
                row_offset = self.__point.x + (x * self.cell_size)
                col_offset = self.__point.y + (y * self.cell_size)
                self.cells[y][x] = Cell(
                    Point(row_offset, col_offset),
                    Point(row_offset + self.cell_size,
                          col_offset + self.cell_size)
                )
                self.__draw_cell(x, y)

    def __break_entrance_and_exit(self) -> None:
        self.cells[0][0].top = False
        self.__draw_cell(0, 0)
        self.cells[self.cols-1][self.rows-1].bottom = False
        self.__draw_cell(self.rows-1, self.cols-1)

    def __break_walls_r(self, x: int, y: int) -> None:
        self.cells[y][x].visited = True
        while True:
            queue: list[set[int, int]] = []
            for adj in self.__adjacent:
                xx = x + adj[0]
                yy = y + adj[1]
                if xx < 0 or xx >= self.rows or yy < 0 or yy >= self.cols:
                    continue
                if not self.cells[yy][xx].visited:
                    queue.append((xx, yy,))
            if len(queue) == 0:
                self.__draw_cell(x, y)
                break
            xx, yy = queue[random.randrange(0, len(queue))]
            if xx == x:
                if yy > y:
                    self.cells[y][x].bottom = False
                    self.cells[yy][xx].top = False
                else:
                    self.cells[y][x].top = False
                    self.cells[yy][xx].bottom = False
            else:
                if xx > x:
                    self.cells[y][x].right = False
                    self.cells[yy][xx].left = False
                else:
                    self.cells[y][x].left = False
                    self.cells[yy][xx].right = False
            self.__break_walls_r(xx, yy)

    def __reset_visited_cells(self) -> None:
        for row in self.cells:
            for cell in row:
                cell.visited = False

    def __draw_cell(self, x: int, y: int) -> None:
        if self.__window is not None:
            self.cells[y][x].draw(self.__window, "black")
            self.__animate()

    def __draw_cell_move(self,
                         x: int, y: int,
                         xx: int, yy: int,
                         undo: bool = False
                         ) -> None:
        if self.__window is not None:
            self.cells[y][x].draw_move(self.__window, self.cells[yy][xx], undo)
            self.__animate()

    def __animate(self) -> None:
        self.__window.redraw()
        time.sleep(0.01)

    def __solve_r(self, x: int, y: int) -> bool:
        self.__animate()
        self.cells[y][x].visited = True
        if x == self.rows - 1 and y == self.cols - 1:
            return True
        for adj in self.__adjacent:
            xx = x + adj[0]
            yy = y + adj[1]
            if xx < 0 or xx >= self.rows or yy < 0 or yy >= self.cols:
                continue
            if self.cells[yy][xx].visited:
                continue
            can_move = False
            if xx == x:
                can_move = (yy > y and not self.cells[y][x].bottom) or (
                    yy < y and not self.cells[y][x].top)
            else:
                can_move = (xx > x and not self.cells[y][x].right) or (
                    xx < x and not self.cells[y][x].left)
            if can_move:
                self.__draw_cell_move(x, y, xx, yy)
                if self.__solve_r(xx, yy):
                    return True
                self.__draw_cell_move(x, y, xx, yy, True)
        return False

    def solve(self) -> bool:
        return self.__solve_r(0, 0)
