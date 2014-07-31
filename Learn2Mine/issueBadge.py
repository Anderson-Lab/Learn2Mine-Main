def issueBadge(userBadges):
	try:
		if len(userBadges) > 1:
			badgeDisplay = ''
			for i in range(len(userBadges)-1):
				badgeDisplay = badgeDisplay + "<img width='100px' height='100px' src='images/"+userBadges[i+1]+".png'></img>"
		else:
			badgeDisplay='You have not yet earned any Badges!'
		print(badgeDisplay)
		template_values = {'user':useremail,'badgeDisplay':badgeDisplay}
		#Get the currently logged in user's info
		user_query = db.Query(User)
		user = user_query.filter('EMAIL =', useremail).get()

		#Check if the user is due any badges, if so, issue it with the Openbadges.issue() function
		writeText = '<script src="https://beta.openbadges.org/issuer.js"></script>'
		user.BADGESDUE = list(set(user.BADGESDUE))
		if len(user.BADGESDUE) > 1:
			writeText=writeText+'<script>window.onload = function(){OpenBadges.issue(["http://portal.cs.cofc.edu/learn2mine/static/badges/'+useremail.split("@")[0]+user.BADGESDUE[1]+'.json"], function(errors, successes) {console.log(errors.reason);window.location = "http://learn2mine.appspot.com/Home"});}</script>'
			if(user.BADGESDUE[1] not in user.BADGESEARNED):
				user.BADGESEARNED.append(user.BADGESDUE.pop(1))
			else:
				user.BADGESDUE.pop(1)
			user.put()
	except:
		badgeDisplay = 'You have not yet earned any badges!'
		template_values = {'user':useremail,'badgeDisplay':badgeDisplay}
		writeText = ' '
		print("in the except")

	return template_values, writeText