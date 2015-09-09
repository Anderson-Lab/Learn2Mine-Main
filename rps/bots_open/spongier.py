# spongier
if input == "":
    moveList = []
    rockCount, scissorCount, paperCount = 0
    priorR, priorS, priorP = 0
    nearPriorR, nearPriorS, nearPriorP = 0
    p = ""

moveList.insert(0,input)
numRounds = len(moveList)
nearCut = numRounds/3 # I intend to equally weight the nearest 1/3 moves and the total moves with Bayesian probs.



#GOAL: use the basic counts as bayesian prior probabilities
rockCount == moveList.count("R")
scissorCount == moveList.count("S")
paperCount == moveList.count("P")

priorR = (rockCount/numRounds)
priorS = (scissorCount/numRounds)
priorP = (paperCount/numRounds)

output = ""
if(priorR > priorP & priorR > priorS):
    output = "P"
if(priorS > priorP & priorS > priorR):
    output = "R"
if(priorP > priorR & priorP > priorS):
    output = "S"