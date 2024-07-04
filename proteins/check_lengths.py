file = open("domain_hits.fasta")

dict_lengths = dict()

for line in file:
    line = line.strip()
    if line[0] == ">":
        id = line[1:]
        dict_lengths[id] = 0
    else:
        dict_lengths[id] = len(line)

print(min(dict_lengths.values()))
print(max(dict_lengths.values()))
