#Maaaan
# -*- coding: utf-8 -*-
'''
Created on Mon Mar 30 12:14:26 2015

@author: Dave
'''

import random as r

if input == "":
    rockCount = paperCount = scissorCount = 0
    beats = {'R':'S','S':'P','P':'R'}
    cedes = {'R':'P','P':'S','S':'R'}
    lastMoves = []

elif input == 'P':
    paperCount += 1
elif input == 'R':
    rockCount += 1
elif input == 'S':
    scissorCount += 1

    
if r.random() > 0.85:
    output = r.choice(['P','R','S'])
    lastMoves.append(output)
elif lastMoves[-1] == "R":
    output = r.choice(["P","S"])
    lastMoves.append(output)
elif lastMoves[-1] == "P":
    output = r.choice(["R","S"])
    lastMoves.append(output)
elif lastMoves[-1] == "S":
    output = r.choice(["R","P"])
    lastMoves.append(output)
else:
    output = r.choice(["R", "P", "S"])
    lastMoves.append(output)