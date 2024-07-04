# z tego podejścia zrezygnowano na rzecz klastrowania seaborn.clustermap

import matplotlib.pyplot as plt

clusters_output = open("clustering.tsv")
added = []
clusters = dict()

for line in clusters_output:
    line = tuple(line.strip().split("\t"))
    if line[0] in added:
        clusters[line[0]].append(line[1])
    elif line[1] in added:
        clusters[line[1]].append(line[0])
    else:
        added.append(line[0])
        clusters[line[0]] = [line[0], line[1]]
                
for cluster in clusters:
    if len(clusters[cluster]) >= 3:
        print(clusters[cluster])
