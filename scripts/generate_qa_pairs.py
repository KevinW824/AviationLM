# scripts/generate_qa_pairs.py

from openai import OpenAI
import json
import random
from tqdm import tqdm
from pathlib import Path
import logging
import csv
import os

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize OpenAI client
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def call_llm(client: OpenAI, prompt: str):
    response = client.chat.completions.create(
        model="gpt-4o-mini", 
        messages=[
            {"role": "system", "content": "You are a helpful assistant that generates factoid questions and answers from given context."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256
    )
    return response.choices[0].message.content

def load_documents():
    """Load processed documents from the chunks directory."""
    chunk_dir = Path("data/chunks")
    documents = []
    
    for file_path in chunk_dir.glob("*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for chunk in data["chunks"]:
                    documents.append({
                        "page_content": chunk,
                        "metadata": {"source": data["source"]}
                    })
        except Exception as e:
            logger.error(f"Error loading file {file_path}: {e}")
            continue
    
    return documents

N_GENERATIONS = 100 
QA_generation_prompt = """
Your task is to write a factoid question and an answer given a context.
Your factoid question should be answerable with a specific piece of factual information from the context.
Your factoid question should be formulated in the same style as questions users could ask in a search engine.
This means that your factoid question MUST NOT mention something like "according to the passage" or "context".

Provide your answer as follows:

Output:::
Factoid question: (your factoid question)
Answer: (your answer to the factoid question)

Now here is the context.

Context: {context}\n
Output:::"""

def main():
    logger.info("Loading documents...")
    docs_processed = load_documents()
    logger.info(f"Loaded {len(docs_processed)} documents")

    logger.info(f"Generating {N_GENERATIONS} QA pairs...")
    outputs = []
    
    for sampled_context in tqdm(random.sample(docs_processed, N_GENERATIONS)):
        try:
            # Generate QA couple
            output_QA_couple = call_llm(client, QA_generation_prompt.format(context=sampled_context["page_content"]))
            
            question = output_QA_couple.split("Factoid question: ")[-1].split("Answer: ")[0].strip()
            answer = output_QA_couple.split("Answer: ")[-1].strip()
                
            outputs.append({
                "instruction": question,
                "reference_answer": answer,
                "sources": sampled_context["metadata"]["source"]
            })
        except Exception as e:
            logger.error(f"Error processing document: {e}")
            continue

    # Save the generated QA pairs to CSV
    output_path = Path("data/eval/qa.csv")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["instruction", "reference_answer", "sources"])
        writer.writeheader()
        writer.writerows(outputs)
    
    logger.info(f"Generated {len(outputs)} QA pairs and saved to {output_path}")

if __name__ == "__main__":
    main()