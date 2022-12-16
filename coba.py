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
from plagiarism_detection import preprocessing

def plagiarism_checker(document_1, document_2):
    copydata = preprocessing(document_1, document_2)
    # copydata = [document_1, document_2]
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix = tfidf_vectorizer.fit_transform(copydata)
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    cos_sim = float(cosine_sim[0][1])*100
    # str(round(x*100)) + '%'
    result = (f"Your text is {str(round(cos_sim))}% plagiarized")

    return result