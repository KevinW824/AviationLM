from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain.vectorstores import FAISS
from pathlib import Path
import json

# Use bge-m3 with appropriate prefix
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    encode_kwargs={"normalize_embeddings": True}
)

chunk_dir = Path("data/chunks")
documents = []

for file in chunk_dir.glob("*.json"):
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    for i, chunk in enumerate(data["chunks"]):
        doc = Document(
            page_content=f"Represent this sentence for retrieving relevant passages: {chunk}",
            metadata={"source": data["source"], "chunk_id": i}
        )
        documents.append(doc)

print(f"Loaded {len(documents)} chunks for embedding.")

# Build vector DB
vectorstore = FAISS.from_documents(documents, embedding_model)
vectorstore.save_local("data/vectorstore/faiss_bge_m3_index")
print("Vector store saved.")