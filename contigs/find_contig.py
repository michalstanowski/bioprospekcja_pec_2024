import gzip
from Bio import SeqIO

paths = ["srodowisko1", "srodowisko2", ...]

fasta_in = open("proteins", "r")

fasta_out = open("on_which_contig_are_they_located", "w")


for line in fasta_in:
    line = line.strip()
    if line[0] == ">":
        index = int(line[2])
        print(index)
    else:
        provided_sequence = line
        sequence_found = False
        with gzip.open(paths[index-1], 'rt') as handle:
            for record in SeqIO.parse(handle, 'genbank'):
                for feature in record.features:
                    if feature.type == "CDS" and "translation" in feature.qualifiers:
                        translation = feature.qualifiers["translation"][0]
                        if provided_sequence in translation:
                            contig_id = record.id
                            contig_sequence = record.seq
                            fasta_out.write(">s" + str(index) + str(contig_id) + "\n")
                            fasta_out.write(str(contig_sequence) + "\n")
                            sequence_found = True
                            break
                if sequence_found:
                    break

        if not sequence_found:
            print("Sequence not found in any contig.")
