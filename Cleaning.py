import os
import re
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

direct_in = "G:\\Text_Mining_Project\\"
direct_out = "G:\\Text_Mining_Project_Clean\\"

# stop_words = ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out',
#              'very', 'having', 'with', 'they', 'own', 'an', 'be', 'some', 'for', 'do', 'its', 'yours', 'such', 'into',
#              'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from', 'him', 'each', 'the',
#              'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more',
#              'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no',
#              'when', 'at', 'any', 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because' ,
#              'what', 'over', 'why', 'so', 'can', 'did', 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which',
#              'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']
stop_words = set(stopwords.words('english'))
spec_char = []
PS = PorterStemmer()
LEM = WordNetLemmatizer()
punct_list = [i for i in punctuation]
punct_list.append("n't")
punct_list.append("--")
punct_list.append("...")
punct_list.append("``")
punct_list.append("''")
for filename in os.listdir(direct_in):
    if filename.endswith(".txt"):
        print(filename)
        f = open(direct_in + filename, "r", encoding="utf8")
        line = f.read()
        words = word_tokenize(line)
        f.close()
        appendFile = open(direct_out + filename, 'w', encoding="utf8")
        for r in words:
            r = LEM.lemmatize(r)
            r = PS.stem(r)
            if [s for s in r if s.isdigit()]:
                continue
            if not r.lower() in stop_words and not r.lower() in punct_list:
                if r.startswith("'"):
                    appendFile.write(r)
                else:
                    appendFile.write(" " + r)
        appendFile.close()