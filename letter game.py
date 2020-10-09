import pgzrun
import string
from random import choice,randint
WIDTH =1000
HEIGHT=700
letter_speed=1
right_score=0
wrong_score=0
screen_letters=[]
level=1
background={1:(118, 140, 213),2:(224, 54, 181),3:(229, 178, 172)}
alphabet_colour=["red","black","white","yellow","green","blue"]
def draw():
    screen.fill(background[level])
    for letter in screen_letters:
        screen.draw.text(letter["alphabet"],(letter["x"],letter["y"]),fontsize=50,color=letter["colour"])
    display_score()

def update():
    global wrong_score,letter_speed
    for letter in screen_letters:
        letter["x"] += 1
        letter["y"] += 1
        if letter["y"]>=HEIGHT or letter["x"]>=WIDTH :
            remove_letter(letter)
            get_new_letter()
            wrong_score+=1
  
            
    while len(screen_letters) < 4:
        get_new_letter()
        
def check_level():
    global right_score,level,letter_speed
    if right_score % 10==0:
        level+=1
        letter_speed+=1

def on_key_down(unicode):
    global right_score,wrong_score
    if unicode:
        for letter in screen_letters:
            if unicode==letter["alphabet"]:
                right_score+=1
                check_level()
                remove_letter(letter)
                get_new_letter()
                break
        else:
            wrong_score+=1
    
def get_new_letter():
    letter={"alphabet":"","x":0,"y":0,"colour":""}
    letter["alphabet"]=choice(string.ascii_letters)
    letter["x"]+=randint(10,WIDTH-10)
    letter["y"]+=10
    letter["colour"]=choice(alphabet_colour)
    screen_letters.append(letter)
    
def display_score():
    screen.draw.text("level:"+str(level),(20,20),fontsize=30,color="black")
    screen.draw.text("Right score:"+str(right_score),(WIDTH-200,20),fontsize=30,color="black")
    screen.draw.text("Wrong score:"+str(wrong_score),(WIDTH-200,50),fontsize=30,color="black")

def remove_letter(letter):
    screen_letters.remove(letter)

pgzrun.go()