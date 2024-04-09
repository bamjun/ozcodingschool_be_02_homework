import os
import shutil

pwd = "c:\Projects\oz_coding\ozcodingschool_be_02_homework\za1___OperatingSystem\\05_file"

filenames = os.listdir(pwd)

for filename in filenames:
    if "toto" in filename:
        origin = os.path.join(pwd, filename)
        print(origin)

        # shutil.copy(origin, os.path.join(pwd, "copy.txt"))
        shutil.move(origin, os.path.join(pwd, "temp"))