

class Kämpfer:

    def __init__(self, healpoints, damage, name):
        self.healpoints = healpoints
        self.damage = damage
        self.name = name

    def attributes(self):
        return [self.healpoints, self.damage, self.name]

    def get_damage(self, damage):
        self.healpoints = self.healpoints - damage
        print(self.name + " received " + str(damage) + " damage.")

    def fight(self, other):
        other.get_damage(self.damage)
        print("" + self.name + " hits " + other.name + " for " + str(self.damage) + " damage!")

class Magier(Kämpfer):
    def __init__(self, healpoints, damage, name, mana):
        self.healpoints = healpoints
        self.damage = damage
        self.name = name
        self.mana = mana

    def attributes(self):
        return [self.healpoints, self.damage, self.name, self.mana]

    def fight(self, other):
        self.mana = self.mana + 1
        print(self.name + " hat Mana regeneriert " + str(self.mana))
        
        if (self.mana >= 3):
            self.mana = self.mana - 3
            self.Auswahl = ""
            while not(self.Auswahl in ["Regenerate", "Damage"]):
                if (not (self.Auswahl == "")):
                    print("Wrong Command")
                self.Auswahl = input(self.name + ", Regenerate or Damage?")

            if (self.Auswahl == "Regenerate"):
                self.healpoints = self.healpoints + 10
                print(self.name + " hat Leben regeneriert, jetztige Leben: " + str(self.healpoints))
            elif (self.Auswahl == "Damage"):
                self.damage = self.damage + 3
                other.get_damage(self.damage)
                print(self.name + " blasts " + other.name + " for " + str(self.damage) + " damage!")
                self.damage = self.damage - 3
                
        else:
            other.get_damage(self.damage)
            print("" + self.name + " hits " + other.name + " for " + str(self.damage) + " damage!")
            
class Krieger(Kämpfer):
    def get_damage(self, damage):
        if (self.block_flag):
            self.healpoints = self.healpoints - max(damage-10, 0)
            print(self.name + " received " + str(max(damage-10, 0)) + " damage.")
        else:
            self.healpoints = self.healpoints - damage
            print(self.name + " received " + str(damage) + " damage.")


    def fight(self, other):
        self.Auswahl = ""
        while not(self.Auswahl in ["Block", "Damage"]):
            if (not (self.Auswahl == "")):
                print("Wrong Command")
            self.Auswahl = input(self.name + ", Block or Damage?")
        if (self.Auswahl == "Block"):
            self.block_flag = True
            print(self.name + " uses their shield.")
        elif (self.Auswahl == "Damage"):
            other.get_damage(self.damage)
            print(self.name + " slices " + other.name + " for " + str(self.damage) + " damage!")
            
                
    


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
Max = Krieger(300, 12, "Max")
Zauberer = Magier(60, 30, "Zauberer", 3)
#Arena1 = Arena(Gütnther, Blue)
#Arena1.fight_to_death()
#Arena1.winner().name
Arena2 = Arena(Max, Zauberer)
Arena2.fight_to_death()
Arena2.winner().name
#OnevOne = Arena(Mage, Risch.winner())
#OnevOne.fight_to_death()
