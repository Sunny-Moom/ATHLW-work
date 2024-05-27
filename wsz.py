import json
import sys
import time

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


def getpost():
    url = 'http://localhost:7888/your-endpoint'
    data = "Your test message"
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}

    response = requests.post(url, data=data, headers=headers)

    # 输出指令内容
    return response.text


command = getpost()


def leve():
    """
    练级
    Returns:

    """
    global command
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
    # 寻帮逻辑
    print("输入帮会名称")
    while command.isdigit():
        command = getpost()
        time.sleep(2)
    ocr_report = ocr.report_text_in_image(command, devices)
    adb.adb_touch(ocr_report[0] + 562, ocr_report[1])
    cv.find_and_act_on_image('wsz', 27, 1, 'click', None, devices)


if __name__ == '__main__':
    devices = sys.argv[1]
    print("请输入启动指令")
    while command != '启动':
        command = getpost()
        time.sleep(2)
    print("已启动")
    print(devices)
    # adb.cls()
    adb.adb_image(devices)
    adb.adb_call("shell ime enable com.android.adbkeyboard/.AdbIME", devices)
    adb.adb_call("shell ime set com.android.adbkeyboard/.AdbIME", devices)
    # cv.find_and_act_on_image('wsz', 5, 2, 'click', 4, devices)
    # cv.find_and_act_on_image('wsz', 1, 2, 'click', None, devices)
    # cv.find_and_act_on_image('wsz', 2, 2, 'click', None, devices)
    # cv.find_and_act_on_image('wsz', 3, 2, 'click', None, devices)
    # print("验证码步骤请手动输入")
    # # 验证码手动操作
    # while command != '验证码':
    #     command = getpost()
    #     time.sleep(2)
    # cv.find_and_act_on_image('wsz', 5, 2, 'click', 4, devices)
    # cv.find_and_act_on_image('wsz', 5, 2, 'click', 4, devices)  # 权限申请可复用
    # cv.find_and_act_on_image('wsz', 6, 1, 'report', None, devices)
    # name, nameid = getuser()
    # ocr.find_text_in_image('姓名', devices)
    # adb.adb_inputs(name, devices)
    # ocr.find_text_in_image('身份证号', devices)
    # adb.adb_inputs(nameid, devices)
    # cv.find_and_act_on_image('wsz', 6, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 4, 1, 'click', None, devices)
    # 寻区逻辑
    print("输入区号")
    while not command.isdigit():
        command = getpost()
        time.sleep(2)
    ocr.find_text_in_image(command, devices)
    # 练级逻辑
    cv.find_and_act_on_image('wsz', 8, 1, 'click', None, devices)
    leve()
    cv.find_and_act_on_image('wsz', 28, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 29, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 30, 1, 'click', None, devices)
    leve()
    cv.find_and_act_on_image('wsz', 31, 1, 'click', None, devices)
    cv.find_and_act_on_image('wsz', 32, 1, 'click', None, devices)

