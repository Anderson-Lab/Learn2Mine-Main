import random 
if input=="":
    rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1
choice=list()
choice=["P","R","S"]
if rockCount > paperCount and rockCount > scissorsCount:
	output = "P" 
elif paperCount > scissorsCount:
	output = "S" 
else:
	output = "R" 
if rockCount+ paperCount+scissorsCount%5==0:
    p=random.randrange(0,3)
    pick=choice[p]
    output=pick