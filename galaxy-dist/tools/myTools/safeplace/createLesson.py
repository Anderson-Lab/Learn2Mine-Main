### Script to automate new lesson creationi
import subprocess

print("--- Automatic Lesson Creator for Galaxy ---")
print("Please provide the following information about your lesson")
moveOn = False
while(not moveOn):
	acceptable = False
	while(not acceptable):
		whichTest = raw_input("Give a 1-word lesson identifier (ex: scaleFilter): ")
		if whichTest.find(" ") < 0:
			acceptable = True
		else:
			print("Unacceptable input, please choose an identifier with no spaces")

	lessonTitle = raw_input("Formal title for the Lesson (ex: Scale and Filtering Lesson): ")
	answerFile = raw_input("Solution file for the lesson (ex: scaleFilterSolution.txt; solution file should be placed in tools/myTools/): ")
	badgeTitle = raw_input("Title of the badge (ex: Scale and Filter Mastery Badge): ")
	badgeDescription = raw_input("Give a description of the badge (ex: For Successfully Filtering a Dataset): ")
	tags = raw_input("Tags for the badge, space separated (ex: scale filter mastery learn2mine): ")
	tags = tags.split()

	print("\n\n--------------------------------------")
	print("Identifier: " + whichTest)
	print("Lesson Title: " + lessonTitle)
        print("Solution File: " + answerFile)
	print("Badge Title: " + badgeTitle)
	print("Badge Description: " + badgeDescription)
	print("Badge Tags: " + str(tags))
	print("--------------------------------------")

	confirm = raw_input("Is the above acceptable? (Y/N): ")
	if confirm.lower() == 'y':
		moveOn = True


#Add the lesson to the submitData.xml file
submitDataFile = open("submitData.xml", "r")
submitDataText = submitDataFile.read()
submitDataFile.close()

submitDataText = submitDataText.replace('<!--FLAG-->','<option value="'+whichTest+'">'+lessonTitle+'</option>\n\t<!--FLAG-->')

submitDataFile = open("submitData.xml", "w")
submitDataFile.write(submitDataText)
submitDataFile.close()


#Add the json file for the badge
badgeText = '{\n   "name": "'+badgeTitle+'",\n   "description": "'+badgeDescription+'",\n   "image": "http://learn2mine.appspot.com/images/'+whichTest+'Mastery.png",\n   "criteria": "http://learn2mine.appspot.com/Home",\n   "tags": '+str(tags)+',\n   "issuer": "http://learn2mine.appspot.com/badges/organization.json"\n}'
badgeJSON = open("../../static/badges/auth/"+whichTest+"Mastery.json","w")
badgeJSON.write(badgeText)
badgeJSON.close()


#Add the whichTest and the title to the html printouts
submitFile = open("submitData.py", "r")
submitText = submitFile.read()
submitFile.close()

submitText = submitText.replace('}#FLAG', ', "'+whichTest+'":"'+lessonTitle+'"}#FLAG1')

submitFile = open("submitData.py", "w")
submitFile.write(submitText)
submitFile.close()


# Add grader for the lesson
graderFile = open("grader.py", "r")
graderText = graderFile.read()
graderFile.close()

graderText = graderText.replace("#FLAG1", "elif whichType == '"+whichTest+"':\n\t\tret = score"+whichTest+"(results)\n\t#FLAG1")
graderText = graderText.replace("#FLAG2", "def score"+whichTest+"(results):\n\treturn numberedGrader(results,'/usr/local/galaxy-learn2mine/tools/myTools/"+answerFile+"')\n#FLAG2")

graderFile = open("grader.py", "w")
graderFile.write(graderText)
graderFile.close()

## Restart Galaxy
subprocess.call("/etc/init.d/galaxy restart", shell=True)
print("\n\nCongratulations! The Lesson has been successfully set up in Galaxy. Make sure Learn2Mine has the appropriate badge image file.")
