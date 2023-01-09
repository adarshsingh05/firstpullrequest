import turtle

turtle.bgcolor("white")
turtle.pensize(2)
turtle.speed(0)

for i in range(60000) :
    for colours in ["red", "pink", "blue", "yellow", "magneta", "cyan", "green"]:
        turtle.color(colours)
        turtle.circle(100)
        turtle.left(10)

turtle.hideturtle
{}     