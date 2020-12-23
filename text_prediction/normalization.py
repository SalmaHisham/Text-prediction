import nltk
from nltk.corpus import stopwords
import string
import re
from nltk.book import *


def Normalize(txt):
    stopwords_list = stopwords.words('english')
    ftxt = str.lower(" ".join(txt))
    print("\n" + ftxt + "\n")
    ls = ftxt.split()
    pn = list(string.punctuation)
    flt = []
    for tok in ls:
        if tok not in stopwords_list:
            word = re.sub(r'([-[_\],!?():{}&$#@%*+;"\t\n\b])', r'', tok)
            if word != "":
                flt.append(word)

    t = " ".join(flt)
    sen = list(t.split("."))
    # print(sen)
    return sen


def NormalizeInput(txt):
    stopwords_list = stopwords.words('english')
    ftxt = str.lower("".join(txt))
    ls = ftxt.split()
    pn = list(string.punctuation)
    flt = []
    for tok in ls:
        if tok not in stopwords_list:
            word = re.sub(r'([-[_\],!?():{}&$#@%*+;"\t\n\b])', r'', tok)
            if word != "":
                flt.append(word)

    t = " ".join(flt)
    sen = list(t.split("."))
    # print(sen)
    return sen[0]
