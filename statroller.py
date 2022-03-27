from random import randint 

def rollDie(die):
    return randint(1,die)

def rollHowManyTimes(n,die):
    times = n 
    total = 0
    results = []
    while times > 0:
        roll= rollDie(die)
        total += roll
        # print(times,roll)
        results.append(roll)
        times -=1
    return results

# print(rollHowManyTimes(2,6))
# print(rollHowManyTimes(4,20))
# print(rollHowManyTimes(20,2))

def rollStat():
    stat = 0
    roll= rollHowManyTimes(4,6)
    roll.remove(min(roll))
    for i in roll:
        stat+=i
    return stat

# print(rollStat())

class characterClass:
    def __init__(self,name, race):
        self.race = race
        self.name = name
        self.stre = rollStat()
        self.dext = rollStat()
        self.cons = rollStat()
        self.inte = rollStat() 
        self.wisd = rollStat()
        self.char = rollStat() 
    
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
        atk = rollDie(20) 
        print("1d20",atk,"strength mod",self.stre)
        atk += self.stre
        print("attack")
        return atk
        
    
player1 = characterClass("Joseph","Human")
player1.showStats()