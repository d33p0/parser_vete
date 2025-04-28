import pandas as pd
import re

# --- red file txt dulu---
with open('data_domain.txt', 'r') as file:
    raw_data = file.read()

# --- baris perbasiss ---
lines = raw_data.strip().split('\n')
parsed_data = []

for line in lines:
    match = re.match(
        r"Domain:\s(.+?),\sCountry:\s(.+?),\sLast Analysis Results Count:\s(\d+),\sMalicious Count:\s(\d+),\sTotal Engines:\s(\d+),\sReputation Score:\s(\d+/\d+)",
        line
    )
    if match:
        domain, country, last_count, malicious_count, total_engines, reputation = match.groups()
        parsed_data.append({
            "Domain": domain,
            "Country": country,
            "Last Analysis Results Count": int(last_count),
            "Malicious Count": int(malicious_count),
            "Total Engines": int(total_engines),
            "Reputation Score": reputation
        })

# --- SIMPAN KE EXCEL ---
df = pd.DataFrame(parsed_data)
output_file = "parsed_domains28.xlsx"
df.to_excel(output_file, index=False)

print(f"Data berhasil disimpan ke '{output_file}'")
