import turtle


def squared_spiral(size, step):
    t = turtle.Pen()
    t.shape('turtle')
    t.speed(1)
    t.pensize(0)


    for i in range(0, 70):
        t.forward(size)
        t.left(90)
        size = size + step


def main():
    size = 20
    step = 10
    squared_spiral(size, step)


main()