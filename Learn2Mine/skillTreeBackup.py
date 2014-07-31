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
def makeSkillTree(treeType,useremail):

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
	tree = ''
	if treeType == 'dataminer':
		tree += '<ul id=\"org\" style=\"display: none;">'
		tree += '<li><div id="skpattern" class=\"'+template_values['pr']+'\"><p>Pattern Recognition</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skclustering" class=\"'+template_values['clustering']+'\"><p>Clustering</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skkmeans" class=\"'+template_values['kmeans']+'\"><p>K-Means Clustering</p></div>'
		tree += '<ul>'
		#tree += '<li><div id="skhc" class=\"'+template_values['hc']+'\"><p>Hierarchical Clustering</p></div></li>'
		tree += '</ul></li></ul></li>'
		tree += '<li><div id="skclassification" class=\"'+template_values['classification']+'\"><p>Classification</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skknn" class=\"'+template_values['knn']+'\"><p>K-Nearest Neighbors</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skregression" class=\"'+template_values['regression']+'\"><p>Regression</p></div>'
		tree += '<ul>'
		tree += '<li><div id="sknn" class=\"'+template_values['nn']+'\"><p>Neural Networks</p></div>'
		#tree += '<li><div id="sksvm" class=\"'+template_values['svm']+'\"><p>Support Vector Machines</p></div></li>'
		tree += '</li></ul>'
		#tree += '<li><div id="skdtree" class=\"'+template_values['dtree']+'\"><p>Decision Trees</p></div>'
		#tree += '</li>'
		#tree += '<li><div id="sknb" class=\"'+template_values['nb']+'\"><p>Naive Bayes</p></div></li>'
		tree += '</ul></li></ul></li>'
		tree += '<li><div id="skother" class=\"'+template_values['other']+'\"><p>Other Techniques</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skmarkbask" class=\"'+template_values['markbask']+'\"><p>Market Basket Analysis</p></div></li>'
		tree += '<li><div id="skscalefilter" class=\"'+template_values['scalefilter']+'\"><p>Scale And Filter</p></div>'
		tree += '<ul><li><div id="skpca" class=\"'+template_values['pca']+'\">Principal Component Analysis</div></li></ul></li>'
		tree += '</ul></li>'
		tree += '<li><div id="skcase" class=\"'+template_values['case']+'\"><p>Case Studies</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skcase1" class=\"'+template_values['case1']+'\"><p>Algal Blooms</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skcase2" class=\"'+template_values['case2']+'\"><p>Stock Market</p></div>'
		tree += '<ul>'
		tree += '<li><div id="skcase3" class=\"'+template_values['case3']+'\"><p>Detecting Fraud</p></div>'
		tree += '</ul></li></ul></li></ul></li>'
		tree += '</ul></li>'
		tree += '</ul>'
		return tree

	# This tree doesn't use the sk_____ id's. Not sure why they are needed.
	elif treeType == 'rprogrammer':
		#print template_values['badges']
		badges = template_values['badges'][1:] # Ignores the first, blank value in the badges list
		rBadges = ['standardRMastery','RMissingValuesMastery','RFileIOMastery','RPrediction1Mastery','RPrediction2Mastery']
		badgeTree = {'standardRMastery':'stillneedswork',
					'RMissingValuesMastery':'stillneedswork',
					'RFileIOMastery':'stillneedswork',
					'RPrediction1Mastery':'stillneedswork',
					'RPrediction2Mastery':'stillneedswork'
					}

		# Writing this in such a way that you can have badges that don't relate to the rprogrammer tree
		for badge in badges:
			if badge in rBadges:
				badgeTree[badge] = 'mastered'

		# This is a way to see if they have mastered every R skill so the root can take on a mastered or stillneedswork value/color
		R = 'mastered'
		for skill in badgeTree:
			if badgeTree[skill] != 'mastered':
				R = 'stillneedswork'


		tree += '<ul id=\"org\" style=\"display: none;">'
		tree += '<li><div class=\"'+R+'\"><p>R</p></div>'
		tree += '<ul><li><div class=\"'+badgeTree['standardRMastery']+'\"><p>Standard R</p></div><ul>'
		tree += '<li><div class=\"'+badgeTree['RMissingValuesMastery']+'\"><p>Missing Values</p></div></li>'
		tree += '<li><div class=\"'+badgeTree['RFileIOMastery']+'\"><p>File I/O</p></div></li>'
		tree += '<li><div class=\"'+badgeTree['RMissingValuesMastery']+'\"><p>Missing Values</p></div></li>'
		tree += '<li><div class=\"'+badgeTree['RPrediction1Mastery']+'\"><p>Prediction 1</p></div><ul>'
		tree += '<li><div class=\"'+badgeTree['RPrediction2Mastery']+'\"><p>Prediction 2</p></div></li>'
		tree += '</ul></li>'
		tree += '</ul></li></ul>'
		tree += '</li>'
		tree += '</ul>'
		return tree
	elif treeType == 'bioinformatician':
		return tree

def makeProfileHTML(skilltree):
	#################################### 
	'''
	skilltrees contains all the possible skill trees
	skilltrees must match the values in the treeType functions above

	location is a way to find the index, programmatically, for whichever skill tree we're on
	This is used for the arrows

	The forward arrow in the return uses a %
	This is so that we don't hit array out of bounds; essentially, our list is now circular
	'''
	####################################

	skilltrees = ['dataminer','rprogrammer']#,'bioinformatician']
	location = skilltrees.index(skilltree)
	return '<a href="?tree='+str(skilltrees[location-1])+'"><div class="arrow" id="backProfileArrow"></div></a><a href="?tree='+str(skilltrees[(location+1)%len(skilltrees)])+'"><div class="arrow" id="forwardProfileArrow"></div></a>'