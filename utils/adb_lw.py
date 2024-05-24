import subprocess
from configparser import ConfigParser

path = './config/settings.ini'  # 配置文件路径

config = ConfigParser()
config.read(path)
adb_config = config.get('bin', 'adb')


def cls():
    subprocess.call('cls', shell=True)


def adb_call(call, devices=None):
    """
    无输出地执行adb命令
    :call: 要执行的指令
    :devices: adb设备号
    :return: 无输出
    """
    if devices is not None:
        subprocess.call(adb_config + f"adb -s {devices} " + call, shell=True, stdout=subprocess.DEVNULL)
    else:
        subprocess.call(adb_config + "adb " + call, shell=True, stdout=subprocess.DEVNULL)


def adb_image(devices=None):
    """
    使用adb截图
    :devices: adb设备号
    :return: 将截图输出至.img/screen.png
    """
    adb_call("shell screencap -p /sdcard/screen.png", devices)
    adb_call(f"pull /sdcard/screen.png ./data/img/{devices}screen.png", devices)


def adb_inputs(text, devices=None):
    """
    使用adb输入，依赖于https://github.com/senzhk/ADBKeyBoard
    :text: 要输入的文本
    :devices: adb设备号
    :return: 无输出
    """
    adb_call("shell am broadcast -a ADB_INPUT_TEXT --es msg \\\"" + text + "\\\"", devices)


def adb_touch(x, y, devices=None):
    """
    adb模拟点击
    :param x: x坐标
    :param y: y坐标
    :devices: adb设备号
    :return: 无输出
    """
    adb_call("shell input tap {} {}".format(x, y), devices)
