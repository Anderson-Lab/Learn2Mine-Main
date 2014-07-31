#from galaxy_api import *


def getLesson(page):
	reminder = 'Enter your code in the box provided if the answer is not correct, the difference between the answer produces by running the correct solution and yours will be shown.'
	if page == "example":

                query = Lesson.query()
                userLessons = query.filter(Lesson.author == thisUser)
                existingLesson = userLessons.filter(Lesson.name == lessonName).fetch(1)



		header="Example"
		paragraph = 'This page is an example of how to format your Data Mining Lessons. Here, you put your explnation of any concepts or important things to remember when doing this lesson.'
		problems = ['The problems wll then go here, in a list. This is problem 1', 'Here is problem 2', "And here's 3"]
	elif page == "DealingWithUnknownValues":
		header="Dealing with Unknown Values"
		paragraph = 'The software will tell you which ones you have completed successfully, and which ones you still need to work on.'
		problems = ['Read in the Analysis.txt file from the book into a dataframe using the headings that are specified in the book. Remove any sample that has 1 or more unknown values. Save the contents to a csv file using the command write.csv with the default options, and then copy the contents of this file into your submission.','How many rows were removed in problem 1?']
	elif page == "BasicR":
		header="Basic R"
		paragraph= 'The software allows you to check your solutions as you progress through the level. In this level, you will be asked to manipulate arrays, factors, vectors, matrices, lists, and data frames in R. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b><p>R has three basic indexing operators, with syntax displayed by the following examples:<br>x[i]<br>x[i, j]<br>x[[i]]<br>x[[i, j]]<br>x$a<br>x$"a"<br>For vectors and matrices the [[ forms are rarely used, although they have some slight semantic differences from the [ form (e.g. it drops any names or dimnames attribute, and that partial matching is used for character indices). When indexing multi-dimensional structures with a single index,x[[i]] or x[i] will return the ith sequential element of x.<br>For lists, one generally uses [[ to select any single element, whereas [ returns a list of the selected elements.<br>The [[ form allows only a single element to be selected using integer or character indices, whereas[ allows indexing by vectors. Note though that for a list, the index can be a vector and each element of the vector is applied in turn to the list, the selected component, the selected component of that component, and so on. The result is still a single element.'
		problems = ['Vectors: Write the code that creates a vector/array named <b>v</b> that contains the numbers 1,2,3,...,100.',\
                            'Matrices: Write the code that creates a matrix named <b>M</b> with 10 columns that contains the numbers 1,2,3,...,100 in order.',\
                            'Factors: Write the code that creates a factor with named <b>f</b> with 5 CS students, 3 Data Science students, and 1 CITA student (in that order) using the official abbreviations (CSCI, DATA, and CITA).',\
                            'Slicing or Subsetting: Given the following matrix, M = matrix(c(105,56,303,400,96,156),3,2), create the code that will slice out only those values less than 200 and greater than 100 (inclusive) using a logical statement.',\
                            'Using the same matrix and the <b>which</b> command, create the code that will find the indices, as opposed to the actual values, and store them in a variable called inxs. You can do this by taking the same equality from above (M <= 200 & M >= 100) and then adding the which command (i.e., which(M <= 200 & M >= 100).',\
                            'Given the following matrix, M = matrix(c(105,56,303,400,96,156),3,2), create the code that will change the value in the second column and second row to -105.',\
                            'Using the following list: myList = list(students=c(\'Paul\',\'Edward\',\'Mike\'),count=c(1,2)), create the code that will print out the contents of the students entry using the $ operator.',\
                            "Given the following dataframe, create the code that will change Edward's name to Joe. <br>df = data.frame(students= c('Paul','Edward','Mike'),grades=c('A','B','F')).<br>Hint: This will initial give you trouble because grades and students are a factors. To change this you must execute the following:<br>levels(df$students) = c('Paul','Edward','Mike','Joe'). This tells R the possible values for students.",\
                            "Create the code that changes the column names of the data frame given below to start with an uppercase letter using the colnames function.<br>df = data.frame(students= c('Paul','Edward','Mike'),grades=c('A','B','F')).",\
                            "Create the code that generates the following: (1) A matrix <b>M</b> with 5 columns that contains the values 1,2,...100. (2) The data frame <b>df</b> version of M, where the column names are 'v1','v2','v3','v4', and 'v5'. (3) Then modify <b>df</b> so that it contains a sixth column named <b>label</b> that contains the values 'One','Two','Three',...,'Twenty'. (4) Finally, put all of these into a list called <b>my.list</b> using the following command: my.list = list(M = M, my.df = df)"]
		workflow_ids_R = ['5969b1f7201f12ae','df7a1f0c02a5b08e','0a248a1f62a0cc04','03501d7626bd192f','3f5830403180d620','e85a3be143d5905b','1e8ab44153008be8','c9468fdb6dc5c5f1','2a56795cad3c7db3','4b187121143038ff']
		workflow_ids_python27 = []
	elif page == "fileIO":
		header="File I/O"
		paragraph= 'The software allows you to check your solutions as you progress through the level. In this level, you will be asked to read data from a file. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b>'
		problems = ["""Create the code that reads in the <a href="http://www.dcc.fc.up.pt/~ltorgo/DataMiningWithR/DataSets/Analysis.txt">Analysis.txt</a> 
                               file into a dataframe named <b>df</b> using the following headings: season,size,speed,mxPH,mnO2,Cl,NO3,NH4,oPO4,PO4,Chla,a1,a2,a3,a4,a5,a6,a7. Hint: There are missing values in this file, so you must use na.strings=c('XXXXXXX') in your command to read in the data. Type ?read.table or ?read.csv for more information.""",\
                            """Using the dataframe that you created in the previous problem, 
                               create the code that removes the variables a1 - a7.""",\
                            """Finally, create the code that perform the previous two tasks in 
                               addition to the following: Add the code that creates a new 
                               file on your system called numbers3.csv 
                               that stores the data in a comma delimited text file. This file 
                               must NOT contain quotes and it must NOT contain row numbers. 
                               To do this you can either use the write.table or write.csv 
                               function in R. To look up the documentation, type ?write.csv or 
                               ?write.table."""]
		workflow_ids_R = ['417e33144b294c21','2d9035b3fc152403','d413a19dec13d11e']
		workflow_ids_python27 = []
	elif page == "functions":
		header="Functions"
		paragraph= 'The software allows you to check your solutions as you progress through the level. In this level, you will be asked to create several functions. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b>'
		problems = ['Write a function that returns the average of three numbers. Here is the function definition. You must fill in the middle.<br><br>average3 <- function(v1,v2,v3) {<br>insert code here<br>}',\
                            'Write a function that find the roots of a quadratic equation and returns the results in an array. Make sure the positive root is the first element of the array. Here is the function definition. You must fill in the middle.<br><br>quadratic <- function(a,b,c) {<br>insert code here<br>}',\
                            'Write a function that returns the area of a triangle. Here is the function definition. You must fill in the middle. <br><br>area <- function(height,width) {<br>insert code here<br>}']
		workflow_ids_R = ['2f94e8ae9edff68a','8237ee2988567c1c','f09437b8822035f7']
		workflow_ids_python27 = []
	elif page == "loops":
		header="Loops with Functions"
		paragraph= 'The software allows you to check your solutions as you progress through the level. In this level, you will be asked to create several functions that use loops to accomplish a task. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b>'
		problems = ['Write a function that loops through the values of an array and returns the sum of the values using a for loop. You may not use the built in sum function. Here is the function definition. You must fill in the middle.<br><br>my.sum <- function(my.array) {<br>insert code here<br>}',\
                            'Write a function that loops through the values of an array and returns the geometric mean of the values using a for loop. You may not use the built in sum function. Here is the function definition. You must fill in the middle.<br><br>my.geometric.mean <- function(my.array) {<br>insert code here<br>}']
		workflow_ids_R = ['fb85969571388350','ba751ee0539fff04']
		workflow_ids_python27 = []
	elif page == "conditionals":
		header="Conditionals with Functions"
		paragraph= 'The software allows you to check your solutions as you progress through the level. In this level, you will be asked to create several functions that use conditionals to accomplish a task. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b>'
		problems = ['Write a function that returns the minimum of three numbers. Here is the function definition. You may not use the min function. You must fill in the middle.<br><br>min3 <- function(v1,v2,v3) {<br>insert code here<br>}',\
                            'Write a function that returns the minimum of an array of numbers. Here is the function definition. You may not use the min function. You must fill in the middle.<br><br>minimum <- function(my.array) {<br>insert code here<br>}']
		workflow_ids_R = ['63cd3858d057a6d1','b472e2eb553fa0d1']
		workflow_ids_python27 = []
	elif page == "empiricalNaiveBayes":
		header="Empirical Naive Bayes"
		paragraph= 'The software allows you to check your solutions as you progress through the level. The functions that you will be asked to complete will read in a file formatted in the same manner as <a href="http://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data">the famous Iris dataset</a>. You can assume that the last column will be the class label and the other columns are guranteed to be numeric and do not contain any missing data. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b>'
		problems = ["""Fill in the following function to determine the prior probability of the classes (could be more than 2 classes). The class labels should be sorted.<br>
                               <b>R</b><br>
                               computePriors <- function(datasetFile) {
                               <br>[insert code here]<br>
                               }<br>
                               The return statement should look like the following for the Iris dataset, but note that this is determined by the dataset 
                               and will change: return(list(priors=c(0.3,0.5,0.2),classes=c("Iris-setosa","Iris-versicolor","Iris-virginica")))<br>
                               <br>
                               <b>Python 2.7</b><br>
                               def computePriors(datasetFile):<br>
                               &nbsp&nbsp&nbsp&nbsp[insert code here]<br>
                               The return statement should look like the following for the Iris dataset, but note that this is determined by the dataset 
                               and will change: return {'priors': numpy array, 'classes': numpy array}<br><br>
                               """,\
                            """Fill in the following function to determine the class specific densities (fraction) of each variable using k uniformly 
                               spaced bins between the minimum and maximum for i-th feature.<br>
                               <b>R</b><br>
                               computeDensities <- function(datasetFile,i,class,k) {<br>
                               [insert code here]<br>
                               }<br>The return statement should look like the following for the Iris dataset, but note that this is determined by the 
                               dataset and will change: return(list(bounds=c(1,2,3,4),densities=c(0.3,0.6,0.1))). The ranges are <2, [2,3), >=3.
                               <br>
                               <b>Python 2.7</b><br>
                               def computeDensities(datasetFile,i,cls,k):<br>
                               &nbsp&nbsp&nbsp&nbsp[insert code here]<br>
                               The return statement should look like the following for the Iris dataset, but note that this is determined by the
                               dataset and will change: return {'bounds': numpy array,'densities': numpy array. The ranges are <2, [2,3), >=3.<br><br>
                               """,\
                            """Fill in the following function to determine the posterior probabilities of each sample in the dataset (one for each class).
                               The parameter k is the the same k for the uniformly spaced bins.<br>
                               <b>R</b><br>
                               computePosteriors <- function(datasetFile,k) {<br>
                               [insert code here]<br>
                               }<br>
                               The return statement should look like the following for the Iris dataset, but note that this is determined by the 
                               dataset and will change: return(matrix(...)), where each row corresponds to a sample and each column corresponds to a class.
                               Columns should be alphabetically sorted in ascending order according to the class name.<br>
                               <b>Python 2.7</b><br>
                               def computePosteriors(datasetFile,k):<Br>
                               &nbsp&nbsp&nbsp&nbsp[insert code here]<br>
                               The return statement should look like the following for the Iris dataset, but note that this is determined by the 
                               dataset and will change: return numpy array, where each row corresponds to a sample and each column corresponds to a class.
                               Columns should be alphabetically sorted in ascending order according to the class name.<br><br>
                            """]
		workflow_ids_R = ['ebfb8f50c6abde6d','33b43b4e7093c91f','f2db41e1fa331b3e']
		workflow_ids_python27 = ['1cd8e2f6b131e891','a799d38679e985db','f597429621d6eb2b']
	elif page == "LeaveOneOutCV":
		header="Leave-one-out Cross-validation"
		paragraph= 'The software allows you to check your solutions as you progress through the level. The functions that you will asked to write expected you to use a data frame (R) or a pandas data frame (python). You can assume that the last column will be the class label and the other columns are guranteed to be numeric and do not contain any missing data. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b>'
		problems = ["""
Create the following function to predict the class label of a vector called sample using a 1-nearest neighbor algorithm.<br>
<b>R</b><br>
		<pre><code>
			# Submission begin
			one.nn <- function(training.data,sample) {
			  [insert code here]
			}
			# Submission end
		</code></pre>
		This function should return the predicted class label. You may use the following code structure to run your function:<br>
		<pre>
			set.seed(100)
			df = data.frame(V1=rnorm(100),V2=rnorm(100),V3=rnorm(100),V4=rnorm(100),V5=rnorm(100),Class=sample(c("One","Two","Three","Four"),100,replace=T))

			for (i in 1:nrow(df)) {
			    print(one.nn(df[-i,],df[i,1:ncol(df)-1]))
			}
		</pre>
		<br>
		<b>Python 2.7</b><br>
		<pre>
			# Submission begin
			def one_nn(training_data,sample):
			  [insert code here]
			# Submission end
		</pre>
		This function should return the predicted class label. You may use the following code structure to run your function:<br>
		<pre>
			from numpy import *
			import random
			from pandas import *

			random.seed(100)

			def sample_wr(population, k):
			    "Chooses k random elements (with replacement) from a population"
			    n = len(population)
			    _random, _int = random.random, int  # speed hack
			    result = [None] * k
			    for i in xrange(k):
			        j = _int(_random() * n)
			        result[i] = population[j]
			    return result

			n = 100
			v1 = []
			v2 = []
			v3 = []
			v4 = []
			v5 = []
			for i in range (n):
			        v1.append(random.gauss(0,1))
			        v2.append(random.gauss(0,1))
			        v3.append(random.gauss(0,1))
			        v4.append(random.gauss(0,1))
			        v5.append(random.gauss(0,1))

			cls = sample_wr(["One","Two","Three","Four"],n)

			df = DataFrame({'v1':v1, 'v2':v2, 'v3':v3, 'v4': v4, 'v5':v5, 'zcls':cls})
			for i in range(len(df.index)):
			    pred = one_nn(df.drop([i]),df.iloc[i,0:(len(df.columns)-1)])
			    print pred
		</pre>
<br><br>
                               """,\
                            """
Create the following function to calculate the accuracy [0,1] of a data frame using your implementation of a 1-nearest neighbor algorithm.<br
<b>R</b><br>
<pre>
# Submission begin
accuracy <- function(training.data) {
    [insert code here]
}
# Submission end
</pre><br>
This function should return the accuracy, which is a number between 0 and 1. You may add the following to the code structure above to run your function:
<pre>
print accuracy(df)
</pre>
<b>Python 2.7</b><br>
<pre>
# Submission begin
def accuracy(training_data):
    [insert code here]
# Submission end
</pre><br>
This function should return the accuracy, which is a number between 0 and 1. You may add the following to the code structure above to run your function:
<pre>
print accuracy(df)
</pre><br>
                            """]
		workflow_ids_R = ['e89067bb68bee7a0','4ff6f47412c3e65e']
		workflow_ids_python27 = ['911dde3ddb677bcd','0c5ffef6d88a1e97']
	elif page == "decisionTree":
		header="Decision Tree"
		paragraph= 'The software allows you to check your solutions as you progress through the level. The functions that you will asked to write expects you to use a vectors and/or matrices. You can assume that all the variables will be categorical. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b><br><br>You may want to review the following source for information on entropy and information gain: <a href="http://www.autonlab.org/tutorials/infogain11.pdf">Information Gain</a>.'
		problems = ["""
Create the following function to calculate the entropy of a vector.<br>
<b>R</b><br>
<pre>
# Submission begin
entropy <- function(Y) {
    [code here]
}
# Submission end
</pre>
This function should return entropy as a float. You may use the following code structure to run your function:<br>
<pre>
set.seed(10)
df = data.frame(color=sample(c("Blue","Black","Red"),100,replace=T),income=sample(c("low","middle","high"),100,replace=T),age=sample(c("young","middle","old"),100,replace=T),Class=sample(c("One","Two","Three","Four"),100,replace=T))

print(entropy(df[,ncol(df)]))
</pre>
<br>
<b>Python 2.7</b><br>
<pre>
# Submission begin
def entropy(Y):
  [insert code here]
# Submission end
</pre>
This function should return the entropy as a float. You may use the following code structure to run your function:<br>
<pre>
Coming soon...
</pre>
<br><br>
                               """,\
                            """
Create a function that returns the specific conditional entropy.<br
<b>R</b><br>
<pre>
# Submission begin
spec.conditional.entropy <- function(Y,X,v) {
    [insert code here]
}
# Submission end
</pre><br>
This function should return the specific conditional entropy as a float. You may add the following to the code structure above to run your function:
<pre>
print(spec.conditional.entropy(df[,ncol(df)],df[,1],'Black'))
</pre>
<b>Python 2.7</b><br>
<pre>
# Submission begin
def spec_conditional_entropy(Y,X,v):
    [insert code here]
# Submission end
</pre><br>
This function should return the specific conditional entropy as a float. You may add the following to the code structure above to run your function:
<pre>
Coming soon...
</pre><br><br>
                               """,\
                            """
Create a function that returns the conditional entropy.<br
<b>R</b><br>
<pre>
# Submission begin
conditional.entropy <- function(Y,X) {
    [insert code here]
}
# Submission end
</pre><br>
This function should return the conditional entropy as a float. You may add the following to the code structure above to run your function:
<pre>
print(conditional.entropy(df[,ncol(df)],df[,2]))
</pre>
<b>Python 2.7</b><br>
<pre>
# Submission begin
def conditional_entropy(Y,X):
    [insert code here]
# Submission end
</pre><br>
This function should return the conditional entropy as a float. You may add the following to the code structure above to run your function:
<pre>
Coming soon...
</pre><br><br>
                               """,\
                            """
Create a function that returns the information gain.<br
<b>R</b><br>
<pre>
# Submission begin
information.gain <- function(Y,X) {
    [insert code here]
}
# Submission end
</pre><br>
This function should return the information gain as a float. You may add the following to the code structure above to run your function:
<pre>
print(information.gain(df[,ncol(df)],df[,2]))
</pre>
<b>Python 2.7</b><br>
<pre>
# Submission begin
def information_gain(Y,X):
    [insert code here]
# Submission end
</pre><br>
This function should return the information gain as a float. You may add the following to the code structure above to run your function:
<pre>
Coming soon...
</pre><br><br>
                               """,\
                            """
Create a function that splits Y into subsets determined by the values in X.<br
<b>R</b><br>
<pre>
# Submission begin
split.Y <- function(Y,X) {
    [insert code here]
}
# Submission end
</pre><br>
This function should return a list of subsets of Y. The order of the subsets is determined by sorting the unique values in X. You may add the following to the code structure above to run your function:
<pre>
print(split.Y(df[,ncol(df)],df[,2]))
</pre>
<b>Python 2.7</b><br>
<pre>
# Submission begin
def split_Y(Y,X):
    [insert code here]
# Submission end
</pre><br>
This function should return a list of subsets of Y. The order of the subsets is determined by sorting the unique values in X. You may add the following to the code structure above to run your function:
<pre>
Coming soon...
</pre><br><br>
                               """,\
                            """
Create a function that optimal splits Y into subsets using the column in Xs that provides the maximum information gain.<br
<b>R</b><br>
<pre>
# Submission begin
split.optimal <- function(Y,Xs) {
    [insert code here]
}
# Submission end
</pre><br>
This function should return a list of subsets of Y. The order of the subsets is determined by sorting the unique values in the column of Xs that provides the optimal information gain. You may add the following to the code structure above to run your function:
<pre>
print(split.optimal(df[,ncol(df)],df[,1:ncol(df)-1]))
</pre>
<b>Python 2.7</b><br>
<pre>
# Submission begin
def split_optimal(Y,Xs):
    [insert code here]
# Submission end
</pre><br>
This function should return a list of subsets of Y. The order of the subsets is determined by sorting the unique values in the column of Xs that provides the optimal information gain. You may add the following to the code structure above to run your function:
<pre>
Coming soon...
</pre><br><br>
                            """]
		workflow_ids_R = ['79966582feb6c081','5564089c81cf7fe8','ba03619785539f8c','cbbbf59e8f08c98c','964b37715ec9bd22','1fad1eaf5f4f1766']
		workflow_ids_python27 = ['911dde3ddb677bcd','0c5ffef6d88a1e97','0c5ffef6d88a1e97','0c5ffef6d88a1e97','0c5ffef6d88a1e97','0c5ffef6d88a1e97']
	elif page == "kmeans":
		header="k-means"
		paragraph= 'The software allows you to check your solutions as you progress through the level. The functions that you will asked to write expects you to use vectors, matrices, and/or dataframes. This is unsupervised learning, so the functions expect the class label to be removed. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b><br><br>You may want to review the following source for information on k-means: <a href="http://www.autonlab.org/tutorials/kmeans11.pdf">k-means</a>.'
		problems = ["""
Create the following function to calculate the euclidean distance between two vectors.<br>
<b>R</b><br>
<pre>
# Submission begin
distance <- function(sample1,sample2){
  [insert code here]
}
# Submission end
</pre>
This function should return the distances as a float. The parameters sample1 and sample2 are vectors. You may use the following code structure to run your function, and you can download the Iris dataset <a href="http://archive.ics.uci.edu/ml/machine-learning-databases/iris/">here</a>.<br>
<pre>
read.csv('iris.data',header=F)
sample1 = df[2,1:ncol(df)-1]
sample2 = df[8,1:ncol(df)-1]
print(distance(sample1,sample2))
</pre>
                               """,\
                            """
Create a function that assigns a single sample to one of the clusters.<br
<b>R</b><br>
<pre>
# Submission begin
assign.group <- function(means,sample) {
  [insert code here]
}
# Submission end
</pre><br>
This function should return the assigned cluster as an index (integer). Means is a matrix of size (k x d), where k is the number of clusters and d is the number of dimensions. The parameter sample is a vector of size (1xd). You may add the following to the code structure above to run your function:
<pre>
means = df[1:3,1:ncol(df)-1]
sample = df[30,1:ncol(df)-1]
print(assign.group(means,sample))
</pre>
                               """,\
                            """
Create a function that assigns multiple samples to the clusters.<br
<b>R</b><br>
<pre>
# Submission begin
assign.groups <- function(means,samples) {
  [insert code here]
}
# Submission end
</pre><br>
This function should return the assigned clusters as a vector of indices (integers). The parameter means is a matrix of size (k x d), where k is the number of clusters and d is the number of dimensions. The parameter samples is a matrix of size (n x d). You may add the following to the code structure above to run your function:
<pre>
means = df[1:3,1:ncol(df)-1]
samples = df[1:30,1:ncol(df)-1]
print(assign.groups(means,samples))
</pre>
                               """,\
                            """
Create a function that returns the means given a cluster assignment for each sample.
<b>R</b><br>
<pre>
# Submission begin
calculate.means <- function(samples,groups) {
  [insert code here]
}
# Submission end
</pre><br>
This function should return the calculated means as a matrix. The parameter groups is a vector of indices (i.e., returned by assign.groups). The order of the means in the resulting matrix must be sorted according to the parameter groups (i.e., group 1 should be listed first). The parameter samples is a matrix of size (n x d). You may add the following to the code structure above to run your function:
<pre>
means = df[1:3,1:ncol(df)-1]
samples = df[1:30,1:ncol(df)-1]
assigned.groups = assign.groups(means,samples)
print(calculate.means(samples,assigned.groups))
</pre>
                               """,\
                            """
Create a function that returns the means after running the standard k-means algorithm.<br>
<b>R</b><br>
<pre>
# Submission begin
kmeans <- function(samples,init.means) {
  [insert code here]
}
# Submission end
</pre><br>
This function should return a matrix that represent the means found from running the k-means standard algorithm. The parameter samples is a matrix of size (n x d). The parameter init.means is a matrix of size (k x d), where k is the number of clusters and d is the number of dimensions. You may add the following to the code structure above to run your function:
<pre>
means = df[1:3,1:ncol(df)-1]
samples = df[,1:ncol(df)-1]
print(kmeans(samples,means))
</pre>
                            """]
		workflow_ids_R = ['c385e49b9fe1853c','f7bb1edd6b95db62','52e496b945151ee8','b887d74393f85b6d','f0f309c56aff0025']
		workflow_ids_python27 = []
	elif page == "hierarchicalClustering":
		header="Hierarchical Clustering"
		paragraph= 'The software allows you to check your solutions as you progress through the level. The functions that you will asked to write expects you to use vectors, matrices, and/or dataframes. This is unsupervised learning, so the functions expect the class label to be removed. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b><br><br>You may want to review the following source for information on <a href="http://www.autonlab.org/tutorials/kmeans11.pdf">hierarchical clustering</a>.'
		problems = ["""
Create the following function to calculate the euclidean distance between two vectors.<br>
<b>R</b><br>
<pre>
# Submission begin
distance <- function(sample1,sample2){
  [insert code here]
}
# Submission end
</pre>
This function should return the distances as a float. The parameters sample1 and sample2 are vectors. You may use the following code structure to run your function, and you can download the Iris dataset <a href="http://archive.ics.uci.edu/ml/machine-learning-databases/iris/">here</a>.<br>
<pre>
reed.csv('iris.data',header=F)
sample1 = df[2,1:ncol(df)-1]
sample2 = df[8,1:ncol(df)-1]
print(distance(sample1,sample2))
</pre>
                               """,\
                            """
Create a function that calculates the UPGMA distance between two clusters.<br>
<b>R</b><br>
<pre>
# Submission begin
upgma <- function(samples1,samples2) {
  [insert code here]
}
# Submission end
</pre><br>
This function should return the UPGMA distance between two sets of variables. The parameter samples1 is a matrix of size (n x d), where n is the number of samples in cluster 1 and d is the number of dimensions. The parameter samples2 is a matrix of size (m x d), where m is the number of samples in cluster 2. You may add the following to the code structure above to run your function:
<pre>
samples1 = df[1:3,1:ncol(df)-1]
samples2 = df[10:30,1:ncol(df)-1]
print(upgma(samples1,samples2))
print(upgma(samples2,samples1))
</pre>
                               """,\
                            """
Create a function that selects the closest two groups in a list of groups using the UPGMA distance.<br>
<b>R</b><br>
<pre>
# Submission begin
select.two <- function(groups) {
  [insert code here]
}
# Submission end
</pre><br>
This function should return a vector that has three values. The first two are integers correspond to the indices of the two closest groups. The parameter groups is a list of matrices. You may add the following to the code structure above to run your function:
<pre>
groups = list(df[1:3,1:ncol(df)-1],df[4:10,1:ncol(df)-1],df[30:40,1:ncol(df)-1])
print(select.two(groups))
</pre>
                               """,\
                            """
Create a function that clusters a group of samples using UPGMA hiearchical clustering using the specified threshold.
<b>R</b><br>
<pre>
# Submission begin
hierarchical.cluster <- function(samples,threshold) {
  [insert code here]
}
# Submission end
</pre><br>
This function should a return list of matrices. Each element in the list (a matrix) corresponds to a group of samples that have been clustered together. To begin, every sample is in its own cluster/group. Then using the UPGMA distance, combine the two closest to a new cluster. Repeat this until the distance between the next two closest groups is greater than the threshold parameter (a float) or there is only one cluster remaining. You may add the following to the code structure above to run your function:
<pre>
samples = df[1:10,1:ncol(df)-1]
print(hierarchical.cluster(samples,0.5))
print(hierarchical.cluster(samples,Inf))
</pre>
                            """]
		workflow_ids_R = ['36ddb788a0f14eb3','72ad249754f05d26','eafb646da3b7aac5','42a2c611109e5ed3']
		workflow_ids_python27 = []
	elif page == "Test":
		header="Test"
		paragraph= 'The software allows you to check your solutions as you progress through the level. In this level, you will be asked to manipulate arrays, factors, vectors, matrices, lists, and data frames in R. <p><b>The first n-1 problems are for gaining experience and are technically optional. At any point, you may try your hand at the last problem or "boss fight". Successful completion of the last problem is required.</b><p>R has three basic indexing operators, with syntax displayed by the following examples:<br>x[i]<br>x[i, j]<br>x[[i]]<br>x[[i, j]]<br>x$a<br>x$"a"<br>For vectors and matrices the [[ forms are rarely used, although they have some slight semantic differences from the [ form (e.g. it drops any names or dimnames attribute, and that partial matching is used for character indices). When indexing multi-dimensional structures with a single index,x[[i]] or x[i] will return the ith sequential element of x.<br>For lists, one generally uses [[ to select any single element, whereas [ returns a list of the selected elements.<br>The [[ form allows only a single element to be selected using integer or character indices, whereas[ allows indexing by vectors. Note though that for a list, the index can be a vector and each element of the vector is applied in turn to the list, the selected component, the selected component of that component, and so on. The result is still a single element.'
		problems = ['v=1:101']
		workflow_ids_R = ['ebfb8f50c6abde6d']
		workflow_ids_python27 = []
	else:
		header="Content coming soon!"
		paragraph="We are working hard to expand on content. Please check again later!"
		problems = ' '
		workflow_ids_R = [None,None,None]
		workflow_ids_python27 = [None,None,None]




	return {
            'header':header,
            'paragraph': paragraph,
            'problems':problems,
            'reminder':reminder,
            'workflow_ids_R': workflow_ids_R,
            'workflow_ids_python27': workflow_ids_python27
        }
