#DreamCommandoKickers
if input == "":
    Count = "S"
    Change = []
    
if len(Change) < 5:
    
    if input == "R":
        Change.append("R")
        
    elif input == "P":
        Change.append("P")
    
    elif input == "S":
        Change.append("S")
        

else:
    
    P = Change.count("P")
    R = Change.count("R")
    S = Change.count("S")

    if P > R and P > S:
        Count = P
    elif R>S and R>P:
        Count = R
    elif S>R and S>P:
        Count = S

 
output = Count