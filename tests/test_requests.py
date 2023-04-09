import requests
from json import JSONDecodeError
#import json
from consts import SERVICE_URL
from sources.enums.global_enums import GlobalErrorMessages

def test_get_req():
    #responce = requests.get(url = SERVICE_URL)
    
    #print(responce.__getattribute__(name))
    
    headers = {'Accept': 'application/json'}
    try:
        responce = requests.get(SERVICE_URL)
        stat_code = responce.status_code
        assert stat_code in range(200, 300), GlobalErrorMessages.WRONG_STATUS_CODE.value
    except JSONDecodeError:
        print('No JSON')
    