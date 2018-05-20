#####################################################################
#Rico Cintron
#Intro to Programming
#2-10-2016
#
#####################################################################



#inport and generate random numbers
from random import randint

#defualt at 0
numRolls = 0
valid = True
playerScore = 0
houseScore = 0
#enter # of rolls, produces number of rolls, if anything aside from integers, message populates.
while valid == True:
    try:
        numRolls = int(input("Enter number of rolls: "))
        valid = False
    except:
        print("Please enter intergers only")
print("numRolls=",numRolls)

for roll in range(numRolls):
#Associate random number generation to die1 and die2, create diesum which is a sum of die1 and die2
    die1 = randint(1,6)
    die2 = randint(1,6)
    diesum = die1 + die2
#Print die1 and die2 and diesum
    print ()
    print ("dice1,",die1)
    print ("dice2,",die2)
    print ()
    print ("Total for this roll",diesum)
    print ()
#display craps if we receive a 7 or 11
    if diesum == 7 or diesum == 11:
        houseScore +=2
        print ("CRAPS, house scores 2")
#if die 1 is the same as die 2, determin whether even our doubles
    elif die1 == die2:
        if die1%2 == 0:
            playerScore +=2
            print("Even Doubles, Player scores 2")
        else:
            houseScore +=2
            print ("Odd Doubles, house scores 2")
#if sum is less than 7 the house receives the points
    elif (diesum < 7) :
        houseScore +=2
        print("Total less than 7, add 2 points for the house!")
#if sum is greater than 7 player receives the points
    elif (diesum > 7):
        playerScore +=2
        print("Total greater than 7, add 2 points for the player!")

#Display current Score
    print ("House Score is currently:",houseScore)
    print ("Player Score is currently:",playerScore)
#Our winner is...
if (houseScore>playerScore):
    print ()
    print ()
    print ()
    print ("House won this time...")
if (playerScore>houseScore):
    print ()
    print ()
    print ()
    print ("Player takes the cake...")
if (houseScore==playerScore):
    print ()
    print ()
    print ()
    print ("TIE,NOT ALLOWED!")
            
