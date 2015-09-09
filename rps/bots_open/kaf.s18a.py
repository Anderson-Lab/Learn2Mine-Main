# kaf.s18a
# 10% --> random
# 20% --> 3-deep markov chain
# __  --> basic history
from __future__ import division
from random import random, choice
assert 1 / 2 == 0.5  # make sure division import properly ...

# record input
if input == "":  # initialize
    rockCount = paperCount = scissorsCount = 0
    input_seq, output_seq = [], []
    actions = ('R', 'P', 'S')
    beats = {'R': 'P', 'P': 'S', 'S': 'R'}  # value beats key
    cedes = {'R': 'S', 'P': 'R', 'S': 'P'}  # key beats value
    table = {}
    w1 = w2 = None
elif input == "R":
    rockCount += 1
    input_seq.append(input)
elif input == "P":
    paperCount += 1
    input_seq.append(input)
elif input == "S":
    scissorsCount += 1
    input_seq.append(input)

if len(table) > 0:
    if w1 not in table:
        table[w1] = {}
    if w2 not in table[w1]:
        table[w1][w2] = {}
    if input not in table[w1][w2]:
        table[w1][w2][input] = 0
    table[w1][w2][input] += 1
    w1, w2 = w2, input

# choose output
rnd = random()
if rnd > 0.9:
    output = choice(actions)
elif rnd > 0.8:
    if len(input_seq) < 5:
        output = choice(actions)
        prev = table[w2][input]
    output = beats[max(prev, key=prev.get)]
else:
    if rockCount > paperCount and rockCount > scissorsCount:
        output = beats['R']
    elif paperCount > scissorsCount:
        output = beats['P']
    else:
        output = beats['S']
output_seq.append(output)