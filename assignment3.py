import pgzrun,random
WIDTH=1000
HEIGHT=700
ball_x_speed=4
ball_y_speed=4
missed=False
score=0
ball = Actor("ball",center = (random.randint(0,300),random.randint(0,300)))
paddle = Actor("paddle")
paddle.left = 0
paddle.bottom =HEIGHT
def draw():
    screen.fill("black")
    ball.draw()
    paddle.draw()
    display_score()
    if missed:
        display_text()

def update():
    if not missed:
        move_ball()

def on_mouse_move(pos):
    paddle.x=pos[0]
    if paddle.left<0:
        paddle.left=0
    elif paddle.right> WIDTH:
        paddle.right=WIDTH

def move_ball():
    ball.x+=ball_x_speed
    ball.y+=ball_y_speed
    check_boundaries()
    check_paddle_collision()
    check_paddle_miss()

def check_boundaries():
    global ball_y_speed,ball_x_speed
    if ball.bottom >HEIGHT or ball.top<0:
        ball_y_speed *=-1
    elif ball.left<0 or ball.right>WIDTH:
        ball_x_speed*=-1

def check_paddle_collision():
    global ball_y_speed,score
    if ball.colliderect(paddle):
        ball_y_speed*=-1
        score+=10

def check_paddle_miss():
    global missed
    if ball.bottom > paddle.top + abs(ball_y_speed):
        missed=True
def  display_text():
    position=((WIDTH//2)-120,(HEIGHT//2))
    screen.draw.text("oops! you missed it",position,fontsize=50,color="red")

def display_score():
    screen.draw.text("score:"+str(score),(10,10),fontsize=20,color="red")

pgzrun.go()