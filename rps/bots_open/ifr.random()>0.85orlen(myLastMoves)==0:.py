if r.random() > 0.85 or len(myLastMoves) == 0:
        output = r.choice(['P','R','S'])
        myLastMoves.append(output)
    elif myLastMoves[-1] == "R" and r.random < 0.50:
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