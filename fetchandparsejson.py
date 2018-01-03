import requests
import json

url = 'https://icanhazdadjoke.com/slack'
response = requests.get(url)
if response.status_code == requests.codes.ok:
    print(response.text)
    parsed_response = json.loads(response.text)

    print(parsed_response['attachments'][0]['text'])
    

