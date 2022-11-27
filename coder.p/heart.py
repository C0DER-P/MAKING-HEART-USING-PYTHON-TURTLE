import turtle
turtle.title("heart")

s=turtle.getscreen()
t=turtle.Turtle()
s.bgcolor('black')
t.begin_fill()
t.color('red')
t.speed(2)
t.left(50)
t.forward(150)
#curve
t.circle(60,200)
t.right(140)
t.circle(60,200)
t.forward(160)
t.end_fill()
t.hideturtle()
turtle.mainloop()