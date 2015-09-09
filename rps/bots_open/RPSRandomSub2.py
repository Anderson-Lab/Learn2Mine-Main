# RPSRandomSub2
if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = 0
elif input == "R":
	rockCount += 1
elif input == "P":
	paperCount += 1
elif input == "S":
	scissorsCount += 1

list = ["R","P","S"]	
if rockCount > paperCount and rockCount > scissorsCount:
	output = list[2] # paper beats rock
elif paperCount > scissorsCount:
	output = list[1] # scissors beats paper
else:
	output = list[0] # rock beats scissors