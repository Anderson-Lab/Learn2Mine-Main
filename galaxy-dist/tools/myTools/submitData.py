import urllib, urllib2, httplib, httplib2 #import requests
import sys
import shutil
import optparse
import tempfile
import os
import json
import grader
import time
from galaxy.util.json import *

results = sys.argv[1]
lesson = sys.argv[2]
#keyfile = sys.argv[7]
email = sys.argv[7]
globalLoc = '/usr/local/galaxy-learn2mine/galaxy-dist/' # For use on deployed Galaxy
#globalLoc = '/home/jldierks/Desktop/learn2mine-main/galaxy-dist/' # For use on local Galaxy

# NOTE: not sure about the __cn__ one...
replaceList = ['__at__','__cr__','__cn__','__ob__','__cb__','__dq__','__sq__','__as__','__ds__']
replaceWithList = ['@','\r','\n','[',']','"',"'",'&','$']

#argv[8] is the textarea input
if sys.argv[8].strip() != '':
	results = sys.argv[8]
	for i in range(len(replaceList)):
		results = results.replace(replaceList[i],replaceWithList[i])
#Otherwise results stored in csv file, read that file
else:
	infile = open(results, "r")
	results = infile.read().strip()
	infile.close()

#split by newline character
results = results.split("\n")

#Galaxy puts quotes around each item, remove those
#for i in range(len(results)):
#	results[i] = results[i].replace('"', '')

############################################
####   FORMATTING DATA FOR TRANSFER	####
############################################
learn2mine = "http://learn2mine.appspot.com"
#learn2mine = "http://localhost:8080"

score, status, feedback = grader.mainGrader(lesson, results, email)
#data = {"key":key, "score":score, "status": status, "type":lesson}
data = {"email":email, "score":score, "status": status, "type":lesson}

#If they master the lesson, create the appropriate badge file
if(status == 'mastered'):
	badge = '{\n   "uid":"'+email+'",\n   "recipient": {\n      "type":"email",\n      "hashed": false,\n      "identity": "'+email+'"\n   },\n   "image":"http://learn2mine.appspot.com/images/'+lesson+'Mastery.png",\n   "badge":"http://portal.cs.cofc.edu/learn2mine/static/badges/auth/'+lesson+'Mastery.json",\n   "issuedOn":'+str(int(time.time()))+',\n   "verify": {\n      "type":"hosted",\n      "url": "http://portal.cs.cofc.edu/learn2mine/static/badges/'+email.split("@")[0]+lesson+'Mastery.json"\n   }\n}'
	outfile = open(globalLoc+'static/badges/'+email.split("@")[0]+lesson+'Mastery.json', 'w')
	outfile.write(badge)
	outfile.close()
elif(status == 'learned'):
	badge = '{\n   "uid":"'+email+'",\n   "recipient": {\n      "type":"email",\n      "hashed": false,\n      "identity": "'+email+'"\n   },\n   "image":"http://learn2mine.appspot.com/images/'+lesson+'Learned.png",\n   "badge":"http://portal.cs.cofc.edu/learn2mine/static/badges/auth/'+lesson+'Learned.json",\n   "issuedOn":'+str(int(time.time()))+',\n   "verify": {\n      "type":"hosted",\n      "url": "http://portal.cs.cofc.edu/learn2mine/static/badges/'+email.split("@")[0]+lesson+'Mastery.json"\n   }\n}'
	outfile = open(globalLoc+'static/badges/'+email.split("@")[0]+lesson+'Learned.json', 'w')
	outfile.write(badge)
	outfile.close()

#Print main results to galaxy history
print("{"+"Status: "+ status+"}")
print("{"+"Score: " + str(score)+"}")
#print("{"+"Key: " + str(key)+"}")
print("{"+"Email: " + str(email)+"}")

h = httplib2.Http()
#data = dict(name="Joe", comment="A test comment")
resp, content = h.request(learn2mine+"/Grade", "POST", urllib.urlencode(data))


################################
#####     HTML OUTPUT      #####
################################
#Define flags for python call from the xml
op = optparse.OptionParser()
op.add_option('-o', '--htmloutput', default=None)
op.add_option('-d', '--outputdir', default="/tmp/shortread")
op.add_option('-z', '--csvoutput', default=None)
opts, args = op.parse_args()
if not os.path.exists(opts.outputdir): 
	os.makedirs(opts.outputdir)


lessonDict = {"functions":"R Functions Lesson", "loops":"Loops Lesson","conditionals":"R Conditionals Lesson","RFileIO":"R File I/O Lesson", "basicR":"Basic R Lesson", "uploading":"Uploading Data","knn":"K-Nearest Neighbor","kmeans":"K Means Clustering", "scaleFilter":"Scale and Filter","pca":"Principal Component Analysis", "pls": "Partial Least Squares Regression", "nn": "Neural Networks","mb":"Market Basket Analysis", "algae": "Case Study 1: Algae", "stock":"Case Study 2: Stocks", "fraud":"Case Study 3: Fraud", "RMissingValue":"R Missing Values","RPrediction1":"R Prediction Lesson 1","RPrediction2":"R Prediction Lesson 2","advancedStandard":"Advanced Standard R Lesson","advancedFile":"Advanced File I/O Lesson","advancedUnknown":"Advanced Unknown Values Lesson", "advancedPrediction":"Advanced R Prediction Lesson", "test2":"This is the second Test", "stock1":"Stock Market Case Study","evaluation":"Evaluation Criteria Functions","simulatedTrader":"Stock Market Simulated Trader", "basicRTutorial":"Basic R Tutorial","fileIOTutorial":"File IO Tutorial","loopsConditionalsTutorial":"Loops and Conditionals Tutorial","knnRTutorial":"knn In R Tutorial","knnToolTutorial":"knn Tool Tutorial", "dataMining":"Data Mining General Lesson","classification":"Classification Lesson","bayes":"General Bayes Lesson","empiricalNB":"Empirical Naive Bayes Lesson","testSet":"Test Set Cross Validation Lesson","leaveOneOut":"Leave One Out Cross Validation Lesson","kFold":"k-Fold Cross Validation Lesson","crossValidation":"Cross Validation General Lesson","search":"Search Lesson","bfs":"BFS Lesson","dfs":"DFS Lesson","ai":"Artificial Intelligence Lesson","ucs":"UCS Lesson","decisionTree":"Decision Tree Lesson", "hierarchicalClustering":"Hierarchical Clustering Lesson","knapsack":"Knapsack Problem Lesson","kmeansClustering":"kmeansClustering"}#FLAG11>>>>>>> a703cb1a13de320773b430674b47ee731c17ba3b

#HTML Output for lesson
res = ['<!DOCTYPE HTML><html><head></head><body><h1>Submission to Learn2Mine</h1><p><b>Lesson Submitted: </b>'+ lessonDict[lesson] +'<br /><b>Status: </b>']
if resp.status == 200:
	#res.append('Successful Submission!<br/><b>Key: </b>'+str(key)+'<br /><br /><b>Lesson Progress:</b>')
	res.append('Answers Evaluated<br/><b>User: </b>'+str(email)+'<br /><br /><b>Lesson Progress:</b>')
	if status == 'learned':
		res.append('Learned. You have successfully completed the lesson and earned the following badge:<br><br><a href="http://learn2mine.appspot.com/Home"><img src=http://learn2mine.appspot.com/images/'+lesson+'Learned.png /></a><br><br>Head to your Learn2Mine home page to claim this badge with your Mozilla OpenBadges account!<br>')
	elif status == 'mastered':
		res.append('Mastered! You have successfully completed the lesson and earned the following badge:<br><br><a href="http://learn2mine.appspot.com/Home"><img src=http://learn2mine.appspot.com/images/'+lesson+'Mastery.png /></a><br><br>Head to your Learn2Mine home page to claim this badge with your Mozilla OpenBadges account!<br>')
	else:
		res.append("Still Needs Work")
	if score != None:
		res.append('<br /><b>Score: </b>' + str(score) +'<br />')
	else:
		res.append('<br/ >This lesson has no associated score<br />')
	res.append(feedback)
else:
	res.append("An error occurred submitting your work to Learn2Mine. Please try again. If the problem persists, contact us!")
	res.append("\n<b>Response Status:</b> "+str(resp.status))

#close the html body tag
res.append('</body>')
#create html output file and write to it
outfile = open(opts.htmloutput, 'w')
outfile.write(''.join(res))
outfile.close()


