#!/usr/bin/python3

import requests
import json

########## FILLMEIN
telegram_api_key = ''   # format botXXXXXX:XXXXXXX
chat_id = ''
postcode = '1234AA'
##########

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:75.0) Gecko/20100101 Firefox/75.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Referer': 'https://www.ah.nl/kies-moment/bezorgen/{}'.format(postcode),
    'X-Order-Mode': '',
    'X-Breakpoint': 'xxlarge',
    'X-Requested-With': 'XMLHttpRequest',
    'Connection': 'keep-alive',
    'TE': 'Trailers',
}

params = (
    ('url', '/kies-moment/bezorgen/{}'.format(postcode)),
)

response = requests.get('https://www.ah.nl/service/rest/delegate', headers=headers, params=params)

for day in json.loads(response.text)['_embedded']['lanes'][3]['_embedded']['items'][0]['_embedded']['deliveryDates']:
  for slot in day['deliveryTimeSlots']:
    if slot['state'] != 'full':
      message = "AH delivery timeslot available on {}: from {} to {}".format(day['date'], slot['from'], slot['to'])
      url = "https://api.telegram.org/{}/sendMessage?text={}&chat_id={}"
      req = url.format(telegram_api_key, message, chat_id)
      print(req)
      requests.get(req)
