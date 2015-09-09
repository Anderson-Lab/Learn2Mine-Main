#RPSBotHLS3

import math
import random

if input == "":
    tier = ["R","P","S"]
    total = 1.0
    inputAction = {"R":0.0,"P":0.0,"S":0.0}
    outputAction = {"R":0.0,"P":0.0,"S":0.0}
elif input == "R":
    inputAction["R"] += 1.0  
elif input == "P" :
    inputAction["P"] += 1.0   
elif(input == "S"):
    inputAction["S"] += 1.0

#print("Tier",tier[0],tier[1],tier[2])
#print("inputAction",inputAction[tier[0]],inputAction[tier[1]],inputAction[tier[2]],total)
#print("OutputAction",outputAction[tier[0]],outputAction[tier[1]],outputAction[tier[2]],total)
#print((outputAction[tier[0]]//total),(outputAction[tier[2]]//total))
mod = ((outputAction[tier[0]]/total)-(outputAction[tier[2]]/total))
#print(mod)
output = tier[int(mod+math.sin(random.random()))]
outputAction[output]+=1
#print(output)
total+=1

if(outputAction["R"]>outputAction["S"] and outputAction["R"]>outputAction["P"]):
    if(outputAction["S"]>outputAction["P"]):
        tier[0] = "S"
        tier[1] = "R"
        tier[2] = "P"
    else:
        tier[0] = "P"
        tier[1] = "R"
        tier[2] = "S"
elif(outputAction["S"]>outputAction["R"] and outputAction["S"]>outputAction["P"]):
    if(outputAction["R"]>outputAction["P"]):
        tier[0] = "R"
        tier[1] = "S"
        tier[2] = "P"
    else:
        tier[0] = "P"
        tier[1] = "S"
        tier[2] = "R"
elif(outputAction["P"]>outputAction["R"] and outputAction["P"]>outputAction["S"]):
    if(outputAction["R"]>outputAction["S"]):
        tier[0] = "R"
        tier[1] = "P"
        tier[2] = "S"
    else:
        tier[0] = "S"
        tier[1] = "P"
        tier[2] = "R"