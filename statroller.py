import characterclass as ch 

name = input("enter name:")
race = input("enter race:")
player1 = ch.CharacterClass(name,race)
player1.showStats()