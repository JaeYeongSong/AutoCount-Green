import json
import requests
from datetime import datetime

with open('config.json', 'r') as file:
    config = json.load(file)

slackToken = config['slackToken']
crawlingDelay = config['crawlingDelay']

def postMessage(token, channel, text):
    response = requests.post('https://slack.com/api/chat.postMessage',
        headers={'Authorization': 'Bearer '+token},
        data={'channel': channel,'text': text}
    )

def postGreenData(text):
    postMessage(slackToken, '#초록여행-데이터', text)

def now():
    nowTimes = datetime.now()
    return nowTimes.strftime('%Y-%m-%d %H:%M:%S')