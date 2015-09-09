#smartDefense
def defeatMove(obj):
	if obj == 'R':
		return 'P'
	elif obj == 'P':
		return 'S'
	else:
		return 'R'

def lostLastMatche(myMove, oponentMove):
	if myMove == defeatMove(oponentMove):
		return False
	else:
		return True	

def mostPlayed(dic):
	if dic['R'] > dic['P'] and dic['R'] > dic['S']:
		return 'R'
	elif dic['P'] > dic['S']:
		return 'P'
	else:
		return 'S'


if input == '':
	oponent = {'R': 0, 'P': 0, 'S': 0}
	my = {'R': 0, 'P': 0, 'S': 0}

	consecutiveDefeats = 0
	oponentHistory = []
	myHistoriy = ['R']
	output = mylastMove = 'R'
else:
	oponent[input] += 1
	oponentHistory.append(input)
	myHistoriy.append(input)
	
	if lostLastMatche(mylastMove, input):
		consecutiveDefeats += 1
	else:
		consecutiveDefeats = 0

	if consecutiveDefeats > 2:
		oponentMostPlayed = mostPlayed(oponent)
		move = defeatMove(oponentMostPlayed)
	else:
		myMostPlayed = mostPlayed(my)
		move = defeatMove(myMostPlayed)

	my[move] += 1
	output = mylastMove = move