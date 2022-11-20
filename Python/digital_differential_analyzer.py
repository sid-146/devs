"""
calculate dx, dy, slop


"""

from matplotlib import pyplot


def DDA(x_start, y_start, x_end, y_end):
    xCordinate = []
    yCordinate = []

    dx = x_end - x_start
    dy = y_end - y_start

    xCordinate = []
    yCordinate = []

    pyplot.plot(xCordinate, yCordinate)
    pyplot.show()


if __name__ == "__main__":
    x_start = int(input("Enter Starting 'X' co-ordinate: "))
    y_start = int(input("Enter Starting 'Y' co-ordinate: "))

    x_end = int(input("Enter ending 'X' co-ordinate: "))
    y_end = int(input("Enter ending 'Y' co-ordinate: "))

    DDA(x_start=x_start, y_start=y_start, x_end=x_end, y_end=y_end)
