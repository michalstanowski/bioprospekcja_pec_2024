# nieuwzględnione w pracy

import csv
search_output = open("pdb_analysis.tsv")

pdb_output = csv.writer(open("pdb_significant_hits.csv", "w"))

checked = set()

dict_pdb = dict()

for line in search_output:
    line = line.strip().split("\t")
    if line[0] not in checked and float(line[10]) < 0.05:
        pdb_output.writerow([line[0], line[1], line[-1]])
    checked.add(line[0])
