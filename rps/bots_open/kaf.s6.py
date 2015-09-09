# kaf.s6
from __future__ import division
from random import SystemRandom, random, choice
import math

assert 1 / 2 == 0.5  # make sure division import properly ...


def chunks(l, n):
    ''' Yield successive n-sized chunks from l.
    http://stackoverflow.com/questions/312443/how-do-you-split-a-list-into-evenly-sized-chunks-in-python
    '''
    for i in xrange(0, len(l), n):
        yield l[i:i+n]


# nnet code from http://stackoverflow.com/questions/2276933/good-open-source-neural-network-python-library
# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b - a) * random.random() + a


# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill] * J)
    return m


# our sigmoid function, tanh is a little nicer than the standard 1/(1+e^-x)
def sigmoid(x):
    return math.tanh(x)


# derivative of our sigmoid function, in terms of the output (i.e. y)
def dsigmoid(y):
    return 1.0 - y ** 2


class NN:
    def __init__(self, ni, nh, no):
        # number of input, hidden, and output nodes
        self.ni = ni + 1  # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = [1.0] * self.ni
        self.ah = [1.0] * self.nh
        self.ao = [1.0] * self.no

        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        # set them to random values
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        # last change in weights for momentum
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)

    def update(self, inputs):
        if len(inputs) != self.ni - 1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni - 1):
            # self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            summ = 0.0
            for i in range(self.ni):
                summ += self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(summ)

        # output activations
        for k in range(self.no):
            summ = 0.0
            for j in range(self.nh):
                summ += self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(summ)

        return self.ao[:]

    def backPropagate(self, targets, N, M):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        for k in range(self.no):
            error = targets[k] - self.ao[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error

        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error += output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error

        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] = self.wo[j][k] + N * change + M * self.co[j][k]
                self.co[j][k] = change
                # print N*change, M*self.co[j][k]

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j] * self.ai[i]
                self.wi[i][j] = self.wi[i][j] + N * change + M * self.ci[i][j]
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error += 0.5 * (targets[k] - self.ao[k]) ** 2
        return error

    def test(self, patterns):
        for p in patterns:
            print p[0], '->', self.update(p[0])

    def weights(self):
        print 'Input weights:'
        for i in range(self.ni):
            print self.wi[i]
        print
        print 'Output weights:'
        for j in range(self.nh):
            print self.wo[j]

    def predict(self, x):
        return self.update(x)


    def train(self, patterns, iterations=1000, N=0.5, M=0.1):
        # N: learning rate
        # M: momentum factor
        for i in xrange(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets, N, M)
            if i % 100 == 0:
                pass  # print 'error %-14f' % error
# end nnet code

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
    if input_seq[-1] == output_seq[-1]:
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
else:
    x_mat = {'R': 1 << 0, 'P': 1 << 1, 'S': 1 << 2}
    xs = [[x_mat[x] for x in chunk] for chunk in chunks(output_seq, 30)]
    t_mat = {'R': (1, 0, 0), 'P': (0, 1, 0), 'S': (0, 0, 1)}
    t_mat_inv = {(1, 0, 0): 'R', (0, 1, 0): 'P', (0, 0, 1): 'S'}
    ts = [[t_mat[t] for t in chunk] for chunk in chunks(input_seq, 30)]
    nn = NN(1, 100, 3)
    nn.train(zip(xs[:-1], ts[:-1]))

    def try_play(act):
        xs_pred = [x_mat[x] for x in (output_seq[-29:] + [act])]
        y_pred = nn.predict(xs_pred)
        if y_pred == beats[act]:
            return False
        else:
            return True
    checks = {a: try_play(a) for a in ('R', 'P', 'S')}
    if not any(checks.values()):
        if random() >= 0.8:
            output = twos[''.join(input_seq[-2:])]
        else:
            if rockCount > paperCount and rockCount > scissorsCount:
                output = beats['R']
            elif paperCount > scissorsCount:
                output = beats['P']
            else:
                output = beats['S']
    else:
        output = choice([act for act, ok in checks.iteritems() if ok])
output_seq.append(output)