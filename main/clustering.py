import json
import numpy as np
from text import process

from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
from scipy.cluster.hierarchy import ward, dendrogram

import matplotlib.pyplot as plt

with open("./data/data.json", "r") as file:
    data = json.load(file)

title = {}

count = 0
raw_text=[]
for course in data:
    if (count == 376): break
    raw_text.append(process(course["description"]))
    title[count] = course["title"]
    count +=1

vectorizer = TfidfVectorizer(ngram_range=(1,2),
                             min_df=2,
                             max_df= 0.6,
                             stop_words="english",
                             )
matrix = vectorizer.fit_transform(raw_text)



def kCluster():
    kmeans = KMeans(n_clusters=60).fit(matrix)
    # label = kmeans.labels_

    my_dict = {i: np.where(kmeans.labels_ == i)[0] for i in range(kmeans.n_clusters)}

    for i in range(kmeans.n_clusters):
        for j in my_dict[i]:
            print(title[j])
        print("-"*60)


def cosCluster():
    dist = cosine_distances(matrix)
    clusters = ward(dist)
    
    print(clusters)
    



cosCluster()