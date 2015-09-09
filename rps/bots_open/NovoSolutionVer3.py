# NovoSolutionVer3
import random

reversePsychology = []

if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
	
elif input == "R":
	rockCount += 1
	if len(reversePsychology) < 5:
		reversePsychology.append(["P",rockCount])
	else:
		reversePsychology.pop(0)
		reversePsychology.append(["P",rockCount])
		
elif input == "P":
	paperCount += 1
	if len(reversePsychology) < 5:
		reversePsychology.append(["S",paperCount])
	else:
		reversePsychology.pop(0)
		reversePsychology.append(["S",paperCount])
	
elif input == "S":
	scissorsCount += 1
	if len(reversePsychology) < 5:
		reversePsychology.append(["R", scissorsCount])
	else:
		reversePsychology.pop(0)
		reversePsychology.append(["R", scissorsCount])
		
		
def weightedChoice(choices):
	total = sum(weight for choice, weight in choices)
	rand = random.uniform(0, total)
	upTo = 0
	for choice, weight in choices:
		if upTo + weight > rand:
			return choice
		upto += w
	if len(choices) == 0:
		return random.choice(["R", "P", "S"])
	else:
		return random.choice([option for option, weight in choices])	
	
output = weightedChoice(reversePsychology)