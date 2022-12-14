import pandas as pd
import string
import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# import seaborn as sns
import re
import string
import nltk 
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.pipeline import Pipeline
import spacy
from collections import Counter
# nlp = spacy.load('en_core_web_sm')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
from numpy import asarray
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_absolute_error as mae
from sklearn.metrics import mean_absolute_percentage_error as mape
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from nltk.corpus.reader.wordnet import WordNetError
import sys
import time
import threading

def preprocessing(document_1, document_2):
    pattern = r'[' + string.punctuation + ']'
    punct1=re.sub(pattern," ",str(document_1))
    punct2=re.sub(pattern," ",str(document_2))

    casefold1 = punct1.lower()
    casefold2 = punct2.lower()

    token1 = casefold1.split()
    token2 = casefold2.split()

    sw=nltk.corpus.stopwords.words('english')

    list_stopwords = set(stopwords.words('english'))
    stop1 = [word for word in token1 if not word in list_stopwords]
    stop2 = [word for word in token2 if not word in list_stopwords]

    ps = PorterStemmer()

    stem1 = []
    for word in stop1:
        stem1.append(ps.stem(word))
    
    join1 = " ".join(stem1)

    stem2 = []
    for word in stop2:
        stem2.append(ps.stem(word))
    
    join2 = " ".join(stem2)
    data = [join1, join2]
    
    return data