import re
homology_file = open(file="blastp_out")

query_regex = "Query=\s(.+)"
query = ""
findings = []

for line in homology_file:
    line = line.strip()
    if line[:6] == "Query=":
        match_query = re.match(query_regex, line).group(1)
    if line[:5] == "*****":
        match_query = ""
    if line[:9] == "Sequences":
        findings.append(match_query)

print(len(findings))
print(findings)
