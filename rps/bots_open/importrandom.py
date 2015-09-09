import random
if input == "": # initialize variables for the first round
	rockCount = paperCount = scissorsCount = count = 0
        rpsList = []
        last2 = []
elif input == "R":
	rockCount += 1
        rpsList.append("R")
        if len(last2) < 2:
            last2.append("R")
        else:
            last2.remove(last2[0])
            last2.append("R")
elif input == "P":
	paperCount += 1
        rpsList.append("P")
        if len(last2) < 2:
            last2.append("P")
        else:
            last2.remove(last2[0])
            last2.append("P")
elif input == "S":
	scissorsCount += 1
        rpsList.append("S")
        if len(last2) < 2:
            last2.append("S")
        else:
            last2.remove(last2[0])
            last2.append("S")

if count < 10:
        output = random.choice(["R","P","S"])
elif count % 10 == 0:
        output = random.choice(["R","P","S"])      

elif count >10:
        list3 = []
        for i in range(len(rpsList)):
            if rpsList[i] == last2[0]:
                list3.append(i)

        list4 = list3
        for i in range(len(list3)):
            num = list3[i]
            list4[i] = num + 1

        list5 = []
        for i in range(len(rpsList)):
            if last2[1] == rpsList[i]:
                list5.append(i)

        list6 = []
        for i in range(len(list4)):
            for j in range(len(list5)):
                if list4[i] == list5[j]:
                    list6.append(list4[i])

        list7 = []
        for i in range(len(list6)):
            num = list6[i] + 1
            list7.append(num)
        list7.remove(list7[len(list7) - 1])

        list8 = []
        for i in range(len(list7)):
            list8.append(rpsList[list7[i]])
    
        rock = list8.count("R")  
        paper = list8.count("P")  
        scissor = list8.count("S")    

        rockNotLose = rock + scissor
        paperNotLose = paper + rock
        scissorNotLose = scissor + paper
    
        if rockNotLose > paperNotLose and rockNotLose > scissorNotLose:
            output = "R"
        elif paperNotLose > rockNotLose and paperNotLose > scissorNotLose:
            output = "P"
        elif scissorNotLose > paperNotLose and scissorNotLose > rockNotLose:
            output = "S"      
         
        elif rockCount > paperCount and rockCount > scissorsCount:
            output = "P" # paper beats rock
        elif paperCount > scissorsCount:
	    output = "S" # scissors beats paper
        else:
	    output = "R" # rock beats scissors