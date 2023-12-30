import re
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.stem import SnowballStemmer

def to_lower(text):
    return text.lower()

def remove_numbers(text):
    return re.sub(r"\d+", "", text)

def remove_punctuation(text):
    return re.sub(r"[^\w\s]", "", text)

def remove_urls(text):
    return re.sub(r"https?://\S+|www\.\S+", "", text)

def remove_letters(tokens):    
    result = []
    for token in tokens:
        if (len(token) > 1):
            result.append(token)
    return result

def lemmatize(tokens):
    wnl = WordNetLemmatizer()
    stemmer = SnowballStemmer(language="english")
    
    result = []
    for token in tokens:
        new_token = wnl.lemmatize(token)
        # new_token = stemmer.stem(new_token)
        
        result.append(new_token)
    return result

def token2doc(tokens):
    doc = ""
    
    for token in tokens:
        doc += token + " "
    return doc

def process(text):
    new_text = to_lower(text)
    new_text = remove_urls(new_text)
    new_text = remove_numbers(new_text)
    new_text = remove_punctuation(new_text)
    
    tokens = word_tokenize(new_text)
    tokens = lemmatize(tokens)
    tokens = remove_letters(tokens)
    
    return token2doc(tokens)

# text = "computer compute computing computation computations"

# print(process(text))