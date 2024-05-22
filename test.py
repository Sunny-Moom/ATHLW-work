import json
import sys

import requests

import utils.adb_lw as adb
import utils.cv_lw as cv
import utils.ocr_lw as ocr


def getuser():
    url = 'http://192.168.0.109:8086'
    data = {'action': 'get_unassigned_account'}
    response = requests.post(url, data=data)
    data = json.loads(response.text)
    data = data["data"]
    return data["username"], data["password"]


if __name__ == '__main__':
    devices = sys.argv[1]
    print(devices)
    adb.cls()
    adb.adb_image(devices)
    cv.find_and_act_on_image('wsz', 9, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 10, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 11, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 12, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 13, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 14, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 15, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 16, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 17, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 18, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 19, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 20, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 21, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 22, 1, 'click', None, devices)
    while cv.find_and_act_on_image('wsz', 24, 10, 'click', 1, devices) is False:
        cv.find_and_act_on_image('wsz', 25, 1, 'click', 1, devices)
        cv.find_and_act_on_image('wsz', 23, 1, 'click', 1, devices)
