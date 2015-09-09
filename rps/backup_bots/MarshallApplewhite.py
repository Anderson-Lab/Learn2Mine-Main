#Marshall Applewhite
import random 
if input=="":
    rockCount = paperCount = scissorsCount = 0
elif input == "R":
    rockCount += 1
    output="S"
elif input == "P":
    paperCount += 1
    output='R'
elif input == "S":
    scissorsCount += 1
    output='P'
 
choice=list()
choice=["R",'P',"S",]
if rockCount+ paperCount+scissorsCount%5==0:
    p=random.randrange(0,3)
    pick=choice[p]
    output=pick