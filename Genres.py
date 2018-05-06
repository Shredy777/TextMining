import numpy as np
import copy

direct_out = "G:\\Text_Mining_Project_Save\\"
file1 = "W.txt"
file2 = "H.txt"
file_terms="terms.txt"

f = open(direct_out+file_terms,"r",encoding="utf8")
terms = f.read()
f = terms.split()

W = np.loadtxt(direct_out + file1, delimiter=' ', usecols=range(20))
H = np.loadtxt(direct_out + file2, delimiter=' ', usecols=range(len(f)))
p = []
t = []
print(W.shape)

for i in range(20):
    x = [float(i) for i in (copy.deepcopy((W[:,i].T).tolist()))]
    y = sorted(x, reverse = True)
    z = copy.deepcopy(y[0:10])
    for j in z:
        t.append(x.index(j))
    p.append(t)
    t=[]

print(p)



    #print(y[0])




    #listwords = W[:,i].tolist()
    #ranked_list=listwords.sort()
    #print (listwords)
    #for j in [ranked_list[0:10]]:
    #   print( listwords.index(j))




