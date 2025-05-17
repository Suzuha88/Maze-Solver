from time import sleep

from graphics import *
from cell import Cell


class Maze():
    def __init__(
            self,
            start: Point,
            num_rows: int,
            num_cols: int,
            cell_width: int,
            cell_height: int,
            window: Window
    ) -> None:
        self.__start = start
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_width = cell_width
        self.__cell_height = cell_height
        self.__window = window

        self.__cells = []
        self.__create_cells()

        self.__break_entrance_and_exit()

    def __create_cells(self) -> None:
        for r in range(self.__num_rows):
            self.__cells.append([])
            for c in range(self.__num_cols):
                self.__cells[-1].append(Cell(self.__window))
                self.__draw_cell(r, c)

    def __draw_cell(self, r: int, c: int) -> None:
        top_left = Point(self.__start.x + c * self.__cell_width,
                         self.__start.y + r * self.__cell_height)
        bottom_right = Point(top_left.x + self.__cell_width,
                             top_left.y + self.__cell_height)
        self.__cells[r][c].draw(top_left, bottom_right)
        self.__animate()

    def __animate(self):
        self.__window.redraw()
        sleep(0.01)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)
