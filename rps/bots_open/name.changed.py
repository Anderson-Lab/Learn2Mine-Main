# name.changed
import random
rps = ['R','P','S']
output = ""
if input == "": # initialize variables for the first round
	wins = 0
	losses = 0
	opponentHistory = []
	myHistory = []
	firstTen = 0
	myLastTen = []
	opLastTen = []
	rockCounts =  	[0,  ## rock to rock [0]
			  	   	 0,  ## rock to paper [1]
			  	   	 0]  ## rock to scissors [2]

	paperCounts = 	[0,  ## paper to rock [0]
			       	 0,  ## paper to paper [1]
			       	 0]  ## paper to scissors [2]

	scissorCounts = [0,  ## scissors to rock [0]
			  		 0,  ## scissors to paper [1]
			  		 0]  ## scissors to scissors [2]
else:
	opponentHistory.append(input)

if firstTen < 10:
	if firstTen < 2: ## first two times
		pass
	else:
		if firstTen == 2:
			for i in range(len(opponentHistory)):
				oScore = rps.index(opponentHistory[i])
				mScore = rps.index(myHistory[i])
				if mScore == (oScore + 1) % 3:
					wins += 1
				elif oScore == (mScore + 1) % 3:
					losses += 1
		else:
			oScore = rps.index(opponentHistory[len(opponentHistory)-1])
			mScore = rps.index(myHistory[len(myHistory)-1])
			if mScore == (oScore + 1) % 3:
				wins += 1
			elif oScore == (mScore + 1) % 3:
				losses += 1
		# ratio tracking
		numMatches = len(opponentHistory)

		# opponent played rock last

		if opponentHistory[numMatches-1] == 'R':
			if myHistory[len(myHistory)-2] == 'R':
				# opponent played rock in response to rock
				rockCounts[0] += 1
			elif myHistory[len(myHistory)-2] == 'P':
				# opponent played rock in response to paper
				rockCounts[1] += 1
			else: 
				# opponent played rock in response to scissors
				rockCounts[2] += 1

		# opponent played paper last

		elif opponentHistory[numMatches-1] == 'P':
			if myHistory[len(myHistory)-2] == 'R':
				# opponent played paper in response to rock
				paperCounts[0] += 1
			elif myHistory[len(myHistory)-2] == 'P':
				# opponent played paper in response to paper
				paperCounts[1] += 1
			else: 
				# opponent played paper in response to scissors
				paperCounts[2] += 1

		#opponent played scissors last
				
		else:
			if myHistory[len(myHistory)-2] == 'R':
				# opponent played scissors in response to rock
				scissorCounts[0] += 1
			elif myHistory[len(myHistory)-2] == 'P':
				# opponent played scissors in response to paper
				scissorCounts[1] += 1
			else: 
				# opponent played scissors in response to scissors
				scissorCounts[2] += 1

	select = random.randint(0, 2)
	output = rps[select]
	myHistory.append(output)
	firstTen += 1
else:
	numMatches = len(opponentHistory)
	oScore = rps.index(opponentHistory[len(opponentHistory)-1])
	mScore = rps.index(myHistory[len(myHistory)-1])
	if mScore == (oScore + 1) % 3:
		wins += 1
	elif oScore == (mScore + 1) % 3:
		losses += 1
	if firstTen == 10:
		myLastTen += myHistory
		opLastTen += opponentHistory
		rockTen = [0,0,0]
		paperTen = [0,0,0]
		scissorTen = [0,0,0]
	else:
		myLastTen = myLastTen[1:] + [myHistory[len(myHistory)-2]]
		opLastTen = opLastTen[1:] + [opponentHistory[numMatches-1]]
		rockTen = [0,0,0]
		paperTen = [0,0,0]
		scissorTen = [0,0,0]
		for i in range(10):
			if opLastTen[i] == 'R':
				if myLastTen == 'R':
					rockTen[0] += 1
				elif myLastTen == 'P':
					rockTen[1] += 1
				else:
					rockTen[2] += 1
			elif opLastTen == 'P':
				if myLastTen == 'R':
					paperTen[0] += 1
				elif myLastTen == 'P':
					paperTen[1] += 1
				else:
					paperTen[2] += 1
			else:
				if myLastTen == 'R':
					scissorTen[0] += 1
				elif myLastTen == 'P':
					scissorTen[1] += 1
				else:
					scissorTen[2] += 1


	# opponent played rock last

	if opponentHistory[numMatches-1] == 'R':
		if myHistory[len(myHistory)-2] == 'R':
			# opponent played rock in response to rock
			rockCounts[0] += 1
		elif myHistory[len(myHistory)-2] == 'P':
			# opponent played rock in response to paper
			rockCounts[1] += 1
		else: 
			# opponent played rock in response to scissors
			rockCounts[2] += 1

	# opponent played paper last

	elif opponentHistory[numMatches-1] == 'P':
		if myHistory[len(myHistory)-2] == 'R':
			# opponent played paper in response to rock
			paperCounts[0] += 1
		elif myHistory[len(myHistory)-2] == 'P':
			# opponent played paper in response to paper
			paperCounts[1] += 1
		else: 
			# opponent played paper in response to scissors
			paperCounts[2] += 1

	#opponent played scissors last
			
	else:
		if myHistory[len(myHistory)-2] == 'R':
			# opponent played scissors in response to rock
			scissorCounts[0] += 1
		elif myHistory[len(myHistory)-2] == 'P':
			# opponent played scissors in response to paper
			scissorCounts[1] += 1
		else: 
			# opponent played scissors in response to scissors
			scissorCounts[2] += 1	
	

	lastplayed = myHistory[len(myHistory)-1]
	rockAverages = [0,0,0]
	paperAverages = [0,0,0]
	scissorAverages = [0,0,0]
	for i in range(3):
		rockAverages[i] = (.3 * rockCounts[i]) + (.7 * rockTen[i])
	for i in range(3):
		paperAverages[i] = (.3 * paperCounts[i]) + (.7 * paperTen[i])
	for i in range(3):
		scissorAverages[i] = (.3 * scissorCounts[i]) + (.7 * scissorTen[i])
	counter = 'R'
	if lastplayed == 'R':
		myMax = 0
		counter = 'R'
		for i in range(3):
			if rockAverages[i] > myMax:
				myMax = rockAverages[i]
				counter = rps[(i+1)%3]
	elif lastplayed == 'P':
		myMax = 0
		counter = 'P'
		for i in range(3):
			if paperAverages[i] > myMax:
				myMax = paperAverages[i]
				counter = rps[(i+1)%3]
	else:
		myMax = 0
		counter = 'S'
		for i in range(3):
			if scissorAverages[i] > myMax:
				myMax = scissorAverages[i]
				counter = rps[(i+1)%3]
	output = counter