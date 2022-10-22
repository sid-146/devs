from matplotlib import pyplot as plt


def get_coordintes(xstart, ystart, xend, yend):
    dx = xend - xstart
    dy = yend - ystart

    x, y = [xstart], [ystart]

    slop = dy / dx

    intercept = ystart / slop

    # y = mx+c

    while x_inter <= xend:
        x_inter += 0.5
        x.append(x_inter)
        y_inter = (x_inter * slop) + intercept
        y.append(y_inter)
        print(f"x co ordiante: {x}")
        print(f"y co ordiante: {y}")

    return x, y


def drawLine(x, y):
    plt.plot(x, y)


if __name__ == "__main__":
    # xstart = float(input("Enter x start"))
    xstart = 0
    ystart = float(input("Enter y start"))
    ystart = float(input("Enter y start"))

    xend = float(input("Enter x end"))
    yend = float(input("Enter y end"))

    x, y = get_coordintes(xstart, ystart, xend, yend)
    drawLine(x, y)
