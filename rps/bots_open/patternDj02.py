# patternDj02

import random
solutions = {'R':'P', 'P':'S', 'S':'R'}
output = ""
patterns = {}
pattern = []
#countPattern = {}
#print("Input:", input)

def keyBuilder(pattern):
	txt = ""
	for i in range(0, len(pattern)):
		txt += pattern[i]
	return txt

if input == "":
    output = random.choice(solutions.keys())
    count = {'R':0, 'P':0, 'S':0}
    matches = []
else:
    matches.append(input)
    count[input] = count[input] + 1
    if(len(matches)>3):
        for i in range(0, 3):
            pattern.append(matches[len(matches)+(i-3)])
        for i in range(0, len(matches)-4):
        	if(pattern == matches[i:i+3]):
        		#print "pattern found!"
        		txt = keyBuilder(pattern + list(matches[i+4]))
        		if txt in patterns:
        			patterns[txt] += 1
        		else:
        			patterns[txt] = 1
        if len(patterns) > 0:
        	bestPattern = max(patterns, key=patterns.get)
        	#print "bestPattern " + bestPattern
        	#print "repetitions " + str(patterns[bestPattern])
        	#listOf = bestPattern.split(None, len(bestPattern))
        	last = bestPattern[(len(bestPattern)-1)]
        	#print "last " + last
        	output = solutions[last]
        	#print "output " + output
        else:
        	output = random.choice(solutions.keys())
    if(output == ""):
        output = random.choice(solutions.keys())