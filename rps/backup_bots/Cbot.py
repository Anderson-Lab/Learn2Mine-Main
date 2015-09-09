#Cbot
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
choice=["R","S"]
output = "P" 
if rockCount+ paperCount+scissorsCount%5==0:
    p=random.randrange(0,2)
    pick=choice[p]
    output=pick