




class Kämpfer:

    def __init__(self, healpoints, damage, name):
        self.healpoints = healpoints
        self.damage = damage
        self.name = name

    def attributes(self):
        return [self.healpoints, self.damage]

    def fight(self, other):
        other.healpoints = other.healpoints - self.damage
        print("" + self.name + " hits " + other.name + " for " + " damage!")

class Magier(Kämpfer):
    pass
    #def __init__(self, healpoints, damage, name, mana):
    #    self.healpoints = healpoints
    #    self.damage = damage
    #    self.name = name
    #    self.mana = mana
#
   # def Magie(self):
    #    while (self.Magier.mana >= 3):
     #       self.damage = self.damage + 10




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
    
        
    
Blue = Kämpfer(10, 20, "Kevin")
Gütnther = Kämpfer(20, 10, "Gütnther")
Herausforderer = Kämpfer(30, 30, "Max")
Brot = Arena(Gütnther, Blue)
Brot.fight_to_death()
Brot.winner().name
Risch = Arena(Brot.winner(), Herausforderer)
Risch.fight_to_death()
Risch.winner().name
Mage = Magier(150, 1, "Zauberer")#, 3)
OnevOne = Arena(Mage, Risch.winner())
OnevOne.fight_to_death()

