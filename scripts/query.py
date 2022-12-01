from pprint import pprint as p
import json
from pathlib import Path
from stopstem import *
import os
from gensim.models import Word2Vec
import pickle
from cosines import cacCosine
import numpy as np
from tree import *
from spellcheck import SpellCheck

#print(model1.wv)
def correct(query):
    spell_check = SpellCheck('../scripts/words.txt')
    qlist = query.split()
    for i in range(len(qlist)):
        spell_check.check(qlist[i])
        qlist[i]=spell_check.correct()
    return " ".join(qlist)

def replace(query):
    replace_map = {
        "dict" : "dictionary"
    }
    qlist = query.split()
    for i in range(len(qlist)):
        if qlist[i] in replace_map:
            qlist[i]=replace_map[qlist[i]]
    return " ".join(qlist)
    
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


def path():
    try:
        path = os.listdir("C://Users//yatha//Desktop//minor//jsons")
    except:
        try:
            path = os.listdir("C://Users//ganes//Desktop//mini//jsons")
        except:
            path = os.listdir("C://Users//Shabdansh//OneDrive//Desktop//minor1//jsons")
    return path

def findSimilar(query,format,listOfDocs = path()):
    BASE_DIR = Path(os.getcwd()).resolve().parent
    with open('../scripts/model.dat','rb') as file:
        model1 = pickle.load(file)
    #dic={stemmdtitle:[title,link,file]}
    dic={}
    maxi=[]
    for i in listOfDocs:
        if i[-4::]=='json':
            with open(BASE_DIR/('jsons/'+i)) as f:
                data=json.load(f)
                for j in data:
                    if format == 'video':
                        for k in data[j]['videos'].keys():
                            tok = ' '.join(tokenizeAndStem(k))
                            dic[tok]=[k,data[j]['videos'][k],i]
                            maxi.append([sim(tok,' '.join(tokenizeAndStem(query)),model1),data[j]['videos'][k],k,j,i])
                    elif format == 'reading':
                        for k in data[j]['reading'].keys():
                            tok = ' '.join(tokenizeAndStem(k))
                            dic[tok]=[k,data[j]['reading'][k],i]
                            maxi.append([sim(tok,' '.join(tokenizeAndStem(query)),model1),data[j]['reading'][k],k,j,i])
                    else:
                        pass
    return dic,maxi

def answers(query,mode):
    dic,maxi = findSimilar(query,mode)
    answere = sorted(maxi,reverse=True)[0:8]
    result = []
    for i in answere:
        result.append({"url":i[1],
            "difficulty":i[3],
            "title":i[2]})

    return result,sorted(maxi,reverse=True)

def topSuggest(arr):
    try:
        count={}
        for i in arr:
            if i[-1] in count:
                count[i[-1]]+=1
            else:
                count[i[-1]]=1
        lst=[[count[i],i] for i in count]
        lst.sort()
        tree,nodes=load_tree('tree.dat')
        related=list(children(tree,nodes,lst[0][1][:-5:]))+list(siblings(tree,nodes,lst[0][1][:-5:]))+list(parents(tree,nodes,lst[0][1][:-5:]))
        return related
    except:
        return []

    
l = path()
q1 = "Python Program to Print Natural Numbers Using While and For Loop in Hindi - Tutorial #22"
q2 = "Print the first 10 natural numbers using for loop"
dic,maxi = findSimilar("sum of first few integers",l)
p(sorted(maxi,reverse=True))