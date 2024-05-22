import os
import subprocess
from configparser import ConfigParser
import scripts.startini as star

path = './config/settings.ini'  # 配置文件路径

if __name__ == '__main__':
    ary = star.adb_check()
    # os.system(f"start cmd /k ls")
    for devices in ary:
        os.system(f"start cmd /k python ./nameid.py {devices}")
