import turtle


def spider(i, size):
    t = turtle.Pen()
    t.shape('turtle')
    t.speed(1)
    t.pensize(1)
    for k in range(i):
        t.forward(size)
        t.stamp()
        t.backward(size)
        t.left(360/i)


def main():
    size = 100
    i = 12
    spider(i, size)


main()
