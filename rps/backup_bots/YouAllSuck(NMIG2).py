#YouAllSuck(NMIG2)
import random
if input == "":
	opponentPrevMoves = []
	output = random.choice(["R","P","S"])
else:
	if (random.random() < 0.05):
		output = random.choice(["R","P","S"])
	else:	
		opponentLastMove = input
		rockCount = paperCount = scissorsCount = 0
		for i in range(len(opponentPrevMoves) - 1):
			if (opponentPrevMoves[i] == opponentLastMove):
				if (opponentPrevMoves[i] == "P"):
					paperCount += 1
				elif (opponentPrevMoves[i] == "R"):
					rockCount += 1
				elif (opponentPrevMoves[i] == "S"):
					scissorsCount += 1
		if rockCount > paperCount and rockCount > scissorsCount:
			output = "P"
		elif paperCount > scissorsCount:
			output = "S"
		else:
			output = "R"
		opponentPrevMoves.append(opponentLastMove)