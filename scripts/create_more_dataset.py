import json
from pathlib import Path
from stopstem import *
import os
BASE_DIR = Path(__file__).resolve().parent.parent

path = "C://Users//ganes//Desktop//mini//jsons"
dir_list = os.listdir(path)

print(dir_list)
vocab = ' '
for i in dir_list:
    if i[-4::] == 'json':
        with open(BASE_DIR/("jsons/"+i)) as data_source:
            vocabulary = []
            print(i)
            data1 = json.load(data_source)
            for j in data1:
                vocabulary.extend(data1[j]["reading"].keys())
                vocabulary.extend(data1[j]["videos"].keys())
            vocab += ' '.join(vocabulary) + ' '
            # print(vocab)
            # print(BASE_DIR/("reference/dataset_"+i[:-4]+'txt'))
            # with open(BASE_DIR/("reference/dataset_"+i[:-4]+'txt'),'w') as target:
            #     target.write(vocab)
with open(BASE_DIR/("reference/dataset__dataset.txt"),'w') as target:
    target.write(vocab)
#print(vocabulary)
