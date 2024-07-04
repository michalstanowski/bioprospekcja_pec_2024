from Bio import SeqIO

headers = []

duplicate_headers = []

fasta_files = ["trafienia_jedna_domena", "trafienia_druga_domena"]

for fasta_file in fasta_files:
    with open(fasta_file, "r") as f:
        for seq_record in SeqIO.parse(f, "fasta"):
            header = seq_record.description
            headers.append(header)
            if headers.count(header) > 1:
                duplicate_headers.append(header)

if duplicate_headers:
    print("Powtarzające się nagłówki sekwencji:")
    for header in set(duplicate_headers):
        print(header)
else:
    print("Brak powtarzających się nagłówków sekwencji.")
