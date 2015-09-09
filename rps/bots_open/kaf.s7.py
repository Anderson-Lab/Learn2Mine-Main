# kaf.s7
import random
actions = ('R', 'P', 'S')
beats = {'R': 'P', 'P': 'S', 'S': 'R'}  # value beats key
cedes = {'R': 'S', 'P': 'R', 'S': 'P'}  # key beats value

if input == "":
    input_seq = []
    output_seq = []
    table = {}
    w1 = w2 = None
else:
    if w1 not in table:
        table[w1] = {}
    if w2 not in table[w1]:
        table[w1][w2] = {}
    if input not in table[w1][w2]:
        table[w1][w2][input] = 0
    table[w1][w2][input] += 1
    w1, w2 = w2, input

if len(input_seq) <= 15:
    output = random.choice(actions)
else:
    if random.random() >= 0.95:
        output = random.choice(actions)
    output = max(table[w2][input], key=table[w2][input].get)
output_seq.append(output)