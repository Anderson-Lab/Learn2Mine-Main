#PossiblyIntelligent
import random
if input =="":
	numRock = numPaper = numScissors = 0

numRock = input.count("R")
numPaper = input.count("P")
numScissors = input.count("S")

if numRock > numPaper and numRock > numScissors:
	output = "P"
if numPaper > numScissors:
	output = "S"
else:
	output = "R"

if numRock==numPaper and numRock==numScissors:
	output = random.choice("R","P","S")
if numPaper==numScissors:
	output = random.choice(["S", "P"])
if numRock==numScissors:
	output = random.choice(["R", "S"])
if numRock==numPaper:
	output = random.choice(["R", "P"])