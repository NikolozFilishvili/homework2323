from turtle import *
speed(20)
shape("turtle")
#square
width(5)
color('green')
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)
forward(70)
#end-of-square  
#start-of-door
left(90)
color("blue")
begin_fill()
forward(100)
right(90)
forward(50)
right(90)
forward(100)
end_fill()
#endofdoor
#startofroof
penup()
goto(200, 200)
pendown()
left(180)
left(60)
color("blue")
begin_fill()
forward(115)
left(60)
forward(115)
end_fill()
left(60)
#endoroof

penup()
goto(0,-200)
exitonclick()
