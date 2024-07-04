seqs = open("prots.fasta")

with open("prots_cutoff.fasta", "w") as file:
    for line in seqs:
        line = line.strip()
        if line[0] == ">":
            header = line
        else:
            if len(line) > 200 and len(line) < 600:
                file.write(header + "\n")
                file.write(line + "\n")
            else:
                continue
