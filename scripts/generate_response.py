# scripts/generate_response.py

import csv
import time
from pathlib import Path
from tqdm import tqdm
from scripts.rag import load_vectorstore, setup_llm, create_rag_chain

def main(
    infile: Path = Path("data/eval/qa.csv"),
    outfile: Path = Path("data/eval/qa_with_responses.csv"),
):
    """
    Generate responses for questions using RAG (Retrieval-Augmented Generation).
    
    This script processes questions from a CSV file and generates responses using
    a RAG chain. It includes progress tracking, error handling, and timing information.
    
    Args:
        infile (Path): Input CSV file containing questions (default: data/eval/qa.csv)
        outfile (Path): Output CSV file for responses (default: data/eval/qa_with_responses.csv)
    
    Features:
        - Progress bar with real-time updates
        - Processing time tracking for each question
        - Error handling with graceful continuation
        - Success rate statistics
        - Immediate file writing to prevent data loss
    
    Example:
        # Process all questions
        python scripts/generate_response.py
        
        # Process with custom files
        from scripts.generate_response import main
        main(
            infile=Path("my_questions.csv"),
            outfile=Path("my_responses.csv")
        )
    """
    # 1) Boot rag chain
    vs      = load_vectorstore()
    llm     = setup_llm()
    qa_chain = create_rag_chain(vs, llm)

    # 2) Read input file and count total questions
    with infile.open(newline="", encoding="utf-8") as f_in:
        reader = csv.DictReader(f_in)
        all_rows = list(reader)
        total_questions = len(all_rows)
    
    print(f"📊 Found {total_questions} questions to process")

    # 3) Process questions with progress tracking
    fieldnames = list(all_rows[0].keys()) + ["response", "response_sources", "processing_time"]
    
    with outfile.open("w", newline="", encoding="utf-8") as f_out:
        writer = csv.DictWriter(f_out, fieldnames=fieldnames)
        writer.writeheader()
        
        with tqdm(all_rows, desc="Processing questions", unit="q") as pbar:
            for row in pbar:
                question = row["instruction"]
                
                # Update progress bar description
                pbar.set_description(f"Processing: {question[:50]}...")
                
                try:
                    # Time the processing
                    start_time = time.time()
                    
                    # Invoke RAG chain
                    result = qa_chain.invoke({"query": question})
                    
                    # Calculate processing time
                    processing_time = time.time() - start_time
                    
                    # Update row with results
                    row["response"] = result["result"].replace("\n", " ").strip()
                    sources = [doc.metadata["source"] for doc in result["source_documents"]]
                    row["response_sources"] = "; ".join(sources)
                    row["processing_time"] = f"{processing_time:.2f}s"
                    
                    # Write immediately to avoid losing progress
                    writer.writerow(row)
                    f_out.flush()  # Ensure data is written to disk
                    
                    # Update progress bar with timing info
                    pbar.set_postfix({
                        "Time": f"{processing_time:.1f}s",
                        "Sources": len(sources)
                    })
                    
                except Exception as e:
                    print(f"\n❌ Error processing question: {question[:50]}...")
                    print(f"   Error: {str(e)}")
                    
                    # Write error information to row
                    row["response"] = f"ERROR: {str(e)}"
                    row["response_sources"] = ""
                    row["processing_time"] = "ERROR"
                    
                    writer.writerow(row)
                    f_out.flush()
                    
                    # Continue with next question instead of stopping
                    continue

    print(f"✅ Processing complete! Responses saved to {outfile}")
    print(f"📊 Processed {total_questions} questions")
    
    # Show final statistics
    if outfile.exists():
        with outfile.open(newline="", encoding="utf-8") as f_out:
            final_reader = csv.DictReader(f_out)
            successful = sum(1 for row in final_reader if not row.get("response", "").startswith("ERROR"))
            print(f"📈 Success rate: {successful}/{total_questions} ({successful/total_questions*100:.1f}%)")

if __name__ == "__main__":
    main()