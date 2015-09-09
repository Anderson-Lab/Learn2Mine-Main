# ThisIsBRA2

import random

beat = {'R':'P', 'P':'S', 'S':'R'}
moves = ['R', 'P', 'S']

def mostPlayed(dic):
	if dic['R'] > dic['S'] and dic['R'] > dic['P']:
		return 'R'
	elif dic['S'] > dic['P']:
		return 'S'
	else:
		return 'P'

if(input == ""):
	myMoves = {'R':0, 'P':0, 'S':0}
	output = myLastMove = random.choice(moves)
else:
	myMoves[myLastMove] += 1
	mostPlayedMove = mostPlayed(myMoves)
	output = myLastMove = beat[beat[mostPlayedMove]]