from turtle import width
import pgzrun

WIDTH=500
HIGHT =500

box = Rect((50,150),(50,100))
box2 = Rect((105,150),(50,50))

def draw():
    screen.fill('red')
    screen.draw.text('hola amingo',(50,50),color='white')
    screen.draw.text('this is game programming',(50,80),color='yellow',fontsize=50)
    screen.draw.text('this is game programming',(50,80),color='yellow',fontsize=50)
    screen.draw.rect(box,color = 'white')
    screen.draw.filled_rect(box2,color = 'pink')
def update():
    box.x += 1
    box2.y += 2
    
pgzrun.go()