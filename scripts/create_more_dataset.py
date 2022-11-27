import json
from pathlib import Path
from stopstem import *
import os
BASE_DIR = Path(__file__).resolve().parent.parent

path = "C://Users//ganes//Desktop//mini//jsons"
dir_list = os.listdir(path)

print(dir_list)
vocabulary = []
for i in dir_list:
    if i[-4::] == 'json':
        with open(BASE_DIR/("jsons/"+i)) as data_source:
            print(i)
            data1 = json.load(data_source)
            for i in data1:
                vocabulary.extend(data1[i]["reading"].keys())
                vocabulary.extend(data1[i]["videos"].keys())
#print(vocabulary)
arr = tokenizeAndStem(' '.join(vocabulary))
toStore = ','.join(arr)
with open("vocab.txt",'w') as f:
    f.write(toStore)