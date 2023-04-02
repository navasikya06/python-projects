import random
import math
import pr1testing
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

def improve(strat1):
    def upgrade(myscore, theirscore, last):
        if myscore >=100:
            return 0
    return upgrade

def myStrategy(myscore, theirscore, last):
    if not(last):
        return (100 - myscore)//3
    elif myscore >= 93:
        return 0
    elif myscore >= (theirscore + 25):
        return 0
    else:
        return ((theirscore - myscore +1)*2)//5
 
def autoplay(strat1, strat2):
    score1 = 0
    score2 = 0
    last = False
    while True:
        #print()
        #print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
        #print("It is Player 1's turn.")
        
        if strat1 == sample1:
            numDice = sample1(score1, score2, last)
        elif strat1 == sample2:
            numDice = sample2(score1, score2, last)
        elif strat1 == myStrategy:
            numDice = myStrategy(score1, score2, last)
        else:
            numDice = pr1testing.test4(score1, score2, last)
 
        diceTotal = 0
        #diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            #diceString = diceString + " "  + str(d)
            i = i-1
        #print(str(numDice) + " dice chosen.") 
        #print("Dice rolled: " + diceString)
        #print("Total for this turn: " + str(diceTotal))
        score1 += diceTotal
        if score1 > 100 or last: 
            break
        if numDice == 0:
            last = True
        
        #print('')
        #print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
        #print("It is Player 2's turn.")
        
        if strat2 == sample1:
            numDice = sample1(score2, score1, last)
        elif strat2 == sample2:
            numDice = sample2(score2, score1, last)
        elif strat2 == myStrategy:
            numDice = myStrategy(score2, score1, last)
        else:
            numDice = pr1testing.test4(score1, score2, last)

        diceTotal = 0
        #diceString = ""
        i = numDice
        while i > 0:
            d = roll()
            diceTotal += d
            #diceString = diceString + " "  + str(d)
            i = i-1
        #print(str(numDice) + " dice chosen.") 
        #print("Dice rolled: " + diceString)
        #print("Total for this turn: " + str(diceTotal))
        score2 += diceTotal
        if score2 > 100 or last:
            break
        if numDice == 0:
            last = True

    #print("Player 1: " + str(score1) + "   " + "Player 2: " + str(score2))
    if score1 > 100:
        #print("Player 2 wins.")
        return 2
    elif score2 > 100:
        #print("Player 1 wins.")
        return 1
    elif score1 > score2:
        #print("Player 1 wins.")
        return 1
    elif score2 > score1:
        #print("Player 2 wins.")
        return 2
    else:
        #print("Tie.")
        return 3

def manyGames(stra1, stra2, n):
    player1 = 0
    player2 = 0
    ties =0
    i = n
    while i > 0 and i > n//2:
        result = autoplay(stra1, stra2)
        if result == 1:
            player1 += 1
        elif result == 2:
            player2 += 1
        else:
            ties +=1
        i = i-1
    
    while i > 0 and i <= n//2:
        result = autoplay(stra2, stra1)
        if result == 1:
            player1 += 1
        elif result == 2:
            player2 += 1
        else:
            ties +=1
        i = i-1

    print ('')
    print ('Player 1 wins: ' + str(player1))
    print ('Player 2 wins: ' + str(player2))
    print ('Ties: ' + str(ties))

pr1testing.testStrat(myStrategy, 10000)
