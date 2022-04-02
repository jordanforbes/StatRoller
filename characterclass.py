import dice 


class CharacterClass:
    def __init__(self,name, race):
        self.race = race
        self.name = name
        self.stre = dice.rollStat()
        self.dext = dice.rollStat()
        self.cons = dice.rollStat()
        self.inte = dice.rollStat() 
        self.wisd = dice.rollStat()
        self.char = dice.rollStat() 
    
    
    def showStats(self):
        print(
            "Name: ",self.name,
            "Race: ",self.race,
            " Strength: ",self.stre,
            " Dexterity: ",self.dext,
            " Constitution: ",self.cons,
            " Intelligence: ",self.inte,
            " Wisdom: ",self.wisd,
            " Charisma: ",self.char
            )
        
    def attack(self):
        atk = dice.rollDie(20) 
        print("1d20",atk,"strength mod",self.stre)
        atk += self.stre
        print("attack")
        return atk
        
    def reRollStats(self):
        self.stre = dice.rollStat()
        self.dext = dice.rollStat()
        self.cons = dice.rollStat()
        self.inte = dice.rollStat() 
        self.wisd = dice.rollStat()
        self.char = dice.rollStat() 
        self.showStats()
