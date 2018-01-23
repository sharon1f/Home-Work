import requests
payload = {'customerID':'bcqa','action':'getScore','uuid':'QA_AndroidSDKTP93D6LR','customerSessionID':'csid_qa_1516617094.58','activityType':'MAKE_PAYMENT','brand':'testQa'}
baseurl = requests.get('https://api.bcqa.bc2.customers.biocatch.com/api/v6/score', params=payload)
print(baseurl )
print (baseurl)