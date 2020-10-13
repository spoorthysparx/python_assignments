import pgzrun
from random import choice,randint
WIDTH=1000
HEIGHT=700
balloons=[]
balloon_y_speed=2
score=0
game_over=False
print(game_over)
balloon1=Actor("balloon1")
balloon2=Actor("balloon3")
balloon3=Actor("balloon4")

def draw():
    screen.blit("skyn",(0,0))
    draw_balloon()
    display_score()
    if game_over==True:
        screen.draw.text("GAME OVER",(((WIDTH//2)-150),(HEIGHT//2)),fontsize=100,color="red")

def update():
    global game_over
    if not game_over:
        move_balloon()
        for actor in balloons:
            if actor==balloon1 and actor.top > HEIGHT:
                game_over=True
            if actor==balloon2 and actor.top > HEIGHT:
                game_over=True
            if actor==balloon3 and actor.top > HEIGHT:
                create_balloon()    

def create_balloon(): 
    x,y = randint(50,WIDTH-50),20
    balloon1.x = x
    balloon1.y = y
    balloon2.x = x
    balloon2.y = y
    balloon3.x = x
    balloon3.y = y
    actors = [balloon1,balloon2,balloon3]

    balloons.append(choice(actors))

def on_mouse_down(pos,button):
    global score
    for actor in balloons:
        if button==mouse.LEFT and actor.collidepoint(pos):
            if actor == balloon1:
                score+=1
                sounds.pop.play()
                remove_balloon()
                create_balloon()
            elif actor == balloon2:
                score+=2
                sounds.pop.play()
                remove_balloon()
                create_balloon()
            
            elif actor == balloon3:
                score-=1
                sounds.pop.play()
                remove_balloon() 
                create_balloon()


def remove_balloon():
    for balloon in balloons:
        balloons.remove(balloon)
        

def draw_balloon():
    for balloon in balloons:
        balloon.draw()

def move_balloon():
    global balloon_y_speed
    for balloon in balloons:
        balloon.y+=balloon_y_speed

def display_score():
    screen.draw.text("score:"+str(score),(0,0),fontsize=30,color="black")

        

create_balloon()
pgzrun.go()
