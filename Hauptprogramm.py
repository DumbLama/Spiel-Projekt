
from Kämpfer import *
from Arena import *



import pygame as pg
import sys
from pygame.locals import *

pg.init()

DISPLAYSURF = pg.display.set_mode((1000, 700))
pg.display.set_caption('Kuhles Sbiel')
Arenapic = pg.image.load('Arena.png')
Arenax = 0
Arenay = 0
Kämpfer1pic = pg.image.load('Sprites10.png')
Kämpfer1pos = Kämpfer1pic.get_rect()
Kämpfer1pos = Kämpfer1pos.move((910, 559))
print(str(Kämpfer1pos.top) + str(Kämpfer1pos.right))

Kämpfer2pic = pg.image.load('Sprites12.png')
Kämpfer2pos = Kämpfer2pic.get_rect()
Kämpfer2pos = Kämpfer2pos.move((50, 567))

Arenapic = pg.transform.scale(Arenapic, (1000, 700))
direction = "right1"
key = pg.key.get_pressed()
action = ""


def get_action():
    return action

Rouge = Rouge(120, 50, "Rouge", 0, get_action)
Zauberer = Magier(60, 30, "Zauberer", 2, get_action)
Arena2 = Arena(Rouge, Zauberer)


while True: # main game loop
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        #elif event.type == KEYDOWN:
         #   if event.state.

    DISPLAYSURF.blit(Arenapic,(Arenax, Arenay))

    key = pg.key.get_pressed()
    #key = pg.key.get_pressed()

    if direction == "right1":
        print("a"+str(Kämpfer1pos.top) + str(Kämpfer1pos.right))
        Kämpfer1pos = Kämpfer1pos.move(-5,0)
        if Kämpfer1pos.left <=  860:
            direction = "down1"
    elif direction == "down1":
        print("b"+str(Kämpfer1pos.top) + str(Kämpfer1pos.right))
        Kämpfer1pos = Kämpfer1pos.move(-3,3)
        if Kämpfer1pos.top >= 601:
            direction = "right2"
    elif direction == "right2":
        Kämpfer1pos = Kämpfer1pos.move(-5,0)
        if Kämpfer1pos.left <=  135:
            direction = "up1"
    elif direction == "up1":
        Kämpfer1pos = Kämpfer1pos.move(-3,-3)
        if Kämpfer1pos.top <= 559:
            direction = ("up2")

        
            
    DISPLAYSURF.blit(Kämpfer1pic, Kämpfer1pos, Kämpfer1pos)
    DISPLAYSURF.blit(Kämpfer2pic, Kämpfer2pos, Kämpfer2pos)


    pg.display.update()

    
    

        
    
#Blue = Kämpfer(100, 10, "Kevin")
#Gütnther = Kämpfer(150, 8, "Gütnther")
#Max = Krieger(300, 12, "Max")
Rouge = Rouge(120, 50, "Rouge", 0)
Zauberer = Magier(60, 30, "Zauberer", 2)
#Arena1 = Arena(Gütnther, Blue)
#Arena1.fight_to_death()
#Arena1.winner().name
Arena2 = Arena(Rouge, Zauberer)
Arena2.fight_to_death()
Arena2.winner().name
#OnevOne = Arena(Mage, Risch.winner())
#OnevOne.fight_to_death()
