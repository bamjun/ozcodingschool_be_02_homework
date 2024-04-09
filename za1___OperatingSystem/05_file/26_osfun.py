import os

pwd = "c:/Projects/oz_coding/ozcodingschool_be_02_homework/za1___OperatingSystem/05_file"


filenames = os.listdir(pwd)
print(filenames)



print(os.path.isdir(filenames[0]))
print(os.path.isdir(pwd + "/temp"))

print(os.path.isfile(filenames[0]))
print(os.path.isfile(pwd + "/temp"))


filepath = pwd + "/" + filenames[0]
print(filepath)

name, ext = os.path.splitext(filepath)
print(name)

print(ext)