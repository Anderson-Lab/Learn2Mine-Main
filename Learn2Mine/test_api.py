from galaxy_api import *
import json
import time

#print workflow_execute_parameters("3c7d82a64160fdc165ce6542e0f918d6","http://portal.cs.cofc.edu/learn2mine/api/workflows/","f2db41e1fa331b3e","hist_id=63cd3858d057a6d1","param=loops=input1=testing")

api_key = "3c7d82a64160fdc165ce6542e0f918d6"
url = "http://portal.cs.cofc.edu/learn2mine/api/workflows/"
workflow_id = "f2db41e1fa331b3e"
hist_id = "63cd3858d057a6d1"
#print workflow_execute_parameters(api_key,url,workflow_id,"hist_id="+hist_id,"param=gradeCode=studentCode=print(\"testing\")","param=gradeCode=email=pauleanderson@gmail.com","param=gradeCode=language=R","param=gradeCode=badgeName=None")
other=json.dumps({"email":"pauleanderson@gmail.com","studentCode":"testing=1"})
result = workflow_execute_parameters(api_key,url,workflow_id,"hist_id="+hist_id,"param=gradeCode=other="+other)
outputid = result['outputs'][0]
time.sleep(10)
url = "http://portal.cs.cofc.edu/learn2mine/api/histories/"+hist_id+"/contents/"+outputid+"/display"
print url
print display_result("3c7d82a64160fdc165ce6542e0f918d6",url)
