#AlexJacobs

import random


hcount = 0


def histNode(input):
    history.append(input)

    return history

if hcount%6 == 0:
    output  = random.choice("RPS")

if not input:
    output = random.choice("R","P","S")
    history = []

else:
    hcount += 1

    memory = histNode(input)

    r_In = memory.count('R')
    p_In = memory.count('P')
    s_In = memory.count('S')

    r2p = r_In - p_In
    r2s = r_In - s_In
    p2s = p_In - s_In


    t = random.randint(1,10)

    if t > 5:
        output = input
    else:
        if input == "R":
            output = "P"
        if input == "P":
            output = "S"
        if input == "S":
            output = "R"



   # x = [r2p,r2s,p2s]
   # print x

   # out = x.index(max(x))

   # if out == 0:
   #     output = 'P'
   # if out == 1:
   #     output = 'P'
   # if out == 2:
   #     output = 'S'
   # else:
   #     output = 'R'