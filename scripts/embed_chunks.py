# scripts/embed_chunks.py

from langchain_huggingface import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from langchain_community.vectorstores import FAISS
from pathlib import Path
import json
from tqdm import tqdm
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    # Use bge-m3 with appropriate prefix
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={"device": "cuda"},  
        encode_kwargs={"normalize_embeddings": True}
    )
    logger.info("Successfully loaded embedding model")
except Exception as e:
    logger.error(f"Failed to load embedding model: {e}")
    raise

chunk_dir = Path("data/chunks")
documents = []

try:
    # Get list of files first for progress bar
    files = list(chunk_dir.glob("*.json"))
    logger.info(f"Found {len(files)} JSON files to process")
    
    for file in tqdm(files, desc="Processing files"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                data = json.load(f)

            for i, chunk in enumerate(data["chunks"]):
                doc = Document(
                    page_content=f"Represent this sentence for retrieving relevant passages: {chunk}",
                    metadata={"source": data["source"], "chunk_id": i}
                )
                documents.append(doc)
        except Exception as e:
            logger.error(f"Error processing file {file}: {e}")
            continue

    logger.info(f"Loaded {len(documents)} chunks for embedding")

    # Build vector DB
    vectorstore = FAISS.from_documents(documents, embedding_model)
    
    # Create directory if it doesn't exist
    save_dir = Path("data/vectorstore/faiss_bge_m3_index")
    save_dir.parent.mkdir(parents=True, exist_ok=True)
    
    vectorstore.save_local(str(save_dir))
    logger.info("Vector store saved successfully")
    
except Exception as e:
    logger.error(f"An error occurred: {e}")
    raise