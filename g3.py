from tkinter import font
import pgzrun

WIDTH = 700
HEIGHT = 500

#our variables
# actor
p = Actor('char1', (50, 200))
c = Actor('item1', (50, 200))

speed = 3 # speed of movement

score = 0 #global variable

def draw():
    screen.fill('black')
    p.draw()
    screen.draw.text(f'score{score}',(600,460),color='white',fontsize=25)
    c.draw()

def update():
    player_controls()
def check_score():
    if p .colliderect(c):
        score += 10
def update():
    player_controls()

def player_controls():
    if keyboard.UP and not p.top < 0:
        p.y += -speed
        p.angle = 0 
    elif keyboard.DOWN and not p.bottom > HEIGHT:
        p.y += speed
        p.angle = 0
    elif keyboard.LEFT and not p.left < 0:
        p.x += -speed
        p.angle = 10
    elif keyboard.RIGHT and not p.right > WIDTH:
        p.x += speed
        p.angle = -10
    else:
        p.angle = 0
pgzrun.go()

