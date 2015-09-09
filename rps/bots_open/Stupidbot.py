#Stupid bot
import random as r

print 'last move = ', lastMove

if lastMove == "R":
    output = r.choice(["P","S"])
elif lastMove == "P":
    output = r.choice(["R","S"])
elif lastMove == "S":
    output = r.choice(["R","P"])
else:
    output = r.choice(["R", "P", "S"])

print 'output = ', output

lastMove = output