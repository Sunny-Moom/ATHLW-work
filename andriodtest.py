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
    # ocr.find_text_in_image('无双斩', devices)
    adb.adb_call("shell ime enable com.android.adbkeyboard/.AdbIME", devices)
    adb.adb_call("shell ime set com.android.adbkeyboard/.AdbIME", devices)
    # cv.find_and_act_on_image('wsz', 5, 1, 'click', 4, devices)
    # cv.find_and_act_on_image('wsz', 1, 1, 'click', 4,devices)
    # cv.find_and_act_on_image('wsz', 2, 1, 'click', 4,devices)
    # cv.find_and_act_on_image('wsz', 3, 1, 'click', 4,devices)
    # input("验证码步骤请手动输入")
    # # 验证码手动操作
    # cv.find_and_act_on_image('wsz', 5, 1, 'click', 4,devices)
    # cv.find_and_act_on_image('wsz', 5, 1, 'click', 4,devices)  #权限申请可复用
    name, nameid = getuser()
    ocr.find_text_in_image('请填写真实姓名',devices)
    adb.adb_inputs(name, devices)
    ocr.find_text_in_image('请填写有效的身份证号',devices)
    adb.adb_inputs(nameid, devices)
    # cv.find_and_act_on_image('wsz', 6, 1, 'click',None,devices)
    # cv.find_and_act_on_image('wsz', 7, 1, 'click',None,devices)
    # cv.find_and_act_on_image('wsz', 8, 1, 'click', 4,devices)
    # cv.find_and_act_on_image('wsz', 9, 1, 'click', 4,devices)
