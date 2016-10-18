
from Kämpfer import *
from Arena import *



import pygame as pg
import sys
from pygame.locals import *

pg.init()

DISPLAYSURF = pg.display.set_mode((1000, 700))
pg.display.set_caption('gfgfgfufffkkf')
Arenapic = pg.image.load('Arena.png')
Arenax = 0
Arenay = 0
Kämpfer1pic = pg.image.load('Sprites10.png')
Kämpfer1x = 910
Kämpfer1y = 559
Kämpfer2pic = pg.image.load('Sprites12.png')
Kämpfer2x = 50
Kämpfer2y = 567
Arenapic = pg.transform.scale(Arenapic, (1000, 700))
direction = "right1"


while True: # main game loop
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()

    DISPLAYSURF.blit(Arenapic,(Arenax, Arenay))

    if direction == "right1":
        Kämpfer1x += -5
        if Kämpfer1x <=  860:
            direction = "down1"
    elif direction == "down1":
        Kämpfer1y += 3
        Kämpfer1x += -3
        if Kämpfer1y >= 601:
            direction = "right2"
    elif direction == "right2":
        Kämpfer1x += -5
        if Kämpfer1x <=  135:
            direction = "up1"
    elif direction == "up1":
        Kämpfer1y -= 3
        Kämpfer1x -= +3
        if Kämpfer1y <= 559:
            direction = ("up2")
        
            
    DISPLAYSURF.blit(Kämpfer1pic,(Kämpfer1x, Kämpfer1y))
    DISPLAYSURF.blit(Kämpfer2pic,(Kämpfer2x, Kämpfer2y))


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
