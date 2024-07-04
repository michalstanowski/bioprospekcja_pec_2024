import matplotlib.pyplot as plt

domains = open("out_interpro.tsv")


dict_count = dict()

for line in domains:
    line = line.strip().split("\t")
    if line[3] == "Pfam":
        if line[4] not in dict_count:
            dict_count[line[4]] = 0
        dict_count[line[4]] += 1


labels = list(dict_count.keys())
values = list(dict_count.values())

fig, ax = plt.subplots(figsize=(16, 12))

bars = ax.bar(labels, values, color='lightblue', edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval + 1, int(yval), ha='center', va='bottom')

plt.xlabel('Pfam ID domeny')
plt.ylabel('Liczba wystąpień w sekwencjach referencyjnychv UniProt')

plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("count_domains.png")
