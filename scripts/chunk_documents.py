# scripts/chunk_documents.py

from langchain.text_splitter import RecursiveCharacterTextSplitter
from pathlib import Path
import json

input_dir = Path("data/processed/input_md")
output_dir = Path("data/chunks")
output_dir.mkdir(parents=True, exist_ok=True)

splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)

for file_path in input_dir.glob("*.md"):  # You can also use *.txt if needed
    with open(file_path, "r", encoding="utf-8") as f:
        full_text = f.read()

    chunks = splitter.split_text(full_text)

    out_data = {
        "source": file_path.name,
        "chunks": chunks
    }

    out_path = output_dir / f"{file_path.stem}.json"
    with open(out_path, "w", encoding="utf-8") as out_f:
        json.dump(out_data, out_f, indent=2, ensure_ascii=False)

    print(f"Chunked {file_path.name} into {len(chunks)} chunks")
