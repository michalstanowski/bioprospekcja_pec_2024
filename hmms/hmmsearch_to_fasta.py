from Bio import SearchIO
from Bio import SeqIO

result_file = "hmmsearch_file"

hmmer_results = SearchIO.parse(result_file, "hmmer3-text")

sequences_dict = SeqIO.to_dict(SeqIO.parse("all_prots.fasta", "fasta"))

significant_hits = open("new_file.fasta", "w")

for result in hmmer_results:
    for hit in result.hits:
        if hit.evalue < 1e-5:
            significant_hits.write(">" + hit.id + "\n")
            significant_hits.write(str(sequences_dict.get(hit.id, None).seq) + "\n")
