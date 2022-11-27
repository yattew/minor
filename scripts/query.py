from pprint import pprint as p
import json
from pathlib import Path
from stopstem import *
import os
from gensim.models import Word2Vec
import pickle
from cosines import cacCosine
import numpy as np

#print(model1.wv)
def sim(q1,q2,model1):
    a1 = q1.split()
    v1 = np.array([0.0]*100)
    v2 = np.array([0.0]*100)
    c1=1
    for i in a1:
        try:
            v1+=model1.wv[i]
            c1+=1
        except:
            pass
    v1/=c1
    a2 = q2.split()
    c2=1
    for i in a2:
        try:
            v2+=model1.wv[i]
            c2+=1
        except:
            pass
    v2/=c2
    return cacCosine(list(v1),list(v2))



def findSimilar(query,listOfDocs = os.listdir("C://Users//ganes//Desktop//mini//jsons")):
    BASE_DIR = Path(os.getcwd()).resolve().parent
    with open('model.dat','rb') as file:
        model1 = pickle.load(file)
    #dic={stemmdtitle:[title,link,file]}
    dic={}
    maxi=[]
    for i in listOfDocs:
        if i[-4::]=='json':
            with open(BASE_DIR/('jsons/'+i)) as f:
                data=json.load(f)
                for j in data:
                    for k in data[j]['videos'].keys():
                        tok = ' '.join(tokenizeAndStem(k))
                        dic[tok]=[k,data[j]['videos'][k],i]
                        maxi.append([sim(tok,' '.join(tokenizeAndStem(query)),model1),k,i])
                    for k in data[j]['reading'].keys():
                        tok = ' '.join(tokenizeAndStem(k))
                        dic[tok]=[k,data[j]['reading'][k],i]
                        maxi.append([sim(tok,' '.join(tokenizeAndStem(query)),model1),k,i])
    return dic,maxi

l = os.listdir("C://Users//ganes//Desktop//mini//jsons")
q1 = "Python Program to Print Natural Numbers Using While and For Loop in Hindi - Tutorial #22"
q2 = "Print the first 10 natural numbers using for loop"
dic,maxi = findSimilar("sum of first few integers",l)
p(sorted(maxi,reverse=True))