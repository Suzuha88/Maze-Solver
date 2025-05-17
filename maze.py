from time import sleep
from collections import deque
import random

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
            window: Window,
            seed: int | None = None,
            create_speed: float = 0,
            solve_speed: float = 0.005,
    ) -> None:
        random.seed(seed)

        self.__start = start
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_width = cell_width
        self.__cell_height = cell_height
        self.__window = window
        self.__solve_speed = solve_speed
        self.__create_speed = create_speed

        self.__cells = []

        self.__create_cells()
        self.__draw_grid()

        self.__break_walls()
        self.__draw_grid()

    def __create_cells(self) -> None:
        for _ in range(self.__num_rows):
            self.__cells.append([])
            for _ in range(self.__num_cols):
                self.__cells[-1].append(Cell(self.__window))

    def __draw_grid(self) -> None:
        dirs = [(1, 0), (0, 1)]

        frontier = deque([(0, 0)])
        visited = [[False] * self.__num_cols for _ in range(self.__num_rows)]
        visited[0][0] = True

        while frontier:
            r, c = frontier.popleft()

            self.__draw_cell(r, c)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if self.__is_valid_cell(nr, nc) and not visited[nr][nc]:
                    frontier.append((nr, nc))
                    visited[nr][nc] = True

    def __draw_cell(self, r: int, c: int) -> None:
        top_left = Point(self.__start.x + c * self.__cell_width,
                         self.__start.y + r * self.__cell_height)
        bottom_right = Point(top_left.x + self.__cell_width,
                             top_left.y + self.__cell_height)
        self.__cells[r][c].draw(top_left, bottom_right)
        self.__animate(self.__create_speed)

    def __animate(self, time: float):
        self.__window.redraw()
        sleep(time)

    def __break_entrance_and_exit(self) -> None:
        self.__cells[0][0].has_top_wall = False
        self.__draw_cell(0, 0)

        self.__cells[-1][-1].has_bottom_wall = False
        self.__draw_cell(self.__num_rows - 1, self.__num_cols - 1)

    def __is_valid_cell(self, r: int, c: int) -> bool:
        return 0 <= r < self.__num_rows and 0 <= c < self.__num_cols

    def __break_walls(self) -> None:
        self.__break_entrance_and_exit()

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        frontier = [(0, 0)]
        visited = [[False] * self.__num_cols for _ in range(self.__num_rows)]
        visited[0][0] = True

        while frontier:
            r, c = frontier.pop()

            random.shuffle(dirs)

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if not self.__is_valid_cell(nr, nc) or visited[nr][nc]:
                    continue
                visited[nr][nc] = True
                self.__cells[nr][nc].connect(self.__cells[r][c])

                frontier.append((nr, nc))

    def __backtrack(
            self,
            start: tuple[int, int],
            target: tuple[int, int],
            prev_cells: list[list[tuple[int, int]]],
            color: str = "green",
            width: int = 4,
    ) -> None:
        cur_r, cur_c = start[0], start[1]
        prev_r, prev_c = prev_cells[cur_r][cur_c]

        while (cur_r, cur_c) != target:
            self.__cells[cur_r][cur_c].draw_move(
                self.__cells[prev_r][prev_c], color, width)
            cur_r, cur_c = prev_r, prev_c
            prev_r, prev_c = prev_cells[prev_r][prev_c]
            self.__animate(self.__solve_speed)

    def solve(self) -> None:
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        prev_cells = [[(-1, -1)] *
                      self.__num_cols for _ in range(self.__num_rows)]

        visited = [[False] * self.__num_cols for _ in range(self.__num_rows)]
        visited[0][0] = True

        frontier = deque([(0, 0)])

        while frontier:
            r, c = frontier.popleft()

            if r == self.__num_rows - 1 and c == self.__num_cols - 1:
                self.__backtrack((r, c), (0, 0), prev_cells)
                return

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if (
                        not self.__is_valid_cell(nr, nc) or
                        not self.__cells[r][c].is_connected(self.__cells[nr][nc]) or
                        visited[nr][nc]
                ):
                    continue

                prev_cells[nr][nc] = (r, c)
                visited[nr][nc] = True

                frontier.append((nr, nc))

                self.__cells[r][c].draw_move(self.__cells[nr][nc])
                self.__animate(self.__solve_speed)
