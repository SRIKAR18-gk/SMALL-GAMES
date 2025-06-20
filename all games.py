import ponggame
import main,snake
from country import map
print("What game do you wanna play.")
game=int(input("1.turtle pass /// 2.snake /// 3.ponggame/// 4.Guess the country. Enter the number of that game."))
if game==1:
    main.mains()
elif game==2:
    snake.maint()
elif game==3:
    ponggame.main()
elif game==4:
    map.play()
