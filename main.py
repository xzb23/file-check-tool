import sys
import os
import init_

# command = "python check.py"
command = "check.exe"

if not os.path.exists(init_.data_path):
    with open(init_.data_path, "w", encoding="utf-8") as f:
        f.writelines(["0"])

with open(init_.data_path, "r", encoding="utf-8") as f:
    flag = f.readline().strip() == "1"

if (len(sys.argv) < 2):
    print("参数错误！需要一个文件路径")
    # input()
    sys.exit()

if flag:
    with open(init_.data_path, "r", encoding="utf-8") as f:
        filepath1 = f.readlines()[1].strip()
    init_.init_config()
    filepath2 = sys.argv[1]
    os.system(f"{command} \"{filepath1}\" \"{filepath2}\"")
else:
    filepath = sys.argv[1]
    with open(init_.data_path, "w", encoding="utf-8") as f:
        f.writelines(["1\n", filepath])


