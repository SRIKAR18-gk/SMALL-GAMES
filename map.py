import time
import  pandas
from turtle import Turtle,Screen
def play():
    screen=Screen()
    screen.setup(700,700)
    x=350
    data=pandas.read_csv("50_states.csv")
    screen.tracer(0)
    for i in data['state']:
        toy=Turtle()
        toy.hideturtle()
        toy.penup()
        toy.goto(0,x)
        toy.write(i,align="left")
        x-=15
    screen.update()
    time.sleep(3)
    screen.clear()
    toy=Turtle()
    screen=Screen()

    image="blank_states_img.gif"
    screen.addshape(image)
    toy.shape(image)
    screen.update()
    game=True
    num=0
    ind=data['state'].tolist()
    xco=data['x'].tolist()
    yco=data['y'].tolist()

    def ques():
        global game
        nonlocal num

        answer = screen.textinput(title=str(num) + "/50 STATES GUSSED", prompt="GUESS THE STATE NAME")

        if answer in ind:
            num+=1
            loca=ind.index(answer)
            toy=Turtle()
            toy.penup()
            toy.hideturtle()
            toy.goto(xco[loca],yco[loca])
            toy.write(answer,align="center")
            game=True


        else:
            game=False
            screen.clear()
            toys=Turtle()
            toys.hideturtle()
            toys.write("Score: "+str(num),align="center",font=(70))
            time.sleep(4)
            screen.bye()



    while game:
        ques()

    screen.mainloop()
if __name__=="__main__":
    play()