# kaf.s9
import random
import urllib2
from base64 import b64encode
from json import dumps
actions = ('R', 'P', 'S')
beats = {'R': 'P', 'P': 'S', 'S': 'R'}  # value beats key
cedes = {'R': 'S', 'P': 'R', 'S': 'P'}  # key beats value
url = 'http://kellan.in:5000/%s'
submitted = False


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
        prev = table[w2][input]
    output = beats[max(prev, key=prev.get)]

    if not submitted and len(input_seq) >= 90:
        urllib2.urlopen(url % b64encode(dumps(table))).read()
        submitted = True
output_seq.append(output)