import matplotlib.pyplot as plt

file = open('hits_PF00544.fasta')

lengths = []

length = 0

for line in file:
    line = line.strip()
    if line[0] != ">":
        length += len(line)
    else:
        if length > 0:
            lengths.append(length)
        length = 0

print(len(lengths))

plt.hist(lengths, bins=77, color='blue', edgecolor='black')
plt.xlabel('Długość sekwencji [aa]')
plt.ylabel('Liczba sekwencji')

counts, bins, _ = plt.hist(lengths, bins=77)
for i, value in enumerate(counts):
    if value > 0:
        plt.text(bins[i] + (bins[1] - bins[0]) / 2, value, str(int(value)), ha='center', va='bottom')

for i in range(len(bins) - 1):
    plt.vlines(x=bins[i], ymin=0, ymax=counts[i], color='black', linestyle='-')

plt.axvline(x=200, color='red', linestyle='--')
plt.axvline(x=600, color='red', linestyle='--')

plt.show()
