# scripts/app.py

from fastapi import FastAPI
from pydantic import BaseModel
from scripts.rag import load_vectorstore, setup_llm, create_rag_chain
import torch
from contextlib import asynccontextmanager

# Define the request & response schemas
class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    sources: list[dict]

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1) Load once
    app.state.vectorstore = load_vectorstore()
    app.state.llm        = setup_llm()
    app.state.qa_chain   = create_rag_chain(
        app.state.vectorstore,
        app.state.llm
    )
    # (Optional) log GPU availability
    print("CUDA available:", torch.cuda.is_available())
    print("CUDA device name:", torch.cuda.get_device_name(0))
    yield

app = FastAPI(title="AviationLM API", lifespan=lifespan)

@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    result = app.state.qa_chain.invoke({"query": req.question})
    # format sources neatly
    sources = [
        {"source": doc.metadata["source"], "chunk_id": doc.metadata["chunk_id"]}
        for doc in result["source_documents"]
    ]
    return QueryResponse(answer=result["result"], sources=sources)
