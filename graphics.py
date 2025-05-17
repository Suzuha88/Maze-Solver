from tkinter import Tk, BOTH, Canvas
from typing import Self


class Point():
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y


class Line():
    def __init__(self, start: Point, finish: Point) -> None:
        self.start = start
        self.finish = finish

    def draw(self, canvas: Canvas, fill_color: str, width: int) -> None:
        canvas.create_line(
            self.start.x, self.start.y, self.finish.x, self.finish.y, fill=fill_color, width=width
        )


class Window():
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title('Maze Solver')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas(
            self.__root, bg="white", width=width, height=height)
        self.__canvas.pack(fill=BOTH, expand=1)

        self.__running = False

    def redraw(self) -> None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self) -> None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self) -> None:
        self.__running = False

    def draw_line(self, line: Line, fill_color="black", width=2) -> None:
        line.draw(self.__canvas, fill_color, width=width)


class Cell():
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.has_right_wall = True

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__win = window

    def draw(self, p1: Point, p2: Point) -> None:
        self.__x1, self.__y1 = p1.x, p1.y
        self.__x2, self.__y2 = p2.x, p2.y

        if self.has_left_wall:
            self.__win.draw_line(Line(Point(p1.x, p1.y), Point(p1.x, p2.y)))
        if self.has_bottom_wall:
            self.__win.draw_line(Line(Point(p1.x, p2.y), Point(p2.x, p2.y)))
        if self.has_top_wall:
            self.__win.draw_line(Line(Point(p1.x, p1.y), Point(p2.x, p1.y)))
        if self.has_right_wall:
            self.__win.draw_line(Line(Point(p2.x, p1.y), Point(p2.x, p2.y)))

    def draw_move(self, other: Self, undo=False) -> None:
        color = "gray" if undo else "red"

        start = Point((self.__x1 + self.__x2) // 2,
                      (self.__y1 + self.__y2) // 2)
        finish = Point((other.__x1 + other.__x2) // 2,
                       (other.__y1 + other.__y2) // 2)

        self.__win.draw_line(Line(start, finish), color)
