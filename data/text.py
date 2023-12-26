import re
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def to_lower(text):
    return text.lower()

def remove_numbers(text):
    return re.sub(r"\d+", "", text)

def remove_punctuation(text):
    translator = str.maketrans(string.punctuation, " "*len(string.punctuation))
    return text.translate(translator)

def remove_urls(text):
    return re.sub(r"https?://\S+|www\.\S+", "", text)

def remove_stopwords(tokens):
    stop_words = set(stopwords.words("english"))
    
    result = []
    for token in tokens:
        if (token not in stop_words) and (len(token) > 1):
            result.append(token)
    return result

def lemmatize(tokens):
    wnl = WordNetLemmatizer()
    
    result = []
    for token in tokens:
        result.append(wnl.lemmatize(token))
    return result

def process(text):
    new_text = to_lower(text)
    new_text = remove_urls(new_text)
    new_text = remove_numbers(new_text)
    new_text = remove_punctuation(new_text)
    
    tokens = word_tokenize(new_text)
    tokens = remove_stopwords(tokens)
    tokens = lemmatize(tokens)
    
    return tokens
