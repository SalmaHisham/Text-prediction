import nltk
from nltk.util import ngrams
from sklearn.feature_extraction.text import CountVectorizer
from nltk.collocations import *
from nltk.book import *
from normalization import *

text = Normalize(text5)

def extract_gram(data, num):
    data = " ".join(data)
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [" ".join(grams) for grams in n_grams]


def Count(pairs):
    fd = nltk.FreqDist(pairs)
    return fd


unigramDic = Count(extract_gram(text, 1))
bigramDic = Count(extract_gram(text, 2))
biigram = list(bigramDic.keys())
corpora = {}
vocabulary = len(unigramDic)


def bigram():
    for i in biigram:
        secword = i.split(' ', 1)[0]
        corpora[i] = (bigramDic[i] + 1) / (unigramDic[secword] + vocabulary)
