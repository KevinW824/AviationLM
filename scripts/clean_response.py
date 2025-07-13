# scripts/clean_responses.py

import csv
import re
from pathlib import Path

def extract_response(text):
    """Extract the actual response from the model output by removing instruction tokens"""
    match = re.search(r'\[/INST\]</s>(.*)', text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return text.strip()

def clean_csv(infile, outfile):
    with open(infile, newline='', encoding='utf-8') as f_in, \
         open(outfile, 'w', newline='', encoding='utf-8') as f_out:
        reader = csv.DictReader(f_in)
        fieldnames = [fn for fn in reader.fieldnames if fn != "processing_time"]
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        for row in reader:
            if "response" in row and row["response"]:
                row["response"] = extract_response(row["response"])
            row = {k: v for k, v in row.items() if k != "processing_time"}
            writer.writerow(row)
    print(f"Cleaned responses saved to {outfile}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python scripts/clean_responses.py input.csv output.csv")
    else:
        clean_csv(sys.argv[1], sys.argv[2])