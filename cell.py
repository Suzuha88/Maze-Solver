from graphics import *


class Cell():
    def __init__(self, window: Window) -> None:
        self.has_left_wall = True
        self.has_bottom_wall = True
        self.has_top_wall = True
        self.has_right_wall = True

        self.visited = False

        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1

        self.__window = window

    def draw(self, p1: Point, p2: Point) -> None:
        self.__x1, self.__y1 = p1.x, p1.y
        self.__x2, self.__y2 = p2.x, p2.y

        bg_color = self.__window.get_bg_color()

        if self.has_left_wall:
            self.__window.draw_line(Line(Point(p1.x, p1.y), Point(p1.x, p2.y)))
        else:
            self.__window.draw_line(
                Line(Point(p1.x, p1.y), Point(p1.x, p2.y)), bg_color)

        if self.has_bottom_wall:
            self.__window.draw_line(Line(Point(p1.x, p2.y), Point(p2.x, p2.y)))
        else:
            self.__window.draw_line(
                Line(Point(p1.x, p2.y), Point(p2.x, p2.y)), bg_color)

        if self.has_top_wall:
            self.__window.draw_line(Line(Point(p1.x, p1.y), Point(p2.x, p1.y)))
        else:
            self.__window.draw_line(
                Line(Point(p1.x, p1.y), Point(p2.x, p1.y)), bg_color)

        if self.has_right_wall:
            self.__window.draw_line(Line(Point(p2.x, p1.y), Point(p2.x, p2.y)))
        else:
            self.__window.draw_line(
                Line(Point(p2.x, p1.y), Point(p2.x, p1.y)), bg_color)

    def draw_move(self, other: Self, undo=False) -> None:
        color = "gray" if undo else "red"

        start = Point((self.__x1 + self.__x2) // 2,
                      (self.__y1 + self.__y2) // 2)
        finish = Point((other.__x1 + other.__x2) // 2,
                       (other.__y1 + other.__y2) // 2)

        self.__window.draw_line(Line(start, finish), color)

    def connect(self, other: Self) -> None:
        # connect to self.bottom
        if self.__x1 == other.__x1 and self.__y2 == other.__y1:
            self.has_bottom_wall = False
            other.has_top_wall = False
        # connect to self.top
        elif self.__x1 == other.__x1 and self.__y1 == other.__y2:
            self.has_top_wall = False
            other.has_bottom_wall = False
        # connect to self.right
        elif self.__x2 == other.__x1 and self.__y1 == other.__y1:
            self.has_right_wall = False
            other.has_left_wall = False
        # connect to self.left
        elif self.__x1 == other.__x2 and self.__y1 == other.__y1:
            self.has_left_wall = False
            other.has_right_wall = False

        else:
            raise Exception("Cells aren't 4-connected")
