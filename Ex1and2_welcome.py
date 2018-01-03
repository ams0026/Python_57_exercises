#mypython.py
import datetime as dt
import requests
import json

var = input("What is your username? ")
today = dt.date.today()
message = "Hello " + var + "! \nToday is: " + str(today)
print (message)

url = 'https://icanhazdadjoke.com/slack'
response = requests.get(url)
if response.status_code == requests.codes.ok:
    parsed_response = json.loads(response.text)
    joke = parsed_response['attachments'][0]['text']
    print("Today's joke: \n" + joke)
    print("\nThis joke was just " + str(joke.count(" ")+1) + " words long. \n")
exit
    

