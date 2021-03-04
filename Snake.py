import turtle
import time
from random import randint


def Jobbra():
    fej.right(90)


def Ballra():
    fej.left(90)


def gyumolcs_kirak:
    x = randint(-380, 380)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(Jobbra, "Right")
palya.onkey(Ballra, "Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

kijelzo= turtle.Turtle()
kijelzo.color("white")
kijelzo.hideturtle()
kijelzo.penup()
kijelzo.clear()

while True:
    fej.forward(20)
    if fej.xcor() > 400:
        kijelzo.write("Game Over", align="center", font=("Arial", 36, "bold"))
    if fej.xcor() < -400:
        kijelzo.write("Game Over", align="center", font=("Arial", 36, "bold"))
    if fej.ycor() > 300:
        kijelzo.write("Game Over", align="center", font=("Arial", 36, "bold"))
    if fej.ycor() < -300:
        kijelzo.write("Game Over", align="center", font=("Arial", 36, "bold"))
    palya.update()
    time.sleep(0.15)
