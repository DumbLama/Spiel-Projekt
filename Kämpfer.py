class Kämpfer:

    def __init__(self, healpoints, damage, name, get_action):
        self.healpoints = healpoints
        self.damage = damage
        self.name = name
        self.get_action = get_action

    def attributes(self):
        return [self.healpoints, self.damage, self.name]

    def get_damage(self, damage):
        self.healpoints = self.healpoints - damage
        print(self.name + " received " + str(damage) + " damage.")

    def fight(self, other):
        other.get_damage(self.damage)
        print("" + self.name + " hits " + other.name + " for " + str(self.damage) + " damage!")


class Rouge(Kämpfer):

    def __init__(self,healpoints, damage, name, energy, get_action):
        self.healpoints = healpoints
        self.damage = damage
        self.name = name
        self.energy = energy
        self.invisible_flag = False
        self.get_action = get_action

    def attributes(self):
        return [self.healpoints, self.damage, self.name, self.energy]


    def get_damage(self, damage):
        if (self.invisible_flag):
            self.healpoints = self.healpoints - max(damage-100000000, 0)
            print(self.name + " received " + str(max(damage-100000000, 0)) + " damage.")
        else:
            self.healpoints = self.healpoints - damage
            print(self.name + " received " + str(damage) + " damage.")

    def fight(self, other):
        self.energy = self.energy + 1
        print(self.name + " hat Energie regeneriert " + str(self.energy))
        self.invisible_flag = False

        if (self.energy >= 2):
            self.energy = self.energy - 2
            self.Auswahl = ""
            if not(self.Auswahl in ["Invisible", "Damage"]):
                if (not (self.Auswahl == "")):
                    print("Wrong Command")
                self.Auswahl = input("Invisible or Damage?")
                
            if (self.Auswahl == "Special"):
                self.invisible_flag = True
                print(self.name + " is now Invisible.")
                
            elif (self.Auswahl == "Damage"):
                other.get_damage(self.damage)
                print(self.name + " hits " + other.name + " for " + str(self.damage) + " damage!")
                
                
                
                

class Magier(Kämpfer):
    def __init__(self, healpoints, damage, name, mana, get_action):
        self.healpoints = healpoints
        self.damage = damage
        self.name = name
        self.mana = mana
        self.get_action = get_action

    def attributes(self):
        return [self.healpoints, self.damage, self.name, self.mana]

    def fight(self, other):
        self.mana = self.mana + 1
        print(self.name + " hat Mana regeneriert " + str(self.mana))
        
        if (self.mana >= 3):
            self.mana = self.mana - 3
            self.Auswahl = ""
            if not(self.Auswahl in ["Regenerate", "Damage"]):
                if (not (self.Auswahl == "")):
                    print("Wrong Command")
                self.Auswahl = input("Regenerate or Damage?")

            if (self.Auswahl == "Special"):
                self.healpoints = self.healpoints + 10
                print(self.name + " hat Leben regeneriert, jetztige Leben: " + str(self.healpoints))
            elif (self.Auswahl == "Damage"):
                self.damage = self.damage + 3
                other.get_damage(self.damage)
                print(self.name + " blasts " + other.name + " for " + str(self.damage) + " damage!")
                self.damage = self.damage - 3
                
        #else:
        #    other.get_damage(self.damage)
        #    print("" + self.name + " hits " + other.name + " for " + str(self.damage) + " damage!")
            
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
        if not(self.Auswahl in ["Block", "Damage"]):
            if (not (self.Auswahl == "")):
                print("Wrong Command")
            self.Auswahl = input("Block or Damage")
        if (self.Auswahl == "Block"):
            self.block_flag = True
            print(self.name + " uses their shield.")
        elif (self.Auswahl == "Damage"):
            self.block_flag = False
            other.get_damage(self.damage)
            print(self.name + " slices " + other.name + " for " + str(self.damage) + " damage!")
