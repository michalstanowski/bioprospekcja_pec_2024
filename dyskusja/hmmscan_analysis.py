wyniki_scan_mmseqs = open(file="hmmscan_file")

dict_count = dict()

for line in wyniki_scan_mmseqs:
    line = line.strip()
    line = line.split()
    id_seq = line[1][:7]
    e_val = line[7]
    if id_seq == "PF00544":
        print(line[2])
    if id_seq not in dict_count:
        dict_count[id_seq] = 1
    else:
        dict_count[id_seq] += 1
        
print(dict_count)
