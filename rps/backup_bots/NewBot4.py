# NewBot4

import random
if input == "": # initialize variables for the first round
    rockCount = paperCount = scissorsCount = 0
    rockTotal = paperTotal = scissorTotal = 0
    rockOther = paperOther = scissorOther = 0
    rpsDict = {"R":rockCount,"P":paperCount,"S":scissorsCount}
    reverse = {"R":"S","S":"P","P":"R"}
    decisions = ["R","S","P"]
    i = 0
    
elif input == "R":
    rpsDict["R"]+=1
elif input == "P":
    rpsDict["P"]+=1
elif input == "S":
    rpsDict["S"]+=1 
 
if(rpsDict["R"]>rpsDict["P"]*3 and rpsDict["R"]>rpsDict["S"]*3 ):
    i = 1  
elif(rpsDict["P"]>rpsDict["R"]*3 and rpsDict["P"]>rpsDict["S"]*3 ):
    i = 1  
elif(rpsDict["S"]>rpsDict["P"]*3 and rpsDict["S"]>rpsDict["R"]*3 ):
    i = 1
 
if (i == 0):
    output = decisions[random.randint(0,2)]
    i+=1
elif(i == 1):
    if(rpsDict["R"]>rpsDict["P"] and rpsDict["R"]>rpsDict["S"]):
        output = "R"
    elif (rpsDict["P"]>rpsDict["S"]):
        output = "P"
    else:
        output = "S"
    i+=1
elif(i == 2):
    output = reverse[input]
    i +=1
elif(i == 3):
    output = input
    i+=1
elif(i==4):
    output = "R"
    i = random.randint(0,4)