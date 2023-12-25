import turtle

t = turtle.Turtle()
turtle.title("Heart")

screen = turtle.Screen()
screen.bgcolor("black")

t.color("red")
t.fillcolor("red")
t.begin_fill()

t.left(140)
t.forward(180)
t.circle(-90, 200)
t.setheading(60)
t.circle(-90, 200)
t.forward(100)

t.end_fill()
t.up()
t.setpos(-80, 150)
t.down()
t.color("white")
t.write("deez nuts<3", font=("Verdana", 12, "bold"))
t.hideturtle()

turtle.mainloop()