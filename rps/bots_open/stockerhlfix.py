#stockerhl fix

import Math
import random

if(input == ""):
    tier = ["R","P","S"]
    total = 1
    perAction = {"R":0,"P":0,"S":0}
if(input == "R"):
    perAction["R"] += 1  
if(input == "P"):
    perAction["P"] += 1    
if(input == "S"):
    perAction["S"] += 1
mod = ((perAction(tier[0])/total)*(perAction(tier[2])/total))*.5
output = tier[round(mod+Math.sin(random.random()))]
total+=1
tier[1] = max(perAction["R"],perAction["P"],perAction["S"])
tier[2] = min(perAction["R"],perAction["P"],perAction["S"])