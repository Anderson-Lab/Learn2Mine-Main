# kaf.s5
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
    twos = {'RR': 'S', 'RP': 'S', 'RS': 'R', 'PP': 'R', 'PS': 'P', 'SS': 'P'}
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
if len(input_seq) < 30:
    if input_seq[-2] == output_seq[-1]:
        output = choice(actions)
    elif random() >= 0.8:
        output = twos[''.join(input_seq[-2:])]
    else:
        if rockCount > paperCount and rockCount > scissorsCount:
            output = beats['R']
        elif paperCount > scissorsCount:
            output = beats['P']
        else:
            output = beats['S']
output_seq.append(output)