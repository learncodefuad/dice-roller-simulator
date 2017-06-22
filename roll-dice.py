import random

dice = int(raw_input("How much dices do u want? >> "))
dices = []
roll = int(raw_input("How much rolls do u want? >> "))
rolls= []

for n in range(1,roll+1): #Looping through number of rolls
    for m in range(1,dice+1): #looping through number of dices
        dices.append(random.randint(1,6)) #adding random numbers to the dices list(in the number of dices)
        if len(dices) == dice: #checking if length of dices is eq`ual to given dice number
            rolls.append(dices) #adding given numbers of dieces to the rolls lists(in the given number of rolls)
            dices = []  #Making list empty(Here is important)
        else :
            continue



for every_roll in rolls:
    print every_roll
