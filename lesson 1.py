from turtle import *


#we want to paint a house

#step 1: draw a square
speed(5)
width(5)
begin_fill()
color("orange")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
end_fill()
#end of square

#drawing a door
forward(70)
color("black")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()

penup()
goto(200, 200)
pendown()

color("brown")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill() 
#end of door



#drawing a windows
color("black")
penup()

left(30)
forward(65)
left(90)
forward(30)
pendown()
begin_fill()
color("cyan")
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()


penup()
left(90)
forward(100)
pendown()

begin_fill()
forward(50)
left(90)
forward(50)
left(90)
forward(50)
left(90)
forward(50)
end_fill()
#end of windows


penup()
goto(-470, -350)
pendown()


#crating a grass
left(90)
forward(100)
color("green")
width("695")
forward(5000)
#end of grass

exitonclick()