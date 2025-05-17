from tkinter import Tk, BOTH, Canvas


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
