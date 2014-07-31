from google.appengine.api import users
from google.appengine.ext import db


#####################
'''
This class is included for handling our interaction
with the datastore. It's required.
'''
#####################
class User(db.Model):
    EMAIL = db.StringProperty()
    PATTERN = db.StringProperty()
    CLUSTERING = db.StringProperty()
    UPLOADING = db.StringProperty()
    KNN = db.StringProperty()
    KMEANS = db.StringProperty()
    HC = db.StringProperty()
    CLASSIFICATION = db.StringProperty()
    NAIVEBAYES = db.StringProperty()
    SVM = db.StringProperty()
    NN = db.StringProperty()
    DTREE = db.StringProperty()
    REGRESSION = db.StringProperty()
    OTHER = db.StringProperty()
    SCALEFILTER = db.StringProperty()
    MARKETBASKET = db.StringProperty()
    PCA = db.StringProperty()
    CASE = db.StringProperty()
    CASE1 = db.StringProperty()
    CASE2 = db.StringProperty()
    CASE3 = db.StringProperty()
    SESSION = db.StringProperty()
    BADGESDUE = db.StringListProperty()
    BADGESEARNED = db.StringListProperty()
    SKILLSEARNED = db.StringListProperty()

#################################
'''
This function creates a user's skill tree
It reads in values from the datastore based upon the user's email
We implement a treeType so we can prepare for having
	more than just the default skill tree later
'''
#################################
def makeTemplateValues(useremail):

	# Let's make sure the User exists before doing any work
	try:
		db.Query(User).filter("EMAIL =", useremail).get().SESSION
	except:
		return '<p>This user does not exist or there is some worse error. If this problem persists, contact us, please!</p>'

	# Get a handle on the user
	user_query = db.Query(User)
        user_query.filter('EMAIL =', useremail)
        user = user_query.get()
	
	## This dictionary gives us a quick hash reference to the user's attributes
	template_values = {
        'pr': user.PATTERN,
        'clustering': user.CLUSTERING,
	'uploading': user.UPLOADING,
        'knn': user.KNN,
        'kmeans': user.KMEANS,
        'hc': user.HC,
        'classification': user.CLASSIFICATION,
        'nb': user.NAIVEBAYES,
        'svm': user.SVM,
        'nn': user.NN,
        'dtree': user.DTREE,
        'regression': user.REGRESSION,
        'other': user.OTHER,
        'scalefilter': user.SCALEFILTER,
        'markbask': user.MARKETBASKET,
        'pca': user.PCA,
	'case': user.CASE,
	'case1': user.CASE1,
	'case2': user.CASE2,
	'case3': user.CASE3,
	'user':useremail,
	'badges':user.BADGESEARNED
        }
	
	allBadges = ["uploadingMastery","algaeLearned","kmeansLearned","marketMastery",
"pcaMastery","RPrediction1Mastery","stocksLearned","algaeMastery",
"kmeansMastery","nnLearned","plsLearned","RPrediction2Mastery","stocksMastery","fraudLearned","knnLearned"," nnMastery",
"plsMastery","scaleFilterLearned","uploadingMastery","fraudMastery","knnMastery",
"RFileIOMastery","scaleFilterMastery","marketLearned","pcaLearned",
"RMissingValuesMastery","basicRMastery","advancedUnknownMastery",
"advancedStandardMastery","advancedFileMastery","advancedPredictionMastery","loopsMastery","conditionalsMastery",
"functionsMastery","evaluationMastery","basicRTutorialMastery","fileIOTutorialMastery","knnRTutorialMastery",
"loopsConditionalsTutorialMastery","knnToolTutorialMastery","dataMiningMastery","bayesMastery",
"empiricalNBMastery","crossValidationMastery","testSetMastery","kFoldMastery","leaveOneOutMastery", "classificationMastery",
"aiMastery","searchMastery","bfsMastery","dfsMastery","ucsMastery","decisionTreeMastery","clusteringMastery","kmeansClusteringMastery",
"knapsackMastery","hierarchicalClusteringMastery"]#FLAG1
	image_values = template_values['badges']
	image_hash = {}
	for badge in allBadges:
		#image_hash.update({badge:badge}) # Uncomment this out and comment out conditionals to test
		if badge in image_values:
			image_hash.update({badge:badge})
		elif badge not in image_values:
			image_hash.update({badge:'unearned_'+badge})
	
	return image_hash
	
