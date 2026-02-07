import os
import sys
import time
import init_

def check(file_path1, file_path2):
    with os.popen(f"certutil -hashfile \"{file_path1}\" SHA256") as out_:
        f1sha256 = out_.read().splitlines()[1]
    with os.popen(f"certutil -hashfile \"{file_path1}\" SHA512") as out_:
        f1sha512 = out_.read().splitlines()[1]
    with os.popen(f"certutil -hashfile \"{file_path1}\" MD5") as out_:
        f1md5 = out_.read().splitlines()[1]
    with os.popen(f"certutil -hashfile \"{file_path2}\" SHA256") as out_:
        f2sha256 = out_.read().splitlines()[1]
    with os.popen(f"certutil -hashfile \"{file_path2}\" SHA512") as out_:
        f2sha512 = out_.read().splitlines()[1]
    with os.popen(f"certutil -hashfile \"{file_path2}\" MD5") as out_:
        f2md5 = out_.read().splitlines()[1]
    if f1sha256 == f2sha256 and f1sha512 == f2sha512 and f1md5 == f2md5:
        print("文件校验成功！")
    else:
        print("文件校验失败！")
        print(f"file: \t{file_path1}")
        print(f"\tMD5: \t{f1md5}")
        print(f"\tSHA256: \t{f1sha256}")
        print(f"\tSHA512: \t{f1sha512}")
        print()
        print(f"file: \t{file_path2}")
        print(f"\tMD5: \t{f2md5}")
        print(f"\tSHA256: \t{f2sha256}")
        print(f"\tSHA512: \t{f2sha512}")
    time.sleep(1)
    init_.init_config()
    input()


check(sys.argv[1], sys.argv[2])