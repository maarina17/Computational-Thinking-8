import turtle
t = turtle
#this makes the turtle fast
t.speed(10)
#this changes the background color
turtle.Screen() .bgcolor("thistle")

t = turtle
t.penup()
t.goto(-250, -75)
#this makes the turtle blue
t.color("dark slate blue")
t.pendown()

for i in range(120):
    t.forward(500+1)
    t.left(140+1)


turtle.exitonclick()
