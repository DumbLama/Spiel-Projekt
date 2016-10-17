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
