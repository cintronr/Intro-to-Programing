###########################################################################
#Rico Cintron
#Intro to Programming
#4/17/2016
#Week 13 Assignment: Nascar!
###########################################################################

#import randint for random number generation as well as, time.
from random import randint
import time

#names of racers and sponsors.
racers = ['CatDaddy','TreeSap','Real Snake','Worm','Lizard','Monkey','Leaf','dirt','Lion','Zebra','Fly','Ant','Mesquito','Elk','Bear','Bird','Turtle','Dog','Elephant','Chicken']
sponsors = ['Mouse Trap inc','Axe inc','Snake Shot inc','Hook inc','Firebreathing inc', 'Banana inc','wind inc','mud inc','Roar inc','Stripped inc','Obnoxious inc','Fire inc',
            'Repelent inc','Tastey inc','destroy inc','soar inc','slow inc','bark inc','trunk inc','cluck inc']


class Nascar:
    #initilizes arguments
    def __init__(self,name,sponsor,):
        self.name = name
        self.sponsor = sponsor
        self.miles = 0
        self.speed = 0
        
     #print list of drivers name and their sponsors   
    def __str__(self):
        output = '''Driver  Name:\t{}\nSponsor Name:\t{}
        Speed:\t\t{}
        Miles:\t\t{:.2f}'''.format(self.name,self.sponsor,self.speed,self.miles)
        return output
    #Method for calculations
    def update(self):
        mph = randint(1,120)
        self.speed = mph
        self.miles += self.speed/60
     #Method to print described values   
    def printName(self):
        print(self.name,self.sponsor)

#list of all drivers listed as well as other stats for the drivers      
cars = []        
for x in range(len(racers)):
    cars += [Nascar(racers[x],sponsors[x])]
    print(cars[x])
    print()


# Solution for start simulation
racing = True
print()
print("Let's go for a ride!")
print("********3***********")
time.sleep(1)
print("********2***********")
time.sleep(1)
print("********1***********")
time.sleep(1)
print("*********GO*********")

# loop that halts program when car reaches 500 mile mark.
lap=1
while (racing):
    for car in cars:
        car.update()
    if car.miles > 500:
        racing = False
    cars.sort(key=lambda x: x.miles, reverse = True) 


    print("Lap#",lap,"The driver currently in the lead is:",cars[0].name,"Sponsor is:",cars[0].sponsor,"!!!!!")
    lap += 1
    time.sleep(.1)
#displays car in whatever place they are in following the loop above, along with sponsor name, speed when finished and miles completed
print()
for x in range (len(cars)):
    print("Car:","In",x+1,"place","\n\n\b",cars[x])
    print()

















    
##
##
##
##while (racing):
##    
##    for car in cars:
##        car.update()
##        
##        if car.miles >= 500:
##            racing = False
##
##
##for x in range (len(cars)):
##    print (cars[x],cars[x].miles)
##
