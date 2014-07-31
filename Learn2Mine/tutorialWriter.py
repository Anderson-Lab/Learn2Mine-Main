# coding: utf-8
def createTutorialProbs(hint,code,id=0):
	hintHTML = '<div id="hint'+str(id)+'" style="display:none;"><b>Hint:</b> '+hint+'</div><a id="hint'+str(id)+'link" href="javascript:;" onClick="document.getElementById(\'hint'+str(id)+'\').style.display=\'inline\'; document.getElementById(\'hint'+str(id)+'link\').style.display=\'none\';">Hint</a>'
	showlineHTML = ''
	codelist = code.split('<br>')
	for i in range(len(codelist)): # Creates the show line divs
		showlineHTML += '<div class="linecode'+str(id)+'" id="showline'+str(i)+str(id)+'" style="display:none;">'+codelist[i]+'</div>'
	for i in range(len(codelist)):
		if(i == 0):
			showlineHTML += '<a class="linelink'+str(id)+'" id="showline'+str(id)+'link" href="javascript:;" onClick="$(\'#showline'+str(i)+str(id)+'\').css(\'display\',\'block\'); $(\'#showline'+str(id)+'link\').css(\'display\',\'none\'); $(\'#showline'+str(id)+'link'+str(i+1)+'\').css(\'display\',\'block\');">Show Line of Code</a>'
		elif(i == len(codelist) - 1):
			showlineHTML += '<a class="linelink'+str(id)+'" style="display:none;" id="showline'+str(id)+'link'+str(i)+'" href="javascript:;" onClick="$(\'#showline'+str(i)+str(id)+'\').css(\'display\',\'block\'); $(\'#showline'+str(id)+'link'+str(i)+'\').css(\'display\',\'none\');">Show Last Line of Code</a>'
		else:
			showlineHTML += '<a class="linelink'+str(id)+'" style="display:none;" id="showline'+str(id)+'link'+str(i)+'" href="javascript:;" onClick="$(\'#showline'+str(i)+str(id)+'\').css(\'display\',\'block\');$(\'#showline'+str(id)+'link'+str(i)+'\').css(\'display\',\'none\'); $(\'#showline'+str(id)+'link'+str(i+1)+'\').css(\'display\',\'block\');">Show Next Line of Code</a>'

	showallHTML = '<p id="answer'+str(id)+'shown" style="display:none;"><b>Full Answer:</b></p><div id="showall'+str(id)+'" style="display:none;">'+code+'</div><a id="showall'+str(id)+'link" href="javascript:;" onClick="$(\'#showall'+str(id)+'\').css(\'display\',\'block\');$(\'.linecode'+str(id)+'\').css(\'display\',\'none\');$(\'.linelink'+str(id)+'\').css(\'display\',\'none\');$(\'#showall'+str(id)+'link\').css(\'display\',\'none\');$(\'#answer'+str(id)+'shown\').css(\'display\',\'inline\');">Show Answer</a>'
	return hintHTML+'<br>'+showlineHTML+'<br>'+showallHTML+'<br>'


def main(page):
	problems="NOT FOUND"
	if page == 'intro':
		header = 'Tutorial'
		paragraph = 'Welcome to the Learn2Mine tutorial, here we will take you through the different components of Learn2Mine and walk you through your first lessons. Learn2Mine is made of 3 main parts: This frontend Google Appengine website, a Galaxy Server, and an Rstudio server. You\'ve seen the website, let\'s take a look at the other 2 components. Click the link below to open the Galaxy server:<br><br> <a target="_blank_" href="http://portal.cs.cofc.edu/learn2mine">Learn2Mine\'s Galaxy</a>'
		next="I've opened Galaxy!"
		nextPage='galaxyLogin'
	elif page == 'galaxyLogin':
		header = 'Logging In to Galaxy'
		paragraph = 'Following that link should have brought you to a page similar to the one you see presented here. Learn2Mine\'s Galaxy requires users to log in in order to begin carrying out tools. Creating an account on Galaxy is simple, just click on the "you may create one link" (boxed in red in the screenshot below). This will bring you to a page where you may input your email address (the one you used for Learn2Mine), your password, and your prefered "Public name"<br><br><div><img src="images/createAccount.png" target="_blank" width="450px" float="left"/><img src="images/newUser.png" width="450px" target="_blank" style="padding-left:50px" float="left"/></div>'
		next="I've Created my Account!"
		nextPage='galaxy'
	elif page == 'galaxy':
		header = 'Galaxy'
		paragraph = 'This is Galaxy. Here is where you will run your algorithms and submit your work on each lesson for grading. On the left is a list of tool categories, expanding any of those links will provide you with a list of the tools you will available to you for your work in Learn2Mine. Clicking any of thsoe tools will bring up an interface through which you can "Execute" the tool\'s function. For some lessons, these algorithms will be written for you, and you need only select the data and parameters you want to run it with. Other lessons will leave the coding up to you, and ask only for an answer submission in the form of an RStudio output. By creating a Galaxy account, you have automatically been created an RStudio account as well.<div><a href="images/galaxyScreenshot.png"><img src="images/galaxyScreenshot.png" width="600px" target="_blank" float="left"/></a></div><br>The picture above those the following parts of a common Galaxy run:<ol><li><b>The Toolbox:</b> Here you will select the tools you want to run</li><li><b>Current Tool:</b> After selecting a tool, Galaxy will display the necessary inputs, and button to execute here</li><li><b>Metadata:</b> Any necessary information about the tool or it\'s parameters</li><li><b>History:</b> A list of previously run Galaxy jobs and their statuses</li></ol> When you\'re ready, click the link below to see RStudio:<br><br><a target="_blank_" href="http://portal.cs.cofc.edu/learn2mine-rstudio" target="_blank">RStudio</a>'
		next="I've Opened RStudio!"
		nextPage='rstudioLogin'

	elif page == 'rstudioLogin':
		header = 'Exploring RStudio'
		paragraph = 'RStudio is an IDE for writing and running code written in R, a commonly used language for data manipulation. When you register for an account on Galaxy, you are automatically created one for RStudio as well. Your username is simply the prefix of your email, and the password is the same. Click on the following link to access RStudio, and try logging in: <br><a href="http://portal.cs.cofc.edu/learn2mine-rstudio" target="_blank">RStudio</a>'
		next="I've Logged into Rstudio!"
		nextPage="rstudio"
	elif page == 'rstudio':
		header = 'Exploring RStudio'
		paragraph = 'This is Rstudio. Here you will write and run code in R in order to solve some of the problems Learn2Mine poses. Many lessons will require you to copy your output from RStudio, and submit your answer to Learn2Mine using a Galaxy submission tool. Now that you\'ve seen the 3 facets of Learn2Mine and understand how they work, let\'s try a lesson!<div><a href="images/rstudioScreenshot.png" target="_blank"><img src="images/rstudioScreenshot.png" width="600px" float="left"/></a><ol><li><b>Current File:</b> The current file you have open</li><li><b>Console:</b> Here you can run R code directly</li><li><b>Workspace:</b> Shows the currently declared variables available to the console</li><li><b>Directory:</b> Your home directory, you may write, read, or upload files to here.</li></ol></div>'
		next="I'm Ready to Start!"
		nextPage="tutorial1"



	elif page=="tutorial1":
		header='Basic R Tutorial'
		paragraph='The following are 2 example problems similar to the ones you will find within Learn2Mine\'s lessons. Complete them using RStudio, and submit your final answer using Galaxy. Do not be afraid to use the hints or see part of the answer if you get stuck. Note that our answers are not the only way to do these tasks.'
		next='File I/O Tutorial'
		nextPage='tutorial2'


		hint1text = 'Try breaking up each operation and putting them on individual lines - Your code should be 4 lines.'
		code1 = 'x = 1234<br>y = 169837<br>z = x^2 + 13*y/x<br>print(z)'
		problem1code = createTutorialProbs(hint1text,code1,1)

		code2='M = matrix(c(105,56,303,400,96,156),3,2)<br>M[(M>100 & M<200)]'
		hint2text = 'What are the 2 conditions you\'re looking for? Try indexing by those. What boolean operator joins them together?'
		problem2code = createTutorialProbs(hint2text,code2,2)
		problems = '<li>R objects and simple arithmetic: Perform the following analysis using<br>x = 1234 and y = 169837<br>z = x^2 + 13*y/x<br>then type print(z)</li>'+problem1code+'<li>Given the following matrix, M = matrix(c(105,56,303,400,96,156),3,2) Slice out only those values less than 200 and greater than 100 (inclusive) using a logical statement. Print out the results and copy them to the file.</li>'+problem2code

	elif page=="tutorial2":
		header='R File IO Tutorial'
		paragraph='Now it\'s time to learn how to read and manipulate files in R. Perform the following tasks in RStudio with the dataset given. Before reading in the data as each problem says, make sure to change your Rstudio options to 3 digits and a output width of 100'
		next='Loops & Conditionals'
		nextPage='tutorial3'


		hint1text = 'You can read in a dataframe using R\'s read.table() function'
		code1='options(digits = 3,width=100)<br>df <- read.table(\'Analysis.txt\',col.names=c(\'season\',\'size\',\'speed\',\'mxPh\',\'mn02\',\'Cl\',\'no3\',\'nh4\',\'opo4\',\'po4\',\'chla\',\'a1\',\'a2\',\'a3\',\'a4\',\'a5\',\'a6\',\'a7\'))<br> head(df)'
		problem1code = createTutorialProbs(hint1text,code1,1)

		code2='options(digits = 3,width=100)<br>analysis <- readLines(\'Analysis.txt\')<br>head(analysis)'
		hint2text = 'Be sure you\'re calling readLines(). notice how this output is different from the previous one.'
		problem2code = createTutorialProbs(hint2text,code2,2)
		problems = '<li>Read in the <a href="/datasets/Analysis.txt" download="Analysis.txt">Analysis.txt</a> file into a dataframe. Run the head command on your data, and then copy the results into your submission. Read in the following column names (in the order they appear) with the data as well: [\'season\',\'size\',\'speed\',\'mxPh\',\'mn02\',\'Cl\',\'NO3\',\'NH4\',\'oPO4\',\'PO4\',\'Chla\',\'a1\',\'a2\',\'a3\',\'a4\',\'a5\',\'a6\',\'a7\']</li>'+problem1code+'<li>Read the file again, but do so using the readLines command. This will read the file line by line. It is a great function to use if you do not have data structured in a fixed number of rows and columns. Run the head command on the resultof readLines. Copy those results into your submission.</li>'+problem2code

	elif page=="tutorial3":
		header='Loops and Conditionals Tutorial'
		paragraph='This time you\'ll submit code for Galaxy to run and check. You\'ll enter your answers much like before, only this time writing R Code to the submission box. Try out solutions in RStudio until your feel comfortable with your solution, then submit them with the functions names defined below.'
		next='knn R Tutorial'
		nextPage='tutorial4'


		hint1text = 'Try looping through each value in the array, and adding them one-at-a-time to an aggregator variable. What type of loop should you use for this?'
		code1='my.sum <- function(my.array) {<br>&nbsp;&nbsp;&nbsp;  total = 0<br>&nbsp;&nbsp;&nbsp;  for (i in 1:length(my.array)) {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;total = total + my.array[i]<br>&nbsp;&nbsp;&nbsp;  }<br>&nbsp;&nbsp;&nbsp;  return(total)<br>}'
		problem1code = createTutorialProbs(hint1text,code1,1)

		code2='minimum3 <- function(v1,v2,v3) {<br>&nbsp;&nbsp;&nbsp;smallest = v1<br>&nbsp;&nbsp;&nbsp;if (v2 < smallest)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;smallest = v2<br>&nbsp;&nbsp;&nbsp;if (v3 < smallest)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;smallest = v3<br>&nbsp;&nbsp;&nbsp;return(smallest)<br>}'
		hint2text = 'Don\'t try to compare all 3 variables at once, try using 2 if statements to make your decision on which is the smallest'
		problem2code = createTutorialProbs(hint2text,code2,2)
		problems = '<li> Write a function that loops through the values of an array and returns the sum of the values using a <b>for</b> loop. <b>You may not use the built in sum function.</b> Here is the function definition. You must fill in the middle. Instead of submitting the answer submit the working code.<br><br>my.sum &lt;- function(my.array) {<br>    &lt;insert code here><br>}<br></li>'+problem1code+'<li>Write a function that returns the minimum of three numbers. Here is the function definition. You may not use the <b>min</b> function. You must fill in the middle. Instead of submitting the answer submit the working code.<br><br>minimum3 &lt;- function(v1,v2,v3) {<br> &lt;insert code here><br>}<br></li>'+problem2code

	elif page=="tutorial4":
		header='k-NN R Tutorial'
		paragraph='Let\'s tackle our first major algorithm used in datascience: The k-nearest neighbor algorthm.<br><br> Try writing your own algorithm to perform an operation like this in R. If you want to learn more about the k-NN algorithm and how it works, take a look at our <a href="http://learn2mine.appspot.com/Lessons?lesson=knn1" target="_blank">k-NN explanation</a>.'
		next='kNN Tool Lesson'
		nextPage='knn'


		hint1text = 'It may be helpful to write a function inside your my.knn function that can compute euclidean distances. It also may be helpful to write the function to work very specifically with this dataset (i.e. hard-coding in the test labels to be "yes" or "no" when comparing the nearest neighbors.)'
		code1='my.knn <- function(training, testing, k) {<br>&nbsp;&nbsp;&nbsp;&nbsp;train <- read.table(training,sep=",",header=TRUE)<br>&nbsp;&nbsp;&nbsp;&nbsp;test <- read.table(testing,sep=",",header=TRUE)<br>&nbsp;&nbsp;&nbsp;&nbsp;labels <- as.matrix(train[,ncol(train)])<br>&nbsp;&nbsp;&nbsp;&nbsp;features <- as.matrix(train[,1:(ncol(train)-1)])<br>&nbsp;&nbsp;&nbsp;&nbsp;testFeatures <- as.matrix(test)<br>&nbsp;&nbsp;&nbsp;&nbsp;testLabels <- matrix(nrow=nrow(testFeatures))<br>&nbsp;&nbsp;&nbsp;&nbsp;maxint <- 2147483647<br>&nbsp;&nbsp;&nbsp;&nbsp;dist <- function(x1,x2) {<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;return(sqrt(sum((x1 - x2) ^ 2)))<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;distances <- matrix(nrow=nrow(testFeatures),ncol=nrow(train))<br>&nbsp;&nbsp;&nbsp;&nbsp;for(row in 1:nrow(testFeatures)){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for(otherrow in 1:nrow(features)){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;distances[row,otherrow] <- dist(testFeatures[row,],features[otherrow,])<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;for(label in 1:nrow(testLabels)){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nearestNeighborIndexes <- array(dim=(k))<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nearestNeighborValues <- array(maxint,dim=(k))<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for(comp in 1:ncol(distances)){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;euclidDist <- distances[label,comp]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for(neighbor in 1:k){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(euclidDist < nearestNeighborValues[neighbor]){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nearestNeighborIndexes[neighbor] <- comp<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;nearestNeighborValues[neighbor] <- euclidDist<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;break<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;labelctr <- 0<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;for(i in 1:k){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(toString(labels[nearestNeighborIndexes[i]]) == "yes")<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;labelctr <- labelctr + 1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;if(labelctr > k/2){<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;testLabels[label] <- "yes"<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;else{<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;testLabels[label] <- "no"<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;}<br>&nbsp;&nbsp;&nbsp;&nbsp;return(testLabels)<br>}'
		problem1code = createTutorialProbs(hint1text,code1,1)

		problems = '<li>Write your own knn function called my.knn that takes 3 arguments: a training file, a testing file, and a k value. The function should use the training file to develop a set of euclidean distances in order to find the nearest neighbors for the records (rows) in your testing data file. Finally, you want to return a 1 column matrix which contains the correct labels for the testing data. The nth row in the test labels matrix corresponds to the nth row in the testing dataset. Though your kNN algorithm should be generalizeable to many different datasets, you may use the training and testing datasets we provide for you below in order to test your function.<br><a href="datasets/knnRTutorial/trainingdata.csv">Training Set</a>&nbsp;&nbsp;<a href="datasets/knnRTutorial/testingdata.csv">Testing Set</a><br>my.knn &lt;- function(training, testing, k) {<br>    &lt;insert code here><br>}<br></li>'+problem1code
	elif page=="knn":
		header='KNN Tool'
		paragraph='Now it\'s time to get you started on Learn2Mines tool-based lessons. Here you will use the tools we\'ve provided in galaxy in order to run more complex algorithms we\'ve written for you. Follow the instructions of the tool\'s lesson in order to get your very first Mastery badge of the knn algorithm, and see how Learn2Mine\'s lessons are structured'
		next='knn Lesson'
		nextPage='knnLesson'
	else:
		header = 'Oops!'
		paragraph = 'We could not find the page you are looking for, sorry! Try going back to the start of the tutorial. If the problem persists, contact us!'
		next="Back to Start"
		nextPage="intro"
	return {'heading':header, 'paragraph': paragraph, 'next':next, 'nextPage':nextPage, 'problems':problems}
