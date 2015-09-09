# kaf.s15
# parent: s13
# 4-deep markov chains
import random
actions = ('R', 'P', 'S')
beats = {'R': 'P', 'P': 'S', 'S': 'R'}  # value beats key
cedes = {'R': 'S', 'P': 'R', 'S': 'P'}  # key beats value

if input == "":
    rocks = papers = scissors = 0
    input_seq = []
    output_seq = []
    table = {}
    w1 = w2 = w3 = None
else:
    {'R': rocks, 'P': papers, 'S': scissors}[input] += 1

    if w1 is not None and w2 is not None and w3 is not None:
        if w1 not in table:
            table[w1] = {}
        if w2 not in table[w1]:
            table[w1][w2] = {}
        if w3 not in table[w1][w2]:
            table[w1][w2][w3] = []
        table[w1][w2][w3].append(input)
    w1, w2, w3 = w2, w3, input

if len(input_seq) <= 8:
    if random() > 0.9:
        output = random.choice(actions)
    else:
        if rocks > papers and rocks > scissors:
            output = beats['R']
        elif papers > scissors:
            output = beats['P']
        else:
            output = beats['S']
else:
    if random.random() >= 0.9:
        output = random.choice(actions)
    prev = table[w2][w3][input]
    output = beats[random.choice(prev)]
output_seq.append(output)