import turtle 
turtle.speed(10)
turtle.pensize(10)
t=turtle.Turtle()
t.speed(3)
turtle.bgcolor("black") 
turtle.speed(10)
turtle.pensize(10)
def curveMove():
  for i in range(200):
    turtle.rt(1)
    turtle.fd(1)

def drawHeart():
  turtle.hideturtle()
  turtle.color("red")
  turtle.begin_fill()
  turtle.lt(120)
  turtle.fd(111.65)
  curveMove()
  turtle.lt(120)
  curveMove()
  turtle.fd(111.65)
  turtle.end_fill()
  
if __name__ == '__main__':
  drawHeart()

#J
t.shape("circle")
t.color("pink")
t.pensize(35)
t.penup()
t.goto(-300,50)
t.pendown()
t.fd(100)
t.rt(90)
t.fd(150)
t.circle(-50,180)
#U
t.color("aqua")
t.penup()
t.goto(-50,-90)
t.pendown()
t.lt(90)
t.lt(90)
t.fd(150)
t.circle(50,180)
t.fd(150)
#L
t.color("pink")
t.penup()
t.goto(25,50)
t.pendown()
t.rt(-90)
t.fd(140)
t.lt(90)
t.fd(90)
#I
t.color("aqua")
t.penup()
t.goto(160,-90)
t.pendown()
t.lt(90)
t.fd(140)


