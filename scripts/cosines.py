from stopstem import *
def cosine(string1,string2):
    vocab=[]
    with open("vocab.txt" ,'r') as f:
        vocab = f.read().split(',')