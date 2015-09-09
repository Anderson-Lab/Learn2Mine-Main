# test02

import random
solutions = {'R':'P', 'P':'S', 'S':'R'}
output = ""

if input == "":
    output = random.choice(solutions.keys())
    count = {'R':0, 'P':0, 'S':0}
    matches = []
    pattern = []
else:
    matches.append(input)
    count[input] = count[input] + 1
    if(len(matches)>3):
        for i in range(0, 3):
            pattern = matches[len(matches)-(i+1)]
        for i in range(0, len(matches)-4):
            if pattern[0:2] == matches[i:i+2]:
                output = solutions[matches[i+3]]
    if(output == ""):
        output = random.choice(solutions.keys())