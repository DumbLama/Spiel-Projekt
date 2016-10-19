from random import randint
from Kämpfer import *
from Arena import *



import pygame as pg
import sys
from pygame.locals import *
superstate = "Intro"
pg.init()

DISPLAYSURF = pg.display.set_mode((1000, 700))
pg.display.set_caption('Kuhles sbiel')
Arenapic = pg.image.load('Arena.png')
Arenax = 0
Arenay = 0
Feuerballpic = pg.image.load("Kostum1.png")
feuerballx = 0
feuerbally = 0
feuerball_flag = False
Kriegerschlagpic = pg.image.load("Kostum2.png")
Kriegerschlagx = 0
Kriegerschlagy = 0
schlag_flag = False
schlag_counter = 0
Kämpfer1pic = pg.image.load('Sprites10.png')
Kämpfer1x = 910
Kämpfer1y = 559

kämpfer1_fight_flag = False

Kämpfer2pic = pg.image.load('Sprites12.png')
Kämpfer2x = 50
Kämpfer2y = 567

kämpfer2_fight_flag = False

Arenapic = pg.transform.scale(Arenapic, (1000, 700))
direction = "right1"
key = pg.key.get_pressed()
action = ""

def_flag1 = False
def_flag2 = False
input_flag = False
phase = ""
damage_flag = False
special_flag = False
Schild_Flag = False



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
    action = ""
    
    if superstate == "Intro":
    
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
            if Kämpfer1x <=  525:
                direction = "left"


        if direction == "left":
            Kämpfer2x += 5
            if Kämpfer2x >=  115:
                direction = "down2"
        elif direction == "down2":
            Kämpfer2y += 3
            Kämpfer2x += 3
            if Kämpfer2y >= 601:
                direction = "left2"
        elif direction == "left2":
            Kämpfer2x += 5
            if Kämpfer2x >=  425:
                direction = ""
                superstate = "Fight"
                
    elif superstate == "Fight":
        if not ((kämpfer1_fight_flag) or (kämpfer2_fight_flag)):
            if randint(0, 1) == 0:
                kämpfer1_fight_flag = True
                print("Der Kämpfer Links kämpft")
            else:
                kämpfer1_fight_flag = True
                print("Der Kämpfer Rechte kämpft")

        if kämpfer1_fight_flag:
            if phase == "":
                phase = "regeneration"
            elif phase == "regeneration":
                #kämpfer1.regenerate()
                phase = "special"
            elif phase == "special":
                if True:#krieger1.genug():
                    phase = "choice"
                else:
                    phase = "autoattack"
            elif phase == "choice":
                #auswahl treffen
                if key[pg.K_d] and  key[pg.K_s]:
                    pass
                elif key[pg.K_d]:
                    damage_flag = True
                elif key[pg.K_s]:
                    special_flag = True
                if damage_flag or special_flag:
                    phase = "animation"
                    if damage_flag:
                        animation = "damage"
                    else:
                        animation = "special"
                
            elif phase == "autoattack":
                krieger1.autoattack(krieger2)
                phase = "animation"
                animation = "krieger1autoattack"
            elif phase == "animation":
                #animation
                if direction == "":
                    direction = "hingehen"
                if animation == "damage":
                    if direction == "hingehen":
                        Kämpfer1x += -5
                        if Kämpfer1x <=  480:
                            direction = "schlag"
                    elif direction == "schlag":
                        schlag_flag = True
                        schlag_counter += 1
                        if schlag_counter >= 30:
                            direction = "zurückgehen"
                    elif direction == "zurückgehen":
                        schlag_flag = False
                        schlag_counter = 0
                        Kämpfer1x += 5
                        if Kämpfer1x >=  525:
                            direction = ""
                            phase = ""
                            kämpfer1_fight_flag = False
                            kämpfer2_fight_flag = True
                elif animation == "special":
                    pass

                elif animation == "autoattack":
                    pass
                    
            
                
        

            
##    if key[pg.K_d] or  key[pg.K_s]:
##        if key[pg.K_d] and key[pg.K_s]:
##            pass
##        if key[pg.K_d]:
##            action = "Damage"
##        else:
##            action = "Special"
##
##    if direction == "fight":
##        print(action)
##        Arena2.fight_to_death()
##        input()

    
        
            
    #DISPLAYSURF.blit(Kämpfer1pic,(Kämpfer1x, Kämpfer1y))
    DISPLAYSURF.blit(Kämpfer2pic,(Kämpfer2x, Kämpfer2y))
    if feuerball_flag:
        DISPLAYSURF.blit(Feuerballpic,(Feuerballx, Feuerbally))
    if schlag_flag:
        DISPLAYSURF.blit(Kriegerschlagpic, (Kämpfer1x, Kämpfer1y))
    else:
        DISPLAYSURF.blit(Kämpfer1pic,(Kämpfer1x, Kämpfer1y))


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
