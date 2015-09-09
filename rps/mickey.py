#mickey
import random

next_move={'R':0,'P':0,'S':0}

if input == ""
    history = []
    my_history = []
else:
    history.insert(0,input)

size = len(history)
if len(history) > 30
    size = 30
    
if len(history) > 4:
    x = 4
    match = 0
    while(x>0):
	min_history = history[0:x]
	next_move['R'] = next_move['P'] = next_move['S'] = 0
	for i in range(1,size-1):
	    if min_history == history[i:i+x]:
		next_move[history[i-1]] += 1
		match += 1		
	x = x-1
	
    if next_move['R'] >= next_move['P'] and next_move['R'] >= next_move['S']:
	output = 'P'
    elif next_move['P'] >= next_move['S']:
	output = 'S'
    else:
	output = 'R' # rock beats scissors
else:
    output = random.choice(['R','S','P'])

my_history.insert(0,output)