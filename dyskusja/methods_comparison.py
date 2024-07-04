from Bio import SeqIO

blastp = ['s1_k127_1959926_1', 's1_k127_1651975_1', 's3_k127_4405565_1', 's3_k127_1576566_1', ...]

mmseqs = ['s3_k127_3972495_6', 's3_k127_4021500_1', 's3_k127_3972495_4', 's2_k127_942250_1', ...]

mmseqs_set = set(mmseqs)

def extract_fasta_headers(file_path):
    headers = []
    for record in SeqIO.parse(file_path, "fasta"):
        headers.append(record.id)
    return headers

domains = extract_fasta_headers("domains.fasta")

blastp_set = set(findings)
domains_set = set(domains)

blastp_bez_domen = blastp_set - domains_set

domeny_bez_blastp = domains_set - blastp_set

intersected_blastp_domains = blastp_set & domains_set

unique_mmseqs = mmseqs_set - blastp_set - domains_set

unique_blastp = blastp_set - mmseqs_set - domains_set

intersected_bm = mmseqs_set & blastp_set

print(len(unique_mmseqs), len(unique_blastp), len(intersected_bm))
