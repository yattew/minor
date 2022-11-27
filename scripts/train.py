import json
from pathlib import Path
import gensim
from gensim.models import Word2Vec
BASE_DIR = Path(__file__).resolve().parent.parent
from stopstem import *

f = open(BASE_DIR/'jsons/array.json')
  

data = json.load(f)
strung=[]
for i in data:
    strung.extend(data[i]["reading"].keys())
    strung.extend(data[i]["videos"].keys())
actual = list(map(tokenizeAndStem,strung))
#print(actual)
data = actual
model1 = Word2Vec(data, min_count = 1, window = 5, sg=0) 

print(model1.wv.similarity('program to reverse an array',"program to print an array"))
#model2 = gensim.models.Word2Vec(data, min_count = 1, size = 100, window = 5, sg = 1)
model1.wv.