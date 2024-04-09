

import os

def searchFile(dirname, extension):
    filenames = os.listdir(dirname)
    for filename in filenames:
        filepath = os.path.join(dirname, filename)
        if os.path.isdir(filepath):
            searchFile(filepath, extension)
        elif os.path.isfile(filepath):
            name, ext = os.path.splitext(filepath)
            if ext == extension:
                with open(filepath, 'r', encoding='utf-8') as f:
                    print(f.read())

pwd = "c:/Projects/oz_coding/ozcodingschool_be_02_homework/za1___OperatingSystem/05_file"
searchFile(pwd, ".txt")