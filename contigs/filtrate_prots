import gzip
from Bio import SeqIO

paths = ["srodowisko1", "srodowisko2", ...]


file = open("wszystkie_ramki", "w")

for path in paths:
    s = path[8]
    print(s)
    with gzip.open(path, 'rt') as handle:
        for r in SeqIO.parse(handle, 'genbank'):
            for feature in r.features:
                if feature.type == 'CDS':
                    prot_id = feature.qualifiers["protein_id"][0]
                    translation = feature.qualifiers["translation"][0]
                    if len(translation) < 1100 and len(translation) > 250:
                        file.write(f">s{s}_{prot_id}\n")
                        file.write(translation + "\n")
            
