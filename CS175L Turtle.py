'''
Jenna Esposito
CS175L
Exercise 4-19 Stop Sign
'''
import turtle
stop = turtle.Turtle()
stop.shape('turtle')

distance = 50
sides = 8

angle = 360 / sides


stop.penup()
stop.goto(-50, 100)
stop.pendown()

stop.begin_fill()

for i in range(sides):
   stop.forward(distance)
   stop.right(angle)


stop.hideturtle()

stop.penup()
stop.right(110)
stop.forward(80)

stop.write('STOP', font=("Arial", 30, "normal"))


