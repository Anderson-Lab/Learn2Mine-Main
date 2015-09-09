#theOfficialHillaryClintonBot

import random

shortTermMemory = []

if input == "":
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
	if len(shortTermMemory) <= 10:
		shortTermMemory.append(["P", rockCount])
	else:
		shortTermMemory.pop()
		shortTermMemory.append(["P", rockCount])
elif input == "P":
	paperCount += 1
	if len(shortTermMemory) <= 10:
		shortTermMemory.append(["S", paperCount])
	else:
		shortTermMemory.pop()
		shortTermMemory.append(["S", paperCount])
elif input == "S":
	scissorsCount += 1
	if len(shortTermMemory) <= 10:
		shortTermMemory.append(["R", scissorsCount])
	else:
		shortTermMemory.pop()
		shortTermMemory.append(["R", scissorsCount])
		
def timeBias(List):
	counter = 0
	newList = []
	for i in List:
		newList.append([i[0], i[1]*(len(List) - counter)])
		#newList.append([i[0], i[1]*(2**(len(List) - counter))])
		counter += 1
	return newList

def shaker(List):
	if (int(random.uniform(0,100)) % 13) == 0:
		return random.choice(["R", "P", "S"])
	else:
		return weightedChoice(List)
		
def weightedChoice(choices):
	total = sum(weight for choice, weight in choices)
	rand = random.uniform(0, total)
	upTo = 0
	for choice, weight in choices:
		if upTo + weight > rand:
			return choice
		upto += weight
	if len(choices) == 0:
		return random.choice(["R", "P", "S"])
	else:
		return random.choice([option for option, weight in choices])	

'''fakeList = [["P",1],["H",1],["L",1]]	
fun = timeBias(fakeList)
print fun'''

output = shaker(timeBias(shortTermMemory))