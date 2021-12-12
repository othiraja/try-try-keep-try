import turtle
import random
# create by othi 
#backgroud
bg = turtle.Screen()
bg.bgcolor("white")#light green, gray....
turtle.penup()
#1
turtle.goto(-170,-190)
turtle.color("green")
turtle.pendown()
turtle.forward(350)
turtle.penup()
turtle.write("name of person")
#2
turtle.goto(-160,-150)
turtle.color("black")
turtle.pendown()
turtle.forward(300)
turtle.penup()
turtle.write("BIRTHDAY")
#3
turtle.goto(-150,-110)
turtle.color("orange")
turtle.pendown()
turtle.forward(250)
turtle.penup()
turtle.write("HAPPY")
#cake
turtle.goto(-100,-100)
turtle.color("pink")
turtle.begin_fill()
turtle.pendown()
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(150)
turtle.left(90)
turtle.forward(100)
turtle.end_fill()
turtle.penup()
#candle
turtle.goto(-90,0)
turtle.color("green")
turtle.left(180)
turtle.pendown()
turtle.forward(20)
#candle

turtle.penup()
turtle.goto(-60,0)
turtle.color("blue")
turtle.pendown()
turtle.forward(20)
#candke
turtle.penup()
turtle.goto(-30,0)
turtle.color("brown")
turtle.pendown()
turtle.forward(20)
#candle
turtle.penup()
turtle.goto(0,0)
turtle.color("green")
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color("purple")
turtle.pendown()
turtle.forward(20)
colors = ["red", "orange", "brown", "green", "blue", "purple", "white"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()
for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)
turtle.penup()
turtle.goto(-150, 150)
turtle.color("pink")
turtle.pendown()

