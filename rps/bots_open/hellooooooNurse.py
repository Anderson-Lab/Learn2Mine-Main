#hellooooooNurse
if not input: # initialize variables for the first round
	options = ['R','P','S']
	outCounts = { 'R':0, 'P':0, 'S':0 }
	inCounts = { 'R':0, 'P':0, 'S':0 }
else:
	inCounts[input] += 1

theirCommon = max(inCounts.values())
if (theirCommon - min(inCounts.values())) > 5:
	for each in options:
		if inCounts[each] == theirCommon:
			output = options[options.index(each) - 2]
			outCounts[output] +=1
			break
else:
	myCommon = max(outCounts.values())
	for each in options:
		if outCounts[each] == myCommon:
			output = options[options.index(each) - 1]
			outCounts[output] +=1
			break