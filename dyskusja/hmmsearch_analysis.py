import subprocess

ids = ['id_sekwencji']
def get_sequence_from_fasta(fasta_file, seq_id):
    command = f"grep -A 1 '>{seq_id}' {fasta_file}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    lines = result.stdout.strip().split('\n')
    if len(lines) < 2:
        return None 
    header = lines[0].strip()
    sequence = lines[1].strip()
    return header, sequence

fasta_file = "wszystkie_bialka.fasta"
output_file = "trafienia_hmmsearch_PF00544.fasta"
i = 0
sequences = []
for seq_id in ids:
    print(i)
    i+=1
    result = get_sequence_from_fasta(fasta_file, seq_id)
    if result:
        header, sequence = result
        sequences.append((header, sequence))
    else:
        print(f"ID: {seq_id} - Sequence not found")

with open(output_file, 'w') as f:
    for header, sequence in sequences:
        f.write(f"{header}\n")
        f.write(f"{sequence}\n")

print(f"Sequences saved to {output_file}")
