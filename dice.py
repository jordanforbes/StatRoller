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
        results.append(roll)
        times -=1
    return results

def rollStat():
    stat = 0
    roll= rollHowManyTimes(4,6)
    roll.remove(min(roll))
    for i in roll:
        stat+=i
    return stat
