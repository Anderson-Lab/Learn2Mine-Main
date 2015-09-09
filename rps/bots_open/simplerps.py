#simplerps
def defeatMove(obj):
	if obj == 'R':
		return 'P'
	elif obj == 'P':
		return 'S'
	else:
		return 'R'

def mostPlayed(dic):
	if dic['R'] > dic['P'] and dic['R'] > dic['S']:
		return 'R'
	elif dic['P'] > dic['S']:
		return 'P'
	else:
		return 'S'

if input == '':
	oponentMoves = {'R': 0, 'P': 0, 'S': 0}
	myMoves = {'R': 0, 'P': 0, 'S': 0}
	output = 'R'
else:
	# 1 calculate my most frequent move
	# 2 assume that the oponent would try to defeat this move
	# 3 defeat this move
	myMostPlayed = mostPlayed(myMoves)
	move = defeatMove(defeatMove(myMostPlayed))

	oponentMoves[input] += 1
	myMoves[move] += 1
	output = move