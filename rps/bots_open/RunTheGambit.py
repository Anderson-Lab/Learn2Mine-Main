#RunTheGambit
if input == "": # initialize variables for the first round
	import random
	inputString = ""
	outputString = ""

	gambitCount = 0
	gambitofChoice = ""
	gambits = ["RRR", "PPP", "PSR", "RSP", "RPP", "PSS", "PSP", "SSS"]

	if gambitCount == 0: gambitofChoice = random.choice(gambits)
	output = gambitofChoice[gambitCount]
	outputString += output
	gambitCount = (gambitCount + 1) % 3

else:
	inputString += input

	if len(inputString) < 4: #run gambit
		output = gambitofChoice[gambitCount]
		outputString += output
		gambitCount = (gambitCount + 1) % 3
	elif len(inputString) % 4 == 0: #random switch up
		output = random.choice(['R','P','S'])
		outputString += output
	else: #least used output
		count = outputString.count('R')
		output = 'R'
		for throw in ['P','S']:
			newCount = outputString.count(throw)
			if newCount < count: 
				count = newCount
				output = throw