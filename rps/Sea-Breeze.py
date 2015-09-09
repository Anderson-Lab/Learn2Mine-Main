#Sea-Breeze
from random import random
input = ""
first = random()
if input =="":
    history=[]
if first < .5:
    history.append(input)
    blindR = (random(),"R")
    blindS = (random(),"S")
    blindP = (random(),"P")
    topout = (max(blindP,blindR,blindS))
    output = topout[1]
else:
    history.append(input)
    second = random()
    if second < .5:
        seenrandom = random()
        output="n"
        if 0 <= seenrandom < .33:
            output = "R"
        elif .33 <= seenrandom < .66:
            output = "S"
        elif .66 <= seenrandom <= 1:
            output = "P"


    if second >= .5:
        rcount=0
        pcount=0
        scount=0
        for i in range(len(history)):
            if history[i]=="R":
                rcount+=1*(i*.1)
            elif history[i]=="P":
                pcount+=1*(i*.1)
            elif history[i]=="S":
                scount+=1*(i*.1)
        selector = max((rcount,"r"),(pcount,"p"),(scount,"s"))
        if selector[1]=="r":
            output = "P"
        elif selector[1]=="p":
            output = "S"
        elif selector[1]=="s":
            output = "R"