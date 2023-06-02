from turtle import *
from random import randint

def obdlznik(a: int, b: int):
    pendown()
    for i in range(4):
        forward(a if i % 2 == 0 else b)
        right(90)
    penup()

def slnko(n: int, strana: int, luc: int):
    goto(randint(-350, 300), randint(100, 220))
    if (n < 5 or n > 15) or (strana < 10 or strana > 30) or (luc < 30 or luc > 80):
        raise "Incorrect parameters"

    for _ in range(n):
        obdlznik(luc, strana)
        right(90)
        forward(strana)
        left(270 + ((n-2)*180)/n)

penup()
seth(270)
slnko(7, 13, 33)

color('black', 'red')

done()