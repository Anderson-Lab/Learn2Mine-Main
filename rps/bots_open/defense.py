#defense
def defeatOption(obj):
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
	oponent = {'R': 0, 'P': 0, 'S': 0}
	my = {'R': 0, 'P': 0, 'S': 0}

	oponentHistory = []
	myHistoriy = ['R']
	randomize = False
	output = 'R'
else:
	oponent[input] += 1
	oponentHistory.append(input)
	myHistoriy.append(input)
	
	myMostPlayed = mostPlayed(my)
	move = defeatOption(myMostPlayed)
	 
	my[move] += 1
	output = move