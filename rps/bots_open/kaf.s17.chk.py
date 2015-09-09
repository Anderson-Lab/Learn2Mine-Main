# kaf.s17.chk
from sklearn import hmm
from __future__ import division
from random import SystemRandom, choice

assert 1 / 2 == 0.5  # make sure division import properly ...

# record input
if input == "":  # initialize
    rockCount = paperCount = scissorsCount = 0
    input_seq, output_seq = [], []
    rng = SystemRandom()
    actions = ('R', 'P', 'S')
    # dict of moves such that value beats key
    beats = {actions[i]: actions[(i + 1) % 3] for i in xrange(3)}
    model = hmm.GaussianHMM(2, 'full')
elif input == 'R':
    rockCount += 1
    input_seq.append(input)
elif input == 'P':
    paperCount += 1
    input_seq.append(input)
elif input == 'S':
    scissorsCount += 1
    input_seq.append(input)

# choose output
if len(input_seq) <= 10:
    if rng.random() >= 0.95:
        output = choice(actions)
    else:
        model.fit([input_seq])
        z2 = model.predict(input_seq)
        print "z2 = %s" % (z2,)
        output = choice(actions)

output_seq.append(output)