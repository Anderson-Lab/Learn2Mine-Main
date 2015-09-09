# kaf.s19g
# s3 was 0.9, this is 0.2
from __future__ import division
from random import SystemRandom, random, choice
assert 1 / 2 == 0.5  # make sure division import properly ...

# record input
if input == "":  # initialize
    rockCount = paperCount = scissorsCount = 0
    input_seq, output_seq = [], []
    rng = SystemRandom()
    actions = ('R', 'P', 'S')
    beats = {'R': 'P', 'P': 'S', 'S': 'R'}  # value beats key
    cedes = {'R': 'S', 'P': 'R', 'S': 'P'}  # key beats value
elif input == "R":
    rockCount += 1
    input_seq.append(input)
elif input == "P":
    paperCount += 1
    input_seq.append(input)
elif input == "S":
    scissorsCount += 1
    input_seq.append(input)

# choose output
if random() > 0.2:
    output = choice(actions)
else:
    if rockCount > paperCount and rockCount > scissorsCount:
        output = beats['R']
    elif paperCount > scissorsCount:
        output = beats['P']
    else:
        output = beats['S']
output_seq.append(output)