#RPSBotHLS2
from __future__ import print_function
# This must be the first statement before other statements.
# You may only put a quoted or triple quoted string, 
# Python comments or blank lines before the __future__ line.

def print(*args, **kwargs):
    pass

import math
import random

if input == "":
    tier = ["R","P","S"]
    total = 1
    perAction = {"R":0,"P":0,"S":0}
elif input == "R":
    perAction["R"] += 1  
elif input == "P" :
    perAction["P"] += 1    
elif(input == "S"):
    perAction["S"] += 1

#print("Tier",tier[0],tier[1],tier[2])
print("Action",perAction[tier[0]],perAction[tier[1]],perAction[tier[2]],total)
mod = ((perAction[tier[0]]/total)*(perAction[tier[2]]/total))*.5
#print(mod)
output = tier[int(mod+math.sin(random.random()))]
#print(output)
total+=1

if(perAction["R"]>perAction["S"] and perAction["R"]>perAction["P"]):
    if(perAction["S"]>perAction["P"]):
        tier[0] = "S"
        tier[1] = "R"
        tier[2] = "P"
    else:
        tier[0] = "P"
        tier[1] = "R"
        tier[2] = "S"
elif(perAction["S"]>perAction["R"] and perAction["S"]>perAction["P"]):
    if(perAction["R"]>perAction["P"]):
        tier[0] = "R"
        tier[1] = "S"
        tier[2] = "P"
    else:
        tier[0] = "P"
        tier[1] = "S"
        tier[2] = "R"
elif(perAction["P"]>perAction["R"] and perAction["P"]>perAction["S"]):
    if(perAction["R"]>perAction["S"]):
        tier[0] = "R"
        tier[1] = "P"
        tier[2] = "S"
    else:
        tier[0] = "S"
        tier[1] = "P"
        tier[2] = "R"
