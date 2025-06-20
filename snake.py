import time
import turtle
from turtle import Turtle,Screen
import random
def maint():
    num=2
    s=0.2
    screen=Screen()
    screen.bgcolor("black")
    we=Turtle()
    we.color("white")
    we.hideturtle()
    we.write("Snake Game", align="center", font=("Arial", 40, "bold"))
    time.sleep(2)

    we.clear()
    we.write("Press space button to start",align="center", font=("Arial", 40, "bold"))
    time.sleep(2)
    we.clear()
    point=0
    screen.setup(width=800,height=800)
    position=[(0,0),(-20,0),(-40,0)]
    screen.tracer(0)
    tim=[]
    shade=["red","green","blue","orange","red","yellow","brown","violet","pink"]
    for i in position:

        toy=Turtle()
        toy.shape("square")
        toy.penup()
        toy.goto(i)
        tim.append(toy)
        toy.color("white")
    screen.update()
    a=[]
    game=True
    ap=Turtle("circle")
    for i in range(-400, 401):
        a.append(i)
    b = random.choice(a)
    c = random.choice(a)
    ap.penup()
    ap.goto(b,c)
    ap.color("red")

    class ap1:
        def apple(self):
            nonlocal point
            nonlocal s
            nonlocal ap
            nonlocal num
            safe=True

            for i in range(-370,371):
                a.append(i)
            b=random.choice(a)
            c=random.choice(a)
            for segment in tim:
                if segment.distance(b, c) < 20:
                    safe = False
                    break
            if tim[0].distance(ap)<20:
                ap.goto(b,c)
                point+=1
                tail_x = tim[-1].xcor()
                tail_y = tim[-1].ycor()
                toy = Turtle()
                toy.shape("square")
                toy.penup()
                toy.color("white")
                toy.goto(tail_x, tail_y)
                tim.append(toy)
                num = len(tim) - 1
                s+=0.2
                for i in tim:
                    i.speed(s)
    direction="Right"

    class a1:
        def move(self):
            nonlocal direction
            nonlocal game
            screen.tracer(0)
            for i in range(num,0,-1):
                x1 = tim[i - 1].xcor()
                y1 = tim[i - 1].ycor()
                tim[i].goto(x1,y1)
                if tim[i].ycor() > 380 or tim[i].ycor()<-380 or tim[i].xcor()>380 or tim[i].xcor()<-380 :
                    game = False
                    screen.clear()
                    screen.bgcolor("black")

                    toy=Turtle()
                    toy.penup()
                    toy.hideturtle()
                    toy.pencolor("white")
                    toy.write("Game Over",align="center", font=("Arial", 30, "bold"))
                    toy.setheading(270)
                    toy.forward(200)
                    toy.write("Score:"+str(point),align="center", font=("Arial", 24, "bold"))
                    time.sleep(2)
                    screen.bye()
            if direction=="Right":
                tim[0].setheading(0)
                tim[0].forward(20)
            elif direction == "Left":
                tim[0].setheading(180)
                tim[0].forward(20)
            elif direction == "up":
                tim[0].setheading(90)
                tim[0].forward(20)
            elif direction == "down":
                tim[0].setheading(270)
                tim[0].forward(20)
            for segment in tim[1:]:
                if tim[0].distance(segment) == 0:
                    game = False
                    screen.clear()
                    screen.bgcolor("black")
                    toy = Turtle()
                    toy.hideturtle()
                    toy.penup()
                    toy.pencolor("white")
                    toy.write("Game Over", align="center", font=("Arial", 30, "bold"))
                    toy.setheading(270)
                    toy.forward(200)
                    toy.write("Score:" + str(point), align="center", font=("Arial", 24, "bold"))
                    time.sleep(2)
                    screen.bye()
                    return 0
            screen.update()
    class set:
        def up(self):
            nonlocal direction
            if direction!="down":
                direction="up"
        def down(self):
            nonlocal direction
            if direction!="up":
                direction="down"
        def front(self):
            nonlocal direction
            if direction!="Left":
                direction="Right"
        def back(self):
            nonlocal direction
            if direction != "Right":
                 direction = "Left"
        def games(self):
            if game==True:
                g=ap1 ()
                g.apple()
                h=a1()
                h.move()


    def forward():
        nonlocal direction
        b = set()
        b.front()


    def backward():
        c=set()
        c.back()


    def upward():
        d=set()
        d.up()


    def downward():
        e=set()
        e.down()


    screen.listen()


    def gamein():
        f=set()
        f.games()
        screen.ontimer(gamein,200)


    screen.onkey(key="d",fun=forward)
    screen.onkey(key="a",fun=backward)
    screen.onkey(key="w",fun=upward)
    screen.onkey(key="s",fun=downward)
    screen.onkey(key="space",fun=gamein)
    screen.exitonclick()

if __name__=="__main__":
    maint()