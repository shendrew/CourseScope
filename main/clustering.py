import json
import numpy as np
from text import process

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
from sklearn import preprocessing
from scipy.cluster.hierarchy import ward, fcluster


# with open("./data/data.json", "r") as data_file:
#     data = json.load(data_file)

with open("./data/labeled_data.json", "r") as data_file:
    data = json.load(data_file)

with open("./data/labels.json", "r") as label_file:
    labels = json.load(label_file)

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
    MAX_DIST = max(clusters[:, 2])*0.27     # cophenetic distance
    fclusters = fcluster(clusters, t=MAX_DIST, criterion="distance")
    
    # np.save("./data/clusters.npy", fclusters)


def saveLabels():
    clusters = np.load("./data/clusters.npy")
    for topic in range(max(clusters)):
        for i in range(len(clusters)):
            if (clusters[i] == topic):
                # use manually annotated group labels
                courses[i]["labels"] = labels[str(topic)]
                
                if (courses[i]["labels"]):
                    print(courses[i]["title"])
        print(topic, '-'*50)
    
    # save data
    courses_list = []
    for i in range(len(clusters)):
        courses_list.append(courses[i])
                
    # with open("./data/labeled_data.json", "w") as output_file:
    #     json.dump(courses_list, output_file, indent=4)
    
    print("***labels geneated***")
    
        
# cosCluster()
saveLabels()