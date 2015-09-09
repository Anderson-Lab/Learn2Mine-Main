#chewbacca

import random


#input = "R"
#history = ["R","S","P","R","S","S"]
next_move = {"R":0,"S":0,"P":0}
#my_history = []

if input == "":
    history = []
    my_history = []
else:
    history.insert(0,input)
    
if len(history) < 4:
    output = random.choice(["R","S","P"])
else:
    x = 4
    while(x>0):
	min_history = history[0:x]
	for i in range(1,50):
	    next_move["R"] = next_move["P"] = next_move["S"] = 0
	    match = 0
	    for j in range(i,x):
		if min_history[j] == history[i]:
		    match += 1
	    if match == x:
		next_move[history[i]] += 1
		i = 50
		break
	x -= 1

if next_move["R"] >= next_move["P"] and next_move["R"] >= next_move["S"]:
    output = "P"
elif next_move["P"] >= next_move["S"]:
    output = "S"
else:
    output = "R"
    
#print output
my_history.insert(0,output)
