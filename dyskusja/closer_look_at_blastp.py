homologicznie = ['s2_k127_834447_1', 's1_k127_455787_1', 's1_k127_3032933_1', 's3_k127_3669056_1', 's2_k127_614016_1', ...]

import subprocess

def run_grep_for_headers(headers, file_to_search, context_lines=20):
    for header in headers:
        try:
            result = subprocess.run(
                ['grep', '-i', header, '-A', str(context_lines), file_to_search],
                capture_output=True, text=True, check=True
            )
            print(f"Results for {header}:\n")
            print(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"No match found for {header}\n")

file_to_search = 'homology_out'

run_grep_for_headers(homologicznie, file_to_search)
