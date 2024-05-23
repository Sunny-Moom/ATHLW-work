import json

import requests


def getpost():
    url = 'http://localhost:7888/your-endpoint'
    data = "Your test message"
    headers = {'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}

    response = requests.post(url, data=data, headers=headers)

    # 输出指令内容
    return response.text


if __name__ == '__main__':
    print(getpost())
