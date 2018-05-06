import os
import numpy as np
import math
from sklearn.decomposition import NMF

direct_in = "G:\\Text_Mining_Project_Test\\"#Clean
direct_out = "G:\\Text_Mining_Project_Test_out\\"#Save
direct_test = "G:\\Text_Mining_Project_Test\\"
direct_test_out = "G:\\Text_Mining_Project_Test_out\\"

terms = []
doc_count = []
store_terms = []
# List of lists. Every sublist corresponds to a unique document. The sublist contains all terms found in that
# corresponding document.
store_counts = []
# List of lists. Every sublist correspond to a unique document. The sublist contains the count for each corresponding
# term in store_terms, for the given document.
for filename in os.listdir(direct_in):
    if filename.endswith(".txt"):
        print(filename)
        update_terms = []
        update_counts = []
        f = open(direct_in + filename, "r", encoding="utf8")
        line = f.read()
        words = (line.split())
        for r in words:
            r = r.lower()
            if r in update_terms:
                ind = update_terms.index(r)
                update_counts[ind] += 1
            else:
                update_terms.append(r)
                update_counts.append(1)
        for i in update_terms:
            if i in terms:
                ind = terms.index(i)
                doc_count[ind] += 1
            else:
                terms.append(i)
                doc_count.append(1)
        store_terms.append(update_terms)
        store_counts.append(update_counts)

print(terms)
print(doc_count)
print(update_terms)
print(update_counts)

docs1 = ["terms.txt", "doc_count.txt"]
docs2 = ["store_counts.txt", "store_terms.txt"]
lists1 = [terms, doc_count]
lists2 = [store_counts, store_terms]

for i in range(len(docs1)):
    d = docs1[i]
    l = lists1[i]
    f = open(direct_out + d, 'w', encoding="utf8")
    for k in l:
        f.write(str(k) + '\n')
    f.close()

for i in range(len(docs2)):
    d = docs2[i]
    l = lists2[i]
    f = open(direct_out + d, "w", encoding="utf8")
    for k in l:
        s = ''
        for l in k:
            s = str(s) + str(l) + ', '
        f.write(str(s) +'\n')
    f.close()

print(len(store_terms), len(terms))
c_matrix = np.zeros([len(store_terms), len(terms)])
for i in range(len(store_terms)):
    print(i)
    for j in range(len(store_terms[i])):
        w = store_terms[i][j]
        ind = terms.index(w)
        tfidf = math.log(1 + store_counts[i][j]) * math.log(len(store_terms)/doc_count[j],10)
        c_matrix[i, ind] = tfidf
np.savetxt(direct_out + 'c_matrix.txt', c_matrix, fmt='%f',newline=',')

model = NMF(n_components=20, init='random', random_state=0)
W = model.fit_transform(c_matrix)
H = model.components_

print(W.shape)
print(H.shape)

np.savetxt(direct_out + 'W.txt', W, fmt='%f')
np.savetxt(direct_out + 'H.txt', H, fmt='%f')




