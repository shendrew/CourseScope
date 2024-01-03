import json
import numpy as np
import pickle
from text import process

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
from sklearn import preprocessing
from scipy.cluster.hierarchy import ward, fcluster


with open("./data/data.json", "r") as file:
    data = json.load(file)

# text preprocessing
courses={}
raw_text=[]
for course_i in range(len(data)):
    raw_text.append(process(data[course_i]["description"]+data[course_i]["title"]))
    courses[course_i] = data[course_i]

# vectorize
vectorizer = TfidfVectorizer(ngram_range=(3,5),
                        min_df=2,
                        max_df= 0.6,
                        analyzer="char_wb"
                        )
matrix = vectorizer.fit_transform(raw_text)


def cosCluster():
    dist = cosine_distances(matrix)
    clusters = ward(dist)
    print(clusters)
    MAX_DIST = max(clusters[:, 2])*0.28     # cophenetic distance
    fclusters = fcluster(clusters, t=MAX_DIST, criterion="distance")
        
    for topic in range(max(fclusters)):
        for i in range(len(fclusters)):
            if (fclusters[i] == topic):
                print(courses[i]["title"])
        print(topic, '-'*60)
    
cosCluster()