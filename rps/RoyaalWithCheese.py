#RoyaalWithCheese
import random

if input == "":
    Count = "S"
    ShitList = []
    
if len(ShitList) < 5:
    
    if input == "R":
        ShitList.append("R")
        
    elif input == "P":
        ShitList.append("P")
    
    elif input == "S":
        ShitList.append("S")
        

else:
    
    P = ShitList.count("P")
    R = ShitList.count("R")
    S = ShitList.count("S")

    if P > R and P > S:
        Count = P
    elif R>S and R>P:
        Count = R
    elif S>R and S>P:
        Count = S
        
output = Count
