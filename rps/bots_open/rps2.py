#rps2
import random
if (input == ""): #initialize variables for the first round
	opponentMoves = ""
	output = random.choice(["R", "P", "S"])
else:
	opponentMoves = opponentMoves + input
	if (len(opponentMoves) < 5):
		output = random.choice(["R", "P", "S"])
	else: #analyze opponent's last five moves
		if (len(opponentMoves) > 5):
			opponentMoves = opponentMoves[1:6]
		rockCount = paperCount = scissorsCount = 0
		for i in range(5):
			if (opponentMoves[i] == "R"):
				rockCount = rockCount + 1
			elif (opponentMoves[i] == "P"):
				paperCount = paperCount + 1
			else: 
				scissorsCount = scissorsCount + 1
		if (rockCount == 3):
			output = "P"
		elif (paperCount == 3):
			output = "S"
		elif (scissorsCount == 3):
			output = "R"
		elif (rockCount == paperCount):
			output = random.choice(["P", "S"])
		elif (rockCount == scissorsCount):
			output = random.choice(["P", "R"])
		else:
			output = random.choice(["S", "R"])