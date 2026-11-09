import turtle #make drawings
#make screen where drawing will be 
turtle.Screen().bgcolor("Blue")
board=turtle.Turtle()#drawing pen
#draw a triangle
board.color("black","red")
board.pensize(10)
board.penup()
board.goto(0,0)#go to the center
board.pendown()#start drawing
board.begin_fill()
board.speed(5)
for i in range(3):
    board.forward(180)
    board.right(60)
#finish drawing
board.end_fill()
turtle.done()