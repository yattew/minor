import nltk

#nltk.download('stopwords') do for first run

import re                                  
import string                             

from nltk.corpus import stopwords          
from nltk.stem import PorterStemmer        
from nltk.tokenize import TweetTokenizer 
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

def tokenizeAndStem(sentence):
    clean_text = tokenize(sentence)
    asString,asArr = stem(clean_text)
    #return asString
    return list(set(asArr))
