from turtle import *

#we want to paint a house
#step 1: draw a square
speed(30)
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("yellow")
begin_fill()
left(90)
forward(120) #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()


#drawing a roof
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
#end of the roof

#drawing window number 1
penup()
goto(200,200)
pendown()

speed(20)
shape("turtle")
color("purple")
begin_fill()
right(330)
forward(30)
right(90)
color("brown")
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill()

#end of the window number 1


#drawing window number 2
penup()
goto(0,200)
pendown()

color("purple")
right(90)
forward(30)
left(90)
begin_fill()
color("brown")
forward(40)
right(90)
forward(40)
right(90)
forward(40)
end_fill()





exitonclick()