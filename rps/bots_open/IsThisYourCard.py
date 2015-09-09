#IsThisYourCard
import random

if input == "":
    switchBit = 0
    rockCnt = 0
    sciCnt = 0
    papCnt = 0


if rockCnt == 3 or sciCnt == 3 or papCnt == 3:
    switchBit = 4
    
if switchBit == 0:
    output = random.choice(["R","P","S"])
    switchBit = random.choice([1,2,3])
    
    
elif switchBit == 1:
    if input == "R":
        output = "P"
        rockCnt = rockCnt + 1
        
    elif input == "P":
        output = "S"
        papCnt = papCnt + 1
        
    else:
        output = "R"
        sciCnt = sciCnt + 1
    
    switchBit = random.choice([2,3])
    
    
elif switchBit == 2:
    if input == "R":
        output = "S"
        rockCnt = rockCnt + 1
        
    elif input == "P":
        output = "R"
        papCnt = papCnt + 1
        
    else:
        output = "P"
        sciCnt = sciCnt + 1
        
    switchBit = random.choice([1,3])
    
elif switchBit == 3:
    output = "P"
    switchBit = random.choice([0,1,2])
    
else:
    if rockCnt == 3:
        output = "R"
        rockCnt = 0
        sciCnt = 0
        papCnt = 1
        
    elif sciCnt == 3:
        output = "S"
        rockCnt = 1
        sciCnt = 0
        papCnt = 0
        
    else:
        output = "P"
        rockCnt = 0
        sciCnt = 1
        papCnt = 0
    
    switchBit = random.choice([0,1,2,3])