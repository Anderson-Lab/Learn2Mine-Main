# kaf.s10
# 4-deep markov chains
import random
actions = ('R', 'P', 'S')
beats = {'R': 'P', 'P': 'S', 'S': 'R'}  # value beats key
cedes = {'R': 'S', 'P': 'R', 'S': 'P'}  # key beats value

if input == "":
    input_seq = []
    output_seq = []
    table = {}
    w1 = w2 = w3 = None
else:
    if w1 is not None and w2 is not None and w3 is not None:
        if w1 not in table:
            table[w1] = {}
        if w2 not in table[w1]:
            table[w1][w2] = {}
        if w3 not in table[w1][w2]:
            table[w1][w2][w3] = {}
        if input not in table[w1][w2][w3]:
            table[w1][w2][w3][input] = 0
        table[w1][w2][w3][input] += 1
    w1, w2, w3 = w2, w3, input

if len(input_seq) <= 16:
    output = random.choice(actions)
else:
    if random.random() >= 0.95:
        output = random.choice(actions)
    prev = table[w2][w3][input]
    output = beats[max(prev, key=prev.get)]
output_seq.append(output)