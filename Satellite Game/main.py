import pgzrun
from random import randint
from time import time

WIDTH=800
HEIGHT=600

next_satellite=0
Satellitenumber=10
Sats= []

def Create_Satellite():
    for i in range(Satellitenumber):
        Satellite=Actor('satellite')
        Satellite.pos=randint(40,WIDTH-40),randint(40,HEIGHT-40)
        Sats.append(Satellite)



def draw():
    screen.clear()
    screen.blit('background',(0,0))
    Number=1
    for i in Sats:
        screen.draw.text(str(Number),(i.pos[0],i.pos[1]+20))
        i.draw()
        Number=Number+1



def update():
    pass
def on_mouse_down(pos):
    
Create_Satellite()
pgzrun.go()