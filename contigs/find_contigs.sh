#!/bin/bash

awk '/^>/ {print substr($0, 2)}' profiles_found.fasta | while read -r sequence_id; do
    protein_letter=$(echo "$sequence_id" | cut -c 2)
    contig_file="${protein_letter}.gbk.gz"
    echo "Szukanie kontigów dla sekwencji: $sequence_id w pliku: $contig_file"
    zcat "$contig_file" | zgrep -E -A1 "^>.*${sequence_id}" | grep -v "^--$"
    zcat "$contig_file" | zgrep -E -A1 "^>.*${sequence_id}" | grep -v "^--$" >> contigs.fasta
done

echo "Znalezione contigi zostały zapisane do pliku contigs_cellulase.fasta"
