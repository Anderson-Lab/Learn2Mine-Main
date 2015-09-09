# patternDj03

import random
solutions = {'R':'P', 'P':'S', 'S':'R'}
output = ""
patterns = {}
pattern = []

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

    if(len(matches)>4):
        for j in range(3, 10):
            for i in range(0, j):
                pattern.append(matches[len(matches)+(i-j)])
            for i in range(0, len(matches)-(j+1)):
            	if(pattern == matches[i:i+j]):
            		txt = keyBuilder(pattern + list(matches[i+(j+1)]))
            		if txt in patterns:
            			patterns[txt] += 1
            		else:
            			patterns[txt] = 1
        if len(patterns) > 0:
            bestPattern = max(patterns, key=patterns.get)
            last = bestPattern[(len(bestPattern)-1)]
            output = solutions[last]
        else:
        	output = random.choice(solutions.keys())
    if(output == ""):
        output = random.choice(solutions.keys())