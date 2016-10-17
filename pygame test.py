

import pygame as pg
import sys
from pygame.locals import *

pg.init()

DISPLAYSURF = pg.display.set_mode((1000, 700))
pg.display.set_caption('gfgfgfufffkkf')
sprites = pg.image.load('sprites2.png')
spritesx = 0
spritesy = 0


while True: # main game loop
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                spritesx += 1
            elif event.key == K_LEFT:
                spritesx -= 1
            elif event.key == K_UP:
                spritesy -= 1
            elif event.key == K_DOWN:
                spritesy += 1
            print(event.key)
    DISPLAYSURF.blit(sprites,(spritesx, spritesy))

    pg.display.update()

    
    
