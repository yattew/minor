from build_vocab import *
from stopstem import *
def cosine(string1,string2):
    vocab = []
    vocabDict = {}
    with open("vocab.txt" ,'r') as f:
        vocab = f.read().split(',')
        for i in range(len(vocab)):
            vocabDict[vocab[i]] = i
    str1Arr = tokenizeAndStem(string1)
    str2Arr = tokenizeAndStem(string2)
    embed1 = [0]*len(vocab)
    embed2 = [0]*len(vocab)
    for i in range(str1Arr):
