#I dont Know whats even going on
from random import random

class RockPaperScissors():
    def __init__(self):
        self.history=[]

    def blindRandom(self):
        blindR = (random(),"r")
        blindS = (random(),"s")
        blindP = (random(),"p")
        return(max(blindP,blindR,blindS))

    def seenRandom(self):
        output="n"
        seenrandom = random()
        if 0>=seenrandom>.33:
            output = "r"
        elif .33>=seenrandom>.66:
            output = "s"
        elif .66>=seenrandom>1:
            output = "p"

        return output

    def tactical(self):
        rcount=0
        pcount=0
        scount=0
        for i in range(len(self.history)):
            if self.history[i]=="r":
                rcount+=1*(i*.1)
            elif self.history[i]=="p":
                pcount+=1*(i*.1)
            elif self.history[i]=="s":
                scount+=1*(i*.1)
        selector = max((rcount,"r"),(pcount,"p"),(scount,"s"))
        if selector[1]=="r":
            output = "p"
        elif selector[1]=="p":
            output = "s"
        elif selector[1]=="s":
            output = "r"

        return output




    def main(self):
        self.history.append(input)
        first = random()
        if first < .5:
            output=(self.blindRandom()[1])
        else:
            second = random()
            if second < .5:
                output= self.seenRandom()
            if second > .5:
                output = self.tactical()

RockPaperScissors().main()