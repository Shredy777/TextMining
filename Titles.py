import os
import copy

stopw = ['The', 'A']
s = " "
direct_in = "G:\\Text_Mining_Project\\"
direct_out = "G:\\Text_Mining_Project_Save\\"
filename = "Titles.txt"

file = open(direct_out + filename, "w", encoding="utf8")
for filename in os.listdir(direct_in):
    f = filename.split('_')
    f.remove('Script')
    t = f[len(f)-1].split('.')
    t.remove('txt')
    f[len(f)-1] = t[0]
    if f[len(f)-1] in stopw:
        f.insert(0, copy.deepcopy(f[len(f)-1]))
        del f[len(f)-1]
    f = s.join(f)
    file.write(f + '\n')
    print(f)
