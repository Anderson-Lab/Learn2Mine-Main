# test01
solutions = {'R':'P', 'P':'S', 'S':'R'}

if input == "": # initialize variables for the first round
    rockCount = paperCount = scissorsCount = 0
elif input == "R":
    rockCount += 1
elif input == "P":
    paperCount += 1
elif input == "S":
    scissorsCount += 1
    
if rockCount > paperCount and rockCount > scissorsCount:
    output = solutions['P']
elif paperCount > rockCount and paperCount > scissorsCount:
    output = solutions['S']
elif scissorsCount > rockCount and scissorsCount > paperCount:
    output = solutions['R']
else:
    if(input != ""):
        output = solutions[input]
    else:
        output = "R"