import os
import sys
import subprocess
import random

key = str(sys.argv[1])
outfileLocation = sys.argv[2] #Output in keyMaker.xml
email = sys.argv[3].replace("__at__","@")#.split("@")[0]

analysis = open("/home/learn2mine/Exam 1/Analysis.txt", "r")
lines = analysis.readlines()
analysis.close()
for i in range(len(lines)):
	line = lines[i].split('\r\n')[0].split(' ')	#remove the trailing \r\n of each line, then split by space
	if [] in lines:					
		lines.remove([])  			#Removes [] left behind by trailing \r\n, if it exists
	while line.count('') > 0:			#get rid of all of the empty strings
		line.remove('')
	lines[i] = line					

#At this point we have a list of lists, with each inner list containing the separated fields of each line.
for i in range(len(lines[1])):				#For each position in line...
	for j in range(100):				#100 times...
		num1 = random.randint(0,199)		#we want to take 2 random lines (There are 200 total 
		num2 = random.randint(0,199)		#   lines)
		line1 = lines[num1]
		line2 = lines[num2]
		holder = line1[i]
		line1[i] = line2[i]			#and switch their values, thus mixing data within columns
		line2[i] = holder			#    randomly
		lines[num2] = line2
		lines[num1] = line1
#print(lines)

for i in range(len(lines)):				#Returning it from whence it came
	lines[i] = "     ".join(lines[i]) + "\r\n"

os.chdir("../../../../tools/myTools/advancedR")

os.system("mkdir -p "+email)
#subprocess.call("mkdir"+email)

userFile = open(email+"/Analysis.txt","w")
userFile.writelines(lines)
userFile.close()

os.chdir(email)

outfile = open(outfileLocation, "w")
outfile.writelines(lines)
outfile.close()

subprocess.call("Rscript '/home/learn2mine/Exam 1/masteryStandardRLesson.R'", shell=True)
subprocess.call("Rscript '/home/learn2mine/Exam 1/masteryFileRLesson.R'", shell=True)
subprocess.call("Rscript '/home/learn2mine/Exam 1/masteryUnknownValuesRLesson.R'", shell=True)
subprocess.call("Rscript '/home/learn2mine/Exam 1/masteryPredictionRLesson.R'", shell=True)


