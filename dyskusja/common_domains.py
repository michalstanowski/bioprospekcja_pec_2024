mmseqs = {'PF17957': 43, 'PF16640': 26}
blastp = {'PF18884': 7, 'PF14200': 9}

from matplotlib import pyplot as plt


common_domains = set(mmseqs.keys()).intersection(set(blastp.keys()))

filtered_domains = {domain for domain in common_domains if mmseqs[domain] >= 3 or blastp[domain] >= 3}

filtered_mmseqs = {domain: mmseqs[domain] for domain in filtered_domains}
filtered_blastp = {domain: blastp[domain] for domain in filtered_domains}

sorted_domains = sorted(filtered_domains, key=lambda domain: filtered_mmseqs[domain] + filtered_blastp[domain], reverse=True)

top_domains = sorted_domains[:10]
mmseqs_values = [filtered_mmseqs[domain] for domain in top_domains]
blastp_values = [filtered_blastp[domain] for domain in top_domains]

fig, ax = plt.subplots(figsize=(12, 8))

bars1 = ax.bar(top_domains, mmseqs_values, label='MMseqs2', color='turquoise', edgecolor='black')
bars2 = ax.bar(top_domains, blastp_values, label='BLASTP', bottom=mmseqs_values, color='palevioletred', edgecolor='black')

ax.set_xlabel('Pfam ID domeny', fontsize=15)
ax.set_ylabel('Liczba sekwencji z daną domeną', fontsize=15)
ax.legend(fontsize=15)
ax.tick_params(axis='x', labelsize=15)
ax.tick_params(axis='y', labelsize=15)

for bar1, bar2, value1, value2 in zip(bars1, bars2, mmseqs_values, blastp_values):
    mmseqs_mid = value1 / 2
    blastp_mid = value2 / 2
    ax.text(bar1.get_x() + bar1.get_width() / 2, mmseqs_mid, str(value1),
            ha='center', va='center', fontsize=15, color='black')
    ax.text(bar2.get_x() + bar2.get_width() / 2, bar1.get_height() + blastp_mid, str(value2),
            ha='center', va='center', fontsize=15, color='black')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
