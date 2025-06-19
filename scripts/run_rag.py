# scripts/run_rag.py
from scripts.rag import load_vectorstore, setup_llm, create_rag_chain
import torch

def query_rag(qa_chain, question):
    # Get the response
    result = qa_chain.invoke({"query": question})
    
    # Print the answer and sources
    print("\nAnswer:", result["result"])
    print("\nSources:")
    for doc in result["source_documents"]:
        print(f"- {doc.metadata['source']} (Chunk {doc.metadata['chunk_id']})")

if __name__ == "__main__":
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA device count:", torch.cuda.device_count())
    print("Current CUDA device:", torch.cuda.current_device())
    print("CUDA device name:", torch.cuda.get_device_name(torch.cuda.current_device())) 
    
    # Load the vector store
    vs = load_vectorstore()
    
    # Setup the LLM
    llm = setup_llm()
    
    # Create the RAG chain
    qa_chain = create_rag_chain(vs, llm)
    
    # Example query
    question = "What are the key requirements for flight recording systems?"
    query_rag(qa_chain, question)
