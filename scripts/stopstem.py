import nltk
#nltk.download('stopwords') do for first run
import re                                  
import string                             
from nltk.corpus import stopwords          
from nltk.stem import PorterStemmer        
from nltk.tokenize import TweetTokenizer 
from pathlib import Path
import json

BASE_DIR = Path(__file__).resolve().parent


def tokenize(sentence):
    tokenizer = TweetTokenizer(preserve_case=False, strip_handles=True,
                                   reduce_len=True)
    sentence_tokens = tokenizer.tokenize(sentence)


    stopwords_english = stopwords.words('english')

    clean_text = []

    for word in sentence_tokens: # Go through every word in your tokens list
        if (word not in stopwords_english and  # remove stopwords
            word not in string.punctuation):  # remove punctuation
            clean_text.append(word) 

    return clean_text

def stem(clean_text):
    stemmer = PorterStemmer()
    text_stem = []

    for word in clean_text:
            stem_word = stemmer.stem(word)
            text_stem.append(stem_word)
    return ' '.join(text_stem),text_stem

def removeInts(sentence):
    return re.sub(r'[0-9]+', "int", sentence)
    senArr = sentence.split()
    for i in range(len(senArr)):
        try:
            int(arr[i])
            arr[i] = 'int'
        except:
            pass
    return ' '.join(senArr)

def leastForm(sentence):
    reduce ={}
    with open(BASE_DIR/'reduce.json') as f:
        reduce = json.load(f)
    senArr = sentence.split()
    for i in range(len(senArr)):
        try:
            int(arr[i])
            arr[i] = 'int'
        except:
            pass
    return ' '.join(senArr)

def tokenizeAndStem(sentence):
    sentence = removeInts(sentence)
    #reduced = leastForm(sentence)
    clean_text = tokenize(sentence)
    asString,asArr = stem(clean_text)
    #return asString
    return list(set(asArr))

