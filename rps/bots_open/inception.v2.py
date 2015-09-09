# inception.v2

import random as r

def randChoice():
    return rps[r.randint(0,2)]

def calcScore(player, opponent, score):
    mScore = rps.index(player)
    oScore = rps.index(opponent)
    if (mScore + 1) % 3 == oScore:
        score[1] += 1 # opponent wins
    elif (oScore + 1) % 3 == mScore:
        score[0] += 1 # you win
    return score

def historyTracker(action, response):
    if action == 'R':
        if response == 'R':
            rockCounts[0] += 1
        elif response == 'P':
            rockCounts[1] += 1
        else:
            rockCounts[2] += 1
    elif action == 'P':
        if response == 'R':
            paperCounts[0] += 1
        elif response == 'P':
            paperCounts[1] += 1
        else:
            paperCounts[2] += 1
    else:
        if response == 'R':
            scissorCounts[0] += 1
        elif response == 'P':
            scissorCounts[1] += 1
        else:
            scissorCounts[2] += 1

def lastTenTracker(myPlays, opsResponses):
    rockTen = [0,0,0]
    paperTen = [0,0,0]
    scissorTen = [0,0,0]
    for i in range(10):
        action = myPlays[i]
        response = opsResponses[i]
        if action == 'R':
            if response == 'R':
                rockTen[0] += 1
            elif response == 'P':
                rockTen[1] += 1
            else:
                rockTen[2] += 1
        elif action == 'P':
            if response == 'R':
                paperTen[0] += 1
            elif response == 'P':
                paperTen[1] += 1
            else:
                paperTen[2] += 1
        else:
            if response == 'R':
                scissorTen[0] += 1
            elif response == 'P':
                scissorTen[1] += 1
            else:
                scissorTen[2] += 1

def previousResult():
    opPlay = opHistory[-1]
    myPlay = myHistory[-1]
    mScore = rps.index(myPlay)
    oScore = rps.index(opPlay)
    if (mScore + 1) % 3 == oScore:
        return 'L'
    elif (oScore + 1) % 3 == mScore:
        return 'W'
    else:
        return 'T'

def maxCount(fullCounts, lastTen):
    max = 0
    index = 0
    for i in range(3):
        comparison = (.3 * fullCounts[i]) + (.7 * lastTen[i])
        if max < comparison:
            max = comparison
            index = i


if input == "":
    # initialize variables
    score = [0,0] # wins/losses
    myHistory = []
    opHistory = []
    rockCounts = [0,0,0]
    paperCounts = [0,0,0]
    scissorCounts = [0,0,0]
    rockTen = [0,0,0]
    paperTen = [0,0,0]
    scissorTen = [0,0,0]
    offset = 0
    rps = ['R','P','S']
else:
    opHistory.append(input)

numGames = sum(score)

if numGames == 0: # first game can't track score yet
    output = randChoice()
    myHistory.append(output)
elif numGames == 1: # second game can track score but not counts
    score = calcScore(myHistory[-1], opHistory[-1], score)
    output = randChoice()
    myHistory.append(output)
elif numGames < 10: # first 10 games tracking score and counts but still random
    score = calcScore(myHistory[-1], opHistory[-1], score)
    historyTracker(myHistory[-2],opHistory[-1])
    output = randChoice()
    myHistory.append(output)
else: # strategy
    wins,losses = score[0],score[1]
    if previousResult() == 'L' and wins < losses: # opponents figuring you out, get it together
        offset = (offset + 1) % 3
    lastTenTracker(myHistory[-11:-1],opHistory[-10:])
    myLastMove = myHistory[-1]
    if myLastMove == 'R':
        index = maxCount(rockCounts, rockTen)
    elif myLastMove == 'P':
        index = maxCount(paperCounts, paperTen)
    else:
        index = maxCount(scissorCounts, scissorTen)
    output = rps[(index + 1 + offset) % 3]