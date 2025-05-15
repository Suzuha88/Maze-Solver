from tkinter import Tk, BOTH, Canvas


class Window():
    def __init__(self, width: int, height: int) -> None:
        self.__root = Tk()
        self.__root.title('Title')
        self.__root.geometry(f'{width}x{height}')
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

        self.__canvas = Canvas()
        self.__canvas.pack()

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


def main() -> None:
    window = Window(800, 600)
    window.wait_for_close()


if __name__ == "__main__":
    main()
