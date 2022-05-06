import turtle as t
playerAscore= 0
playerBscore= 0

linux=t.Screen()
linux.title("game")
linux.bgcolor("black")
linux.setup(width=800,height=600)
linux.tracer(0)

leftpaddle=t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("white")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)

rightpaddle=t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2

pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score", align="center", font=("Arial",24,"normal"))

def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    leftpaddle.sety(y)

def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)  

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)     

def rightpaddleup():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)  

linux.listen()
linux.onkeypress(leftpaddleup, "w")         
linux.onkeypress(leftpaddledown, "s")   
linux.onkeypress(rightpaddleup, "o")    
linux.onkeypress(rightpaddledown, "l")    

while True:
    linux.update()

    ball.setx(ball.xcor()+ballxdirection)
    ball.setx(ball.ycor()+ballydirection)

    if ball.ycor()>290:
       ball.sety(290)
       ballydirection=ballydirection*-1
    if ball.ycor()>290:
       ball.sety(290)
       ballydirection=ballydirection*-1   

    if ball.xcor()>390:
        ball.goto(0,0)
        ballxdirection=ballxdirection
        playerAscore=playerAscore+1
        pen.clear()
        pen.write("player A:{}   player B:{}".format(playerAscore,playerBscore),align="center",font=("Arial", 24, "normal"))
    if (ball.xcor()>340)and(ball.xcor()<350)and(ball.ycor()<rightpaddle.ycor()+40 and ball.ycor()>rightpaddle.ycor()-40):
        ball.setx(340) 
        ballxdirection=ballxdirection*-1 
    if (ball.ycor()>-340)and(ball.ycor()<-350)and(ball.ycor()<leftpaddle.ycor()+40 and ball.ycor()>leftpaddle.ycor()-40):
        ball.setx(-340) 
        ballydirection=ballydirection*-1     