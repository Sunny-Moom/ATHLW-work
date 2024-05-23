import os
import scripts.startini as star


if __name__ == '__main__':
    ary = star.adb_check()
    os.system(f"start cmd /c python ./netserver.py")
    for devices in ary:
        os.system(f"start cmd /k python ./andriodtest.py {devices}")
    # print('1.测试环境       2.身份证填充      3.生产环境')
    # codd = int(input("请输入序号选择："))
    # if codd is 1:
    #     for devices in ary:
    #         os.system(f"start cmd /c python ./test.py {devices}")
    # elif codd is 2:
    #     for devices in ary:
    #         os.system(f"start cmd /c python ./nameid.py {devices}")
    # elif codd is 3:
    #     for devices in ary:
    #         os.system(f"start cmd /c python ./nameid.py {devices}")
    # else:
    #     print("输入错误")

