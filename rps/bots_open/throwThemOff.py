#throwThemOff
if input == "": # initialize variables for the first round
	import random
	count = 0
	irockCount = ipaperCount = iscissorsCount = 0
	orockCount = opaperCount = oscissorsCount = 0
elif input == "R":
	irockCount += 1
elif input == "P":
	ipaperCount += 1
elif input == "S":
	iscissorsCount += 1
	
if count == 0 or count%6 == 0:
	output = random.choice(['R','P','S'])
elif count%4 == 0:
	if orockCount > opaperCount and orockCount > oscissorsCount:
		output = "S" # scissors beats paper beats rock
		opaperCount += 1
	elif opaperCount > oscissorsCount:
		output = "R" # rock beats scissors beats paper
		oscissorsCount += 1
	else:
		output = "P" # paper beats rock beats scissors
		orockCount += 1
else:
	if irockCount > ipaperCount and irockCount > iscissorsCount:
		output = "P" # paper beats rock
		opaperCount += 1
	elif ipaperCount > iscissorsCount:
		output = "S" # scissors beats paper
		oscissorsCount += 1
	else:
		output = "R" # rock beats scissors
		orockCount += 1
count += 1