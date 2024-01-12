
"""cosine clustering"""
# dist = cosine_distances(matrix)    # dist = 1 - cos_similarity (all pairs)
    
# tree = ward(dist)                   # recursively clusters closest pairs
# MAX_DIST = max(tree[:,2]) * 0.30        # cophenetic distance
# clusters = fcluster(tree, criterion="distance", t=MAX_DIST)

# topics = {i: np.where(clusters == i)[0] for i in range(max(clusters))}

# for topic in topics:
#     for i in topics[topic]:
#         print(title[i])
#     print("-"*60)



"""graph part"""
# MAX_COPHENETIC_DIST = max(tree[:,2]) * 0.35 # max distance between points to be considered together. can be tuned.

# MAX_TITLE_LEN = 15

# fig, ax = plt.subplots(figsize=(15, 80)) # set size
# ax = dendrogram(tree, orientation="right", color_threshold=MAX_COPHENETIC_DIST, leaf_font_size=4,
#                 # labels=data.title.apply(lambda x: x if len(x) < MAX_TITLE_LEN else x[:MAX_TITLE_LEN  - 3] + "...").tolist())
#                 labels=list(map(lambda x: x if len(x) < MAX_TITLE_LEN else x[:MAX_TITLE_LEN  - 3] + "...", list(title.values())))
#                 )

# plt.tick_params(axis= 'x', which='both',  bottom='off', top='off',labelbottom='off')

# plt.tight_layout() #show plot with tight layout
# plt.savefig('clusters_all.png', dpi=300)