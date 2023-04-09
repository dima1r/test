import requests
from json import JSONDecodeError
#import json
from consts import SERVICE_URL
from sources.enums.global_enums import GlobalErrorMessages

def test_get_req():
    #responce = requests.get(url = SERVICE_URL)
    #stat_code = responce.status_code
    #print(responce)
    #print(responce.__getattribute__(name))
    # assert stat_code in range(200, 300), GlobalErrorMessages.WRONG_STATUS_CODE.value
    headers = {'Accept': 'application/json'}
    try:
        responce = requests.get(SERVICE_URL, headers = headers).json()
        print(responce)
        #received_data = responce.json()
    except JSONDecodeError:
        print('No JSON')
    