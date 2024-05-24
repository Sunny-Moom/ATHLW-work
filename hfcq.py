import json
import random
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


def generate_random_char():
    # 所有可能字符
    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # 随机选择一个字符
    char = ''
    for i in range(8):
        char = char + random.choice(chars)
    return char


command = getpost()

if __name__ == '__main__':
    devices = sys.argv[1]
    print("请输入启动指令")
    while command != '启动':
        command = getpost()
        time.sleep(2)
    print("已启动")
    print(devices)
    adb.adb_image(devices)
    adb.adb_call("shell ime enable com.android.adbkeyboard/.AdbIME", devices)
    adb.adb_call("shell ime set com.android.adbkeyboard/.AdbIME", devices)
    cv.find_and_act_on_image('hfcq', 1, 2, 'click', None, devices)
    username = generate_random_char()
    password = generate_random_char()
    ocr.find_text_in_image('用户名', devices)
    adb.adb_inputs(username, devices)
    ocr.find_text_in_image('密码', devices)
    adb.adb_inputs(password, devices)
    ocr.find_text_in_image('密码', devices)
    adb.adb_inputs(password, devices)
    cv.find_and_act_on_image('hfcq', 2, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 3, 2, 'click', None, devices)
    name, nameid = getuser()
    ocr.find_text_in_image('姓名', devices)
    adb.adb_inputs(name, devices)
    ocr.find_text_in_image('身份证号', devices)
    adb.adb_inputs(nameid, devices)
    cv.find_and_act_on_image('hfcq', 5, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 6, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 7, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 8, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 9, 2, 'click', None, devices)
    print("输入区号")
    while command == '启动':
        command = getpost()
        time.sleep(2)
    ocr.find_text_in_image(command, devices)
    cv.find_and_act_on_image('hfcq', 10, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 11, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 12, 2, 'click', None, devices)
    for i in range(6):
        cv.find_and_act_on_image('hfcq', 13, 2, 'click', None, devices)
        cv.find_and_act_on_image('hfcq', 14, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 15, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 16, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 17, 2, 'click', None, devices)
    cv.find_and_act_on_image('hfcq', 18, 2, 'click', None, devices)
