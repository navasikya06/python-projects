import random
import math
random.seed()

def roll():
    return random.randint(0,5)

def sample1(myscore, theirscore, last):
    if myscore > theirscore:
        return 0
    else:
       return 12

def sample2(myscore, theirscore, last):
    if myscore <=50:
        return 30
    elif myscore >= 51 and myscore <=80:
        return 10
    else:
        return 0

def autoPlayLoud(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:
        print()
        print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
        print("It is Player 1's turn.")
        
        if strat1 == sample1:
            numDice = sample1(score1, score2, last)
        elif strat1 == sample2:
            numDice = sample2(score1, score2, last)
        elif strat1 == myStrategy:
            numDice = myStrategy(score1, score2, last)
 
        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print(str(numDice) + " dice chosen.") 
        print("Dice rolled: " + diceString)
        print("Total for this turn: " + str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last: 
            break
        if numDice == 0:
            last = True
        
        print('')
        print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
        print("It is Player 2's turn.")
        
        if strat2 == sample1:
            numDice = sample1(score2, score1, last)
        elif strat2 == sample2:
            numDice = sample2(score2, score1, last)
        elif strat2 == myStrategy:
            numDice = myStrategy(score2, score1, last)

        diceTotal = 0
        diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            diceString = diceString + " "  + str(d)
            i = i-1
        print(str(numDice) + " dice chosen.") 
        print("Dice rolled: " + diceString)
        print("Total for this turn: " + str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True

    print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
    if score1 > 100:
        print("Player 2 wins.")
        return 2
    elif score2 > 100:
        print("Player 1 wins.")
        return 1
    elif score1 > score2:
        print("Player 1 wins.")
        return 1
    elif score2 > score1:
        print("Player 2 wins.")
        return 2
    else:
        print("Tie.")
        return 3

autoPlayLoud(sample1, sample1)
