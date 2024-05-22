import os
import scripts.startini as star

path = './config/settings.ini'  # 配置文件路径

if __name__ == '__main__':
    ary = star.adb_check()
    print('1.测试环境       2.身份证填充      3.生产环境')
    codd = int(input("请输入序号选择："))
    if codd is 1:
        for devices in ary:
            os.system(f"start cmd /k python ./test.py {devices}")
    elif codd is 2:
        for devices in ary:
            os.system(f"start cmd /k python ./nameid.py {devices}")
    elif codd is 3:
        for devices in ary:
            os.system(f"start cmd /k python ./nameid.py {devices}")
    else:
        print("输入错误")
