import turtle


def square(size):
    t = turtle.Pen()
    t.hideturtle()
    t.shape('turtle')
    t.speed(3)
    t.pensize(2)
    t.penup()
    t.goto(size, 0)
    t.pendown()
    t.left(90)
    t.forward(size)
    t.left(90)
    t.forward(2 * size)
    t.left(90)
    t.forward(2 * size)
    t.left(90)
    t.forward(2 * size)
    t.left(90)
    t.forward(size)


def main():
    size = 20
    for step in range(10):
        square(size * (1 + step))


main()
