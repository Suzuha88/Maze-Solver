from graphics import *


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
