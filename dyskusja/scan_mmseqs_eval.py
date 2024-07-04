file = open("scan_mmseqs_only")

dict_mmseqs = dict()
seqs = []
e_vals_05 = []
e_vals_13 = []
for line in file:
    line = line.split()
    idd = line[1][:7]
    seq = line[2]
    e_val = line[7]
    if idd == "PF00544":
        if float(e_val) < 10e-5:
            seqs.append(seq)
    elif idd == "PF13229":
        e_vals_13.append(float(e_val))

print(seqs)
print(sum(e_vals_13)/len(e_vals_13))
