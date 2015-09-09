#StringerBell

import random as r

if input == "":
        myLastMoves = []
        rockCount = paperCount = scissorCount = 0
        output = r.choice(['R','P','S]')
        myLastMoves.append(output)

elif (rockCount == 0 and paperCount == 0):
        output = 'R'
        myLastMoves.append(output)

elif (rockCount == 0 and scissorCount == 0):
        output = 'S'
        myLastMoves.append(output)

elif (scissorCount == 0 and paperCount == 0):
        output = 'P'
        myLastMoves.append(output)

elif input == 'P':
        paperCount += 1
        if (r.random() > 0.85 or len(myLastMoves) == 0):
                output = r.choice(['R','P','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'R':
                output = r.choice(['P','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'P':
                output = r.choice(['R','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'S':
                output = r.choice(['R','P'])
                myLastMoves.append(output)

elif input == 'R':
        rockCount += 1
        if (r.random() > 0.85 or len(myLastMoves) == 0):
                output = r.choice(['R','P','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'R':
                output = r.choice(['P','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'P':
                output = r.choice(['R','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'S':
                output = r.choice(['R','P'])
                myLastMoves.append(output)
elif input == 'S':
        scissorCount += 1
        if (r.random() > 0.85 or len(myLastMoves) == 0):
                output = r.choice(['R','P','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'R':
                output = r.choice(['P','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'P':
                output = r.choice(['R','S'])
                myLastMoves.append(output)
        elif myLastMoves == 'S':
                output = r.choice(['R','P'])
                myLastMoves.append(output)
else:
        output = r.choice(['R','P','S'])
        myLastMoves.append(output)