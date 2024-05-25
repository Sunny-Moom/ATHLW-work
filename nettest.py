import os
import scripts.startini as star


if __name__ == '__main__':
    ary = star.adb_check()
    os.system(f"start cmd /c python ./netserver.py")
    for devices in ary:
        os.system(f"start cmd /k python ./wsz.py {devices}")
