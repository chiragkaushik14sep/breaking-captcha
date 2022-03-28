import os
directory = r"C:\Users\Ckaushik\Downloads\\test\\test_1"


from os import walk

f = []
for (dirpath, dirnames, filenames) in walk(directory):
    f.extend(filenames)

    break

#print(type(f))
for i in range(len(f)):
    x = f[i].split(".")
    t = (x[-1])

    if t == "txt":
        print(t)
        os.remove(r"C:\Users\Ckaushik\Downloads\test\test_1\\"+f[i])