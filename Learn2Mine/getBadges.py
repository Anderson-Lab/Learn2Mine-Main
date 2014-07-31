import json
import urllib, urllib2, httplib, httplib2

def main(useremail):
	h = httplib2.Http()
	data =dict(email=useremail)
	resp, content = h.request("http://beta.openbadges.org/displayer/convert/email", "POST", urllib.urlencode(data))
	print(resp)
	return(resp, content)
