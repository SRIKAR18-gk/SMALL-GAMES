import player
import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager,STARTING_MOVE_DISTANCE,MOVE_INCREMENT
from scoreboard import Scoreboard,game_is_on,FONT
def mains():
    global game_is_on
    screen = Screen()
    screen.setup(width=1000, height=900)
    we = Turtle()
    we.color("black")
    we.hideturtle()
    we.write("Turtle Run ", align="center", font=("Arial", 40, "bold"))
    time.sleep(2)

    we.clear()
    screen.tracer(0)
    times=0.3
    sc=Scoreboard()
    players = Player(screen)
    car_manager = CarManager(screen)

    def move_up():
        players.front()
    def move_left():
        players.left()
    def move_right():
        players.right()

    screen.listen()
    screen.onkey(move_up, "w")
    screen.onkey(move_left, "a")
    screen.onkey(move_right, "d")
    num=1

    def game(num):

        car_manager.move(player.level)
        for i in range(1, 10):
            for car in car_manager.all_toys["lane" + str(i)]:
                car.speed(num)

    def play():
        global num
        global level
        global game_is_on
        for i in range(1, 10):
            for car in car_manager.all_toys["lane" + str(i)]:
                if players.toy.distance(car)<44 and abs(players.toy.ycor()-car.ycor())<20:
                    game_is_on = False
                    players.toy.penup()
                    players.toy.goto(0,0)
                    screen.clear()
                    players.toy.write(f"Game Over", align="center", font=("Arial", 36, "bold"))
                    time.sleep(1)
                    screen.clear()
                    players.toy.write("Score: "+str(sc.score()),align="center",font=FONT)
                    time.sleep(2)
                    screen.bye()



        screen.update()
        time.sleep(times)

    players.update_level()
    while game_is_on:
        global STARTING_MOVE_DISTANCE
        game(num)
        play()
        if players.toy.ycor() > 360:
            screen.reset()
            players.increase_level()
            players.update_level()
            lev=player.level
            num += 1
            times-=0.05
            STARTING_MOVE_DISTANCE+=MOVE_INCREMENT*(player.level-1)
            players = Player(screen)
            car_manager = CarManager(screen)
            if player.level%3==0:
                times-=0.04


    screen.exitonclick()


if __name__=="__main__":
    mains()