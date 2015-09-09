outRandom2

import random

if input == "": # initialize variables for the first round
	inRockCount = inPaperCount = inScissorsCount = 0
	outPaperCount = outScissorsCount = outRockCount = 0
	move = 0
elif input == "R":
	inRockCount += 1
	move += 1
elif input == "P":
	inPaperCount += 1
	move += 1
elif input == "S":
	inScissorsCount += 1
	move += 1

if move <= 15:    #first 15 moves
	if move > 0 and move < 5:
		output = random.choice(["R", "P", "S"])
		move += 1
		if output = "R":
			outRockCount += 1
		if output = "P":
			outPaperCount += 1
		if output = "S":
			outScissorsCount += 1
	if move >= 5 and move < 10:
		output = random.choice(["P", "S"])
		move += 1
		if output = "P":
			outPaperCount += 1
		if output = "S":
			outScissorsCount += 1
	if move > 10 and move <= 15:
		output = random.choice(["R", "P"])
		move += 1
		if output = "R":
			outRockCount += 1
		if output = "P":
			outPaperCount += 1



if outRockCount < outPaperCount and outRockCount < outScissorsCount:
	output = "R" 
	outRockCount += 1

elif outPaperCount < outScissorsCount and outPaperCount < outRockCount:
	output = "P" 
	outPaperCount += 1
elif outScissorsCount < outRockCount and outScissorsCount < outPaperCount:
	output = "S" 
	outScissorsCount += 1
else:
	output = random.choice(["R", "S", "P"])