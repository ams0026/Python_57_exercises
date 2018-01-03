#https://www.wordsapi.com/docs
#needs authorization to return a word


import requests
import json

url = 'https://wordsapiv1.p.mashape.com/words/?random=true'
#payload = {'method':'getQuote','format': 'json','key':'2','lang':'en'}
r = requests.get(url)
if r.status_code == requests.codes.ok:
    print(r.status_code)
    print(r.text)
    parsed_response = json.loads(r.text)
    # quote = parsed_response['quoteText']
    # author = parsed_response['quoteAuthor']
else:
    print("Site returned: " + str(r.status_code) + "\nTry again later. \n")
    

exit