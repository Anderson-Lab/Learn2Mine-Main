import urllib, urllib2, httplib, httplib2 #import requests
import sys
import shutil
import optparse
import tempfile
import os
import json
import time
import subprocess
import difflib

# usage: $html_file' '$other'

# fix the strings in argv
replaceList = ['__at__','__cr__','__cn__','__ob__','__cb__','__dq__','__sq__','__as__','__ds__','__oc__','__cc__','__lt__','__gt__','__pd__','__fs__','__bs__','__ti__','__pe__','__sc__','__vb__']
replaceWithList = ['@','\r','\n','[',']','"',"'",'&','$','{','}','<','>','#','/','\\','~','%',';','|']
for j in range(len(sys.argv)):
	results = sys.argv[j]
	for i in range(len(replaceList)):
		results = results.replace(replaceList[i],replaceWithList[i])
	sys.argv[j] = results

htmlfile = sys.argv[1]
other = json.loads(sys.argv[2])
initCode = other['initializationCode']
finalCode = other['finalizationCode']
insCode = other['instructorCode']
language = other['language']
badgeName = other['badgeName']
stuCode = other['studentCode']
email = other['email']

def create_file(initCode,middleCode,finalCode,language,outfile):
	# Create the student file
	f = open(outfile,"w")
	f.write(initCode)

	f.write("\n")

	f.write(middleCode)

	f.write("\n")

	f.write(finalCode)
	f.close()

create_file(initCode,stuCode,finalCode,language,"student.file")
create_file(initCode,insCode,finalCode,language,"instructor.file")

results = {}
if language == "python27":
<<<<<<< HEAD
<<<<<<< HEAD
	interp = "python3"
elif language == "python3":
	interp = "python3"
elif language == "R" or language == "rcode":
	interp = "Rscript"
else:
	interp = "python3"
=======
=======
>>>>>>> 034f204a2d2fb838e5942ba7e343a1f9dce37236
	interp = "python"
elif language == "R" or language == "rcode":
	interp = "Rscript"
else:
	interp = "python"
<<<<<<< HEAD
>>>>>>> d71c44a842626df743ea929fc1632bede20c7284
=======
>>>>>>> 034f204a2d2fb838e5942ba7e343a1f9dce37236

cmd = [interp,"student.file"]
print " ".join(cmd)
process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
student_stdout, student_stderr = process.communicate()

cmd = [interp,"instructor.file"]
process = subprocess.Popen( cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
instructor_stdout, instructor_stderr = process.communicate()

if student_stdout == instructor_stdout:
	results['return'] = "correct"
else:
	results['return'] = "incorrect"
	
results['student_stdout'] = student_stdout
results['instructor_stdout'] = instructor_stdout
d = difflib.Differ()
diff = d.compare(student_stdout.split("\n"), instructor_stdout.split("\n"))
results['difference_stdout'] = '\n'.join(diff)
results['email'] = email
results['badge_image_url'] = 'None'
badgeName = badgeName.strip()
results['badgeName'] = badgeName

# Now check to see if there is a badge necessary
if "partial" not in badgeName and badgeName != "None" and badgeName != "" and badgeName != None and results['return'] == "correct": 
	badgeImageURL = "http://learn2mine.appspot.com/images/"+badgeName+"Mastery.png"
	results['badge_image_url'] = badgeImageURL
	badge = '{\n   "uid":"'+email+'",\n   "recipient": {\n      "type":"email",\n      "hashed": false,\n      "identity": "'+email+'"\n   },\n   "image":"'+badgeImageURL+'",\n   "badge":"http://portal.cs.cofc.edu/learn2mine/static/badges/auth/'+badgeName+'Mastery.json",\n   "issuedOn":'+str(int(time.time()))+',\n   "verify": {\n      "type":"hosted",\n      "url": "http://portal.cs.cofc.edu/learn2mine/static/badges/'+email.split("@")[0]+badgeName+'Mastery.json"\n   }\n}'
	outfile = open('../../../../static/badges/'+email.split("@")[0]+badgeName+'Mastery.json', 'w')
	outfile.write(badge)
	outfile.close()

	# Award the badge
	learn2mine = "http://learn2mine.appspot.com"
	#learn2mine = "http://localhost:8080"
	h = httplib2.Http()
	resp, content = h.request(learn2mine+"/Grade", "POST", urllib.urlencode(results))

#create html output file and write to it
outfile = open(htmlfile, 'w')
outfile.write(json.dumps(results))
outfile.close()

print json.dumps(results, sort_keys=True,indent=4, separators=(',', ': '))
f = open("student.file",'r')
print f.read()
f.close()
