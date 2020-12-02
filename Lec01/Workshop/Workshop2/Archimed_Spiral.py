import turtle
import numpy as np


def archimed_spiral(k, phi_rad):
    t = turtle.Pen()
    t.shape('turtle')
    t.speed(0)
    t.pensize(1)
    phi_degr = phi_rad * (180 / np.pi)

    for i in range(0, 1000):
        ro = k * phi_rad
        t.forward(ro)
        t.left(phi_degr)
        phi_rad = phi_rad + 0.1


def main():
    archimed_spiral(0.1, 0.1)


main()
