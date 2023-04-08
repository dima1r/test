import requests
import json
from consts import SERVICE_URL
from sources.enums.global_enums import GlobalErrorMessages

def test_get_req():
    responce = requests.get(url = SERVICE_URL)
    stat_code = responce.status_code
    print(stat_code)
    #print(responce.__getattribute__(name))
    assert stat_code in range(200, 300), GlobalErrorMessages.WRONG_STATUS_CODE.value