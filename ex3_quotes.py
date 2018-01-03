import requests
import json

url = 'http://api.forismatic.com/api/1.0/'
payload = {'method':'getQuote','format': 'json','key':'2','lang':'en'}
r = requests.get(url,payload)
if r.status_code == requests.codes.ok:
    #print(r.status_code)
    #print(r.text)
    parsed_response = json.loads(r.text)
    quote = parsed_response['quoteText']
    author = parsed_response['quoteAuthor']
    if author.isspace():
        author = "Unknown"
    print(author + ' said: "' + quote + '"\n')
else:
    print("Site returned: " + r.status_code + "\nTry again later. \n")
    

exit
