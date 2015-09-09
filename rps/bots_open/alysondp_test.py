#alysondp_test
import random

beat={'R':'P','P':'R','S':'P'}
next_move={'R':0,'P':0,'S':0}

if input == "": # initialize variables for the first round
    rockCount = paperCount = scissorsCount = 0
    history = []
    my_history = []
elif input == "R":
    rockCount += 1
elif input == "P":
    paperCount += 1
elif input == "S":
    scissorsCount += 1

if input != "":
    history.insert(0,input)
    '''
    print "ME : ", my_history
    print "CPU: ", history
    if len(my_history)>0:
	if my_history[0] == history[0]:
	    print "TIE"
	elif beat[my_history[0]] == history[0]:
	    print "WIN"
	else:
	    print "LOSE"
    '''
    
if len(history) > 4:
    x = 4
    if len(history) > 100:
        history = history[0:99]
    while(x>0):
	min_history = history[0:x]
	#print "History: ",history
	#print "Min_History: ", min_history
	next_move['R'] = next_move['P'] = next_move['S'] = 0
	#print next_move
	for i in range(1,len(history)-x):
	    if min_history == history[i:i+x]:
		next_move[history[i-1]] += 1
		match += 1
		#print "MATCH:", min_history, "NEXT:", history[i-1]			
	x = x-1
	
    if next_move['R'] > next_move['P'] and next_move['R'] > next_move['S']:
	output = 'P' # paper beats rock
    elif next_move['P'] > next_move['S']:
	output = 'S' # scissors beats paper
    else:
	output = 'R' # rock beats scissors
    #print "output history:",output, " ",next_move
else:
    output = random.choice(['R','S','P'])
    #print "output random:",output

my_history.insert(0,output)
#print "######################################################################"
#print history
#print "rock:", rockCount, " paper:", paperCount, " scissors:", scissorsCount
'''
if rockCount > paperCount and rockCount > scissorsCount:
	output = "P" # paper beats rock
elif paperCount > scissorsCount:
	output = "S" # scissors beats paper
else:
	output = "R" # rock beats scissors
'''