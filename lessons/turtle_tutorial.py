"""Turtle tutorial."""

from turtle import Turtle, colormode, done

leo: Turtle = Turtle()
leo.pencolor("blue")
leo.penup()
leo.goto(45, 60)
leo.pendown()
leo.begin_fill()
leo.speed(50)
leo.fillcolor("pink")
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
i == 0
leo.end_fill()  
leo.hideturtle()

bob: Turtle = Turtle()
bob.pencolor("blue")
bob.penup()
bob.goto(45, 60)
bob.pendown()
bob.begin_fill()
bob.speed(100)
while i < 3:
    bob.forward(300)
    bob.left(120)
    i += 1
i == 0
bob.end_fill()

side_length: int = 300
while i < 70:
    bob.forward(side_length)
    bob.left(122)
    side_length *= 0.97
    i += 1
i == 0

done()