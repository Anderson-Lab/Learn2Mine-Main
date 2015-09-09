#NewBot

import random
if input == "": # initialize variables for the first round
    rockCount = paperCount = scissorsCount = 0
    rockTotal = paperTotal = scissorTotal = 0
    rockOther = paperOther = scissorOther = 0
    reverse = {"R":"S","S":"P","P":"R"}
    decisions = ["R","S","P"]
    i = 0
    
elif input == "R":
    rockCount += 1
elif input == "P":
    paperCount += 1
elif input == "S":
    scissorsCount += 1
 
if (i == 0):
    output = decisions[random.randint(0,2)]
    i+=1
elif(i == 1):
    output = input
    i+=1
elif(i == 2):
    output = reverse[input]
    i +=1
elif(i == 3):
    output = "P"
    i+=1
elif(i==4):
    output = "R"
    i = random.randint(0,4)