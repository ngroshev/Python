import turtle


def draw_turtle_5(font):
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.pensize(2)
    turtle.forward(font)
    turtle.left(90)
    turtle.forward(font)
    turtle.left(90)
    turtle.forward(font)
    turtle.right(90)
    turtle.forward(font)
    turtle.right(90)
    turtle.forward(font)
    turtle.reset()


def draw_turtle_1(font):
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.pensize(2)
    turtle.penup()
    turtle.forward(0)
    turtle.left(90)
    turtle.forward(font)
    turtle.pendown()
    turtle.right(45)
    turtle.forward(font * (2 ** 0.5))
    turtle.right(135)
    turtle.forward(2 * font)
    turtle.reset()


def draw_turtle_0(font):
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.pensize(2)
    turtle.forward(font)
    turtle.left(90)
    turtle.forward(2 * font)
    turtle.left(90)
    turtle.forward(font)
    turtle.left(90)
    turtle.forward(2 * font)
    turtle.reset()


def draw_turtle_4(font):
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.pensize(2)
    turtle.penup()
    turtle.left(90)
    turtle.forward(font)
    turtle.pendown()
    turtle.forward(font)
    turtle.right(180)
    turtle.forward(font)
    turtle.left(90)
    turtle.forward(font)
    turtle.left(90)
    turtle.forward(font)
    turtle.right(180)
    turtle.forward(2 * font)
    turtle.reset()


def draw_turtle_7(font):
    turtle.shape('turtle')
    turtle.speed(1)
    turtle.pensize(2)
    turtle.left(90)
    turtle.forward(font)
    turtle.right(45)
    turtle.forward(font * 2 ** 0.05)
    turtle.left(135)
    turtle.forward(font)
    turtle.reset()


def main():
    font = 50
    step = font / 2
    draw_turtle_1(font)
    draw_turtle_4(font)
    draw_turtle_1(font)
    draw_turtle_7(font)
    draw_turtle_0(font)
    draw_turtle_5(font)


main()
