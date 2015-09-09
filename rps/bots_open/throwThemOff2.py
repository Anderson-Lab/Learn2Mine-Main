#throwThemOff2
if input == "": # initialize variables for the first round
	import random
	count = 0
	orockCount = opaperCount = oscissorsCount = 0
	
if count == 0 or count%6 == 0:
	output = random.choice(['R','P','S'])
else:
	if orockCount > opaperCount and orockCount > oscissorsCount:
		output = "S" # scissors beats paper beats rock
		opaperCount += 1
	elif opaperCount > oscissorsCount:
		output = "R" # rock beats scissors beats paper
		oscissorsCount += 1
	else:
		output = "P" # paper beats rock beats scissors
		orockCount += 1
count += 1