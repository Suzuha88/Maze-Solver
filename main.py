import graphics as g
import maze as m


def main() -> None:
    window = g.Window(1300, 800)

    maze = m.Maze(g.Point(40, 40), 20, 40, 30, 30, window, seed=0)

    window.wait_for_close()


if __name__ == "__main__":
    main()
