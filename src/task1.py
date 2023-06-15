import turtle as t
from random import randint


def obdlznik(a: int, b: int):
    t.pendown()
    for i in range(4):
        t.forward(a if i % 2 == 0 else b)
        t.right(90)
    t.penup()


def slnko(n: int, strana: int, luc: int):
    t.goto(randint(-350, 300), randint(100, 220))
    if (n < 5 or n > 15) or (strana < 10 or strana > 30) or (luc < 30 or luc > 80):
        raise Exception("Incorrect parameters")

    for _ in range(n):
        obdlznik(luc, strana)
        t.right(90)
        t.forward(strana)
        t.left(270 + ((n - 2) * 180) / n)


t.penup()
t.seth(270)
slnko(7, 13, 33)

t.color("black", "red")

t.done()
