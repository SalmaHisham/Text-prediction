from pre_processing import *

def nextWord(txt):
    lastword = txt.split()[-1:]
    lst = []
    for i in biigram:
        firstWord = i.split(' ', 1)[0]
        if lastword[0] == firstWord:
            second = i.split(' ', 1)[1]
            lst.append((second, corpora[i]))
    if len(lst) == 0:
        return " "
    else:
        sorted_by_wight = sorted(lst, key=lambda tup: tup[1])
        return sorted_by_wight


if __name__ == "__main__":
    bigram()
    mytext = "glad it worked out my chair is too"
    afterNorm = NormalizeInput(mytext)
    ans = nextWord(afterNorm)[-1][0]
    print(mytext + "\n" + ans)
