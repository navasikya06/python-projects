def myStrategy(myscore, theirscore, last): 
    if myscore == 0:
        return (100 - myscore)//3 #The total is the difference of 100 and myscore, so my score doesn't go above 100. I div by 3, because the most probable value for a collection of random dice from 0-5 would oscillate around 2.5, so their sum is like to be 2.5*numDice. I choose 3 as median and to be safe.
    elif myscore >= 97: #The purpose of this is to determine a good time to pass in the 90-100 range, instead of playing 1 or 2. I tried this to be 98-100, but when running pr1testing.testStrat, the Terminal returns error. When I ran autoplayLoud, or manyGames of myStrategy vs. Test 8, 9, 10, and 11, myStrategy always wins. But the bulk testStrat indicates that the tests win. Regardless, I actually did start with 97, as I tried a few values in the 90-100 range to see which plays well with which test, but 97 does seem to perform best. 
        return 0
    elif last:
        return ((theirscore - myscore + 3)*2)//5 #If opponent plays 0, I take the difference between our scores, added 3, and divide by the most probable value of a random dice, in order to likely have a higher score than opponent's. I chose to add 3 after trying out different runs, and finding that 3 is a good number.
    elif myscore < 97:
        return (100 - myscore)//4 # Other than all the important cases like above, I would play a number of dice that has the same reasonging as first step, but more conservative, to be safe about not going over 100 at the higher score range. 