import graphics as g
import maze as m


def main() -> None:
    window = g.Window(800, 600)

    maze = m.Maze(g.Point(0, 0), 10, 10, 30, 30, window)

    window.wait_for_close()


if __name__ == "__main__":
    main()
