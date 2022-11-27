
from stopstem import *
def cacCosine(arr1,arr2):
    dot = 0
    mag1 = 0
    mag2 = 0
    for i in range(len(arr1)):
        dot += arr1[i]*arr2[i]
        mag1 += arr1[i]**2
        mag2 += arr2[i]**2
    mag1 = mag1**(1/2)
    mag2 = mag2**(1/2)
    return dot/(mag1*mag2)


def cosine(string1,string2):
    vocab = []
    vocabDict = {}
    with open("vocab.txt" ,'r') as f:
        vocab = f.read().split(',')
        for i in range(len(vocab)):
            vocabDict[vocab[i]] = i
    str1Arr = tokenizeAndStem(string1)
    str2Arr = tokenizeAndStem(string2)
    oneHot1 = [0]*len(vocab)
    oneHot2 = [0]*len(vocab)
    for i in str1Arr:
        if i in vocabDict:
            oneHot1[vocabDict[i]]+=1
    for i in str2Arr:
        if i in vocabDict:
            oneHot2[vocabDict[i]]+=1
    result = cacCosine(oneHot1,oneHot2)
    return result


