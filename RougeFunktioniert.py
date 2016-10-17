
from Kämpfer import *

class Arena:
    def __init__(self, kämpfer1, kämpfer2):
        self.kämpfer1 = kämpfer1
        self.kämpfer2 = kämpfer2

    def fight_to_death(self):
        while (not (self.kämpfer1.healpoints <=0 or self.kämpfer2.healpoints <=0)):
            self.kämpfer1.fight(self.kämpfer2)
            if (not (self.kämpfer1.healpoints <=0 or self.kämpfer2.healpoints <=0)):
                self.kämpfer2.fight(self.kämpfer1)

    def winner(self):
        if (not (self.kämpfer1.healpoints <=0 or self.kämpfer2.healpoints <=0)):
            print("Du Spassti es gibt noch keinen Gewinner warum fragst du denn?")
            return False
        elif (self.kämpfer1.healpoints <=0):
            print( self.kämpfer2.name + " hat gewonnen")
            return self.kämpfer2
        else:
            print( self.kämpfer1.name + " hat gewonnen")
            return self.kämpfer1
    
        
    
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
