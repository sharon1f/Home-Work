import requests

     #valid api parametrs
payloadvalid = {'customerID':'bcqa','action':'getScore','uuid':'QA_AndroidSDKTP93D6LR','customerSessionID':'csid_qa_1516617094.58','activityType':'MAKE_PAYMENT','brand':'testQa'}
     # invalid api parametrs
payloadinvalid = {'customerID':'bcqa','action':'getScore','uuid':'QA_AndroidSDKTP93D6LR','customerSessionID':'','activityType':'MAKE_PAYMENT','brand':'testQa'}
     # get request with valid parametrs
baseurlvalid = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score', params=payloadvalid)
     # get request with invalid parametrs
baseurlinvalid = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score', params=payloadinvalid)
      # parse the respond and extract the "score" value field
data=baseurlvalid.json()
#check if the score is higher
if (data['score']>=800):
 baseurlvalid = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score', params=payloadvalid)
 baseurlinvalid = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score', params=payloadinvalid)
#the score is smaller
else:
 baseurlvalid = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score', params=payloadvalid)
 baseurlinvalid = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score', params=payloadinvalid)