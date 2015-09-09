#StringerBell

import random as r

if input == "":
    rockCount = paperCount = scissorCount = 0
    beats = {'R':'S','S':'P','P':'R'}
    cedes = {'R':'P','P':'S','S':'R'}
    myLastMoves = []
    opponentMoves = []

elif input == 'P':
    paperCount += 1 
    if r.random() > 0.85 or len(myLastMoves) == 0:
        output = r.choice(['P','R','S'])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "R":
        output = r.choice(["P","S"])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "P":
        output = r.choice(["R","S"])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "S":
        output = r.choice(["R","P"])
        myLastMoves.append(output)
    else:
        output = r.choice(["R", "P", "S"])
        myLastMoves.append(output)

elif input == 'R':
    rockCount += 1
    if r.random() > 0.85 or len(myLastMoves) == 0:
        output = r.choice(['P','R','S'])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "R":
        output = r.choice(["P","S"])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "P":
        output = r.choice(["R","S"])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "S":
        output = r.choice(["R","P"])
        myLastMoves.append(output)
    else:
        output = r.choice(["R", "P", "S"])
        myLastMoves.append(output)
        
elif input == 'S':
    scissorCount += 1
    if r.random() > 0.85 or len(myLastMoves) == 0:
        output = r.choice(['P','R','S'])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "R":
        output = r.choice(["P","S"])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "P":
        output = r.choice(["R","S"])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "S":
        output = r.choice(["R","P"])
        myLastMoves.append(output)
    else:
        output = r.choice(["R", "P", "S"])
        myLastMoves.append(output)