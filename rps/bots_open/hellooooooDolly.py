#hellooooooDolly
if not input: # initialize variables for the first round
	options = ['R','P','S']
	outCounts = { 'R':0, 'P':0, 'S':0 }
	roundCount = 0

if roundCount%2 == 0:
	common = max(outCounts.values())
	for each in options:
		if outCounts[each] == common:
			output = options[options.index(each) - 1]
			break
else:
	output = options[options.index(lastOut) - 2]

outCounts[output] +=1
lastOut = output
roundCount += 1