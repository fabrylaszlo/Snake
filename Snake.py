import turtle
import time


def Jobbra():
    fej.right(90)

def Ballra():
    fej.left(90)


palya = turtle.Screen()
palya.setup(width=800, height=600)
palya.bgcolor("green")
palya.title("Snake")
palya.tracer(0)
palya.listen()
palya.onkey(Jobbra, "Right")
palya.onkey(Ballra,"Left")

fej = turtle.Turtle()
fej.shape("triangle")
fej.penup()
fej.color("yellow")

while True:
    fej.forward(20)
    palya.update()
    time.sleep(0.3)