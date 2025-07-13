# AviationLM: A Retrieval-Augmented Generation System for Aviation Documentation

[![Python](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/) [![FastAPI](https://img.shields.io/badge/FastAPI-0.95.2-green.svg)](https://fastapi.tiangolo.com/) [![PyTorch](https://img.shields.io/badge/PyTorch-2.3+-red.svg)](https://pytorch.org/) [![CUDA](https://img.shields.io/badge/CUDA-12.4-green.svg)](https://developer.nvidia.com/cuda-toolkit) [![LangChain](https://img.shields.io/badge/LangChain-0.1+-orange.svg)](https://langchain.com/) [![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)](LICENSE)

## 🚀 Overview

AviationLM is a Retrieval-Augmented Generation (RAG) platform that enables efficient and accurate querying of complex FAA/EASA aviation standards. By combining:

- **Multilingual embeddings** (BAAI/bge-m3)
- **Quantized LLMs** (Mistral-7B-Instruct, 8-bit)
- **FAISS similarity search**
- **FastAPI** microservice architecture
- **LLM-as-judge** evaluation

AviationLM delivers contextual, citation-rich answers tailored for aviation compliance professionals.

## 📚 Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Data Pipeline](#data-pipeline)
4. [Model Configuration](#model-configuration)
5. [Deployment & Infrastructure](#deployment--infrastructure)
6. [Evaluation Framework](#evaluation-framework)
7. [Performance Metrics](#performance-metrics)
8. [Installation & Setup](#installation--setup)
9. [Usage](#usage)
10. [API Documentation](#api-documentation)

## 🎯 Project Overview

### Objectives
The aviation industry relies heavily on extensive technical documentation, including FAA Technical Standard Orders (TSOs), RTCA documents, SAE Aerospace Standards, and EASA regulations. These documents contain critical information for aircraft design, certification, and operational procedures. However, the sheer volume and complexity of these documents make information retrieval challenging for aviation professionals.

- **Information Retrieval**: Enable efficient querying of aviation technical documentation
- **Contextual Understanding**: Provide accurate, contextually relevant responses
- **Regulatory Compliance**: Ensure responses align with official aviation standards
- **Scalability**: Support deployment across various computing environments
- **Evaluation**: Implement rigorous assessment of response quality and source accuracy

### Key Features

- **Multilingual Support**: BAAI/bge-m3 embeddings for cross-language document processing
- **GPU Acceleration**: Optimized for NVIDIA GPUs with 8-bit quantization
- **Cloud Deployment**: FastAPI service architecture for scalable deployment
- **Comprehensive Evaluation**: LLM-as-judge framework with detailed scoring metrics
- **Source Attribution**: Automatic citation of retrieved document sources

## 🏗️ System Architecture

### Core Components

```
AviationLM/
├── data/
│   ├── processed/              # OCR-processed Markdown documents
│   ├── chunks/                 # Tokenized document chunks (~500 tokens)
│   ├── vectorstore/            # FAISS index with embeddings
│   └── eval/                   # Evaluation datasets and results
├── scripts/
│   ├── rag.py                  # Core RAG pipeline implementation
│   ├── app.py                  # FastAPI service deployment
│   ├── embed_chunks.py         # Document embedding generation
│   ├── chunk_documents.py      # Document chunking pipeline
│   ├── generate_qa_pairs.py    # Evaluation dataset generation
│   ├── generate_response.py    # RAG response generation
│   ├── evaluate.py             # LLM-as-judge evaluation
│   └── analyze_eval.py         # Performance analysis
└── requirements.txt            # Python dependencies
```

### Technology Stack

- **Embeddings**: BAAI/bge-m3 (multilingual, 1024-dimensional)
- **Vector Database**: FAISS for similarity search
- **Language Model**: Mistral-7B-Instruct-v0.3 (8-bit quantized)
- **Framework**: LangChain for RAG pipeline orchestration
- **API**: FastAPI for production deployment
- **Evaluation**: OpenAI GPT-4o-mini for automated assessment

## 📊 Data Pipeline

### Document Processing

1. **OCR Processing**: ~274 scanned PDFs converted to Markdown format
2. **Text Chunking**: RecursiveCharacterTextSplitter with 500-token chunks and 100-token overlap
3. **Embedding Generation**: BAAI/bge-m3 embeddings with CUDA acceleration
4. **Index Construction**: FAISS index for efficient similarity search

### Chunking Strategy

```python
splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,      # Target chunk size in tokens
    chunk_overlap=100    # Overlap to maintain context
)
```

## 🤖 Model Configuration

### Embedding Model

```python
embedding_model = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    model_kwargs={"device": "cuda"},
    encode_kwargs={"normalize_embeddings": True}
)
```

**Specifications:**
- **Model**: BAAI/bge-m3
- **Dimensions**: 1024
- **Multilingual**: Yes
- **Normalization**: L2 normalization applied
- **Device**: CUDA-accelerated

### Language Model

```python
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.3",
    quantization_config=BitsAndBytesConfig(
        load_in_8bit=True,
        llm_int8_enable_fp32_cpu_offload=False
    ),
    device_map="auto",
    torch_dtype=torch.float16
)
```

**Specifications:**
- **Model**: Mistral-7B-Instruct-v0.3
- **Quantization**: 8-bit for memory efficiency
- **Precision**: FP16 for GPU optimization
- **Context Window**: 32K tokens
- **Generation Parameters**:
  - `max_new_tokens`: 256
  - `temperature`: 0.7
  - `top_p`: 0.95
  - `repetition_penalty`: 1.15

### RAG Pipeline

```python
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=retriever,
    return_source_documents=True,
    chain_type_kwargs={"prompt": prompt}
)
```

**Retrieval Configuration:**
- **Search Type**: Similarity search
- **Top-k**: 4 documents per query
- **Chain Type**: Stuff (concatenate retrieved documents)

## ☁️ Deployment & Infrastructure

### Production Environment

**Google Cloud Platform Configuration:**
- **Instance Type**: VM with 1x NVIDIA T4 GPU
- **GPU Memory**: 16GB VRAM
- **Python Version**: 3.10
- **CUDA Version**: 12.4
- **Storage**: Persistent disk for document corpus and vector indices

**Environment Setup:**

**Create virtual environment**
```bash
python3.10 -m venv venv
source venv/bin/activate
```

**Install PyTorch with CUDA 12.4 support**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

**Install remaining dependencies**
```bash
pip install -r requirements.txt
```

### FastAPI Service Deployment

The system is deployed as a FastAPI service on GCP for production use, providing:
- **Persistent Model Loading**: Models loaded once on startup for optimal performance
- **GPU Acceleration**: Full utilization of NVIDIA T4 with 16GB VRAM
- **Scalable Architecture**: Ready for load balancing and horizontal scaling
- **Production Monitoring**: GPU availability and performance logging

### FastAPI Service

```python
@app.post("/query", response_model=QueryResponse)
def query_rag(req: QueryRequest):
    result = app.state.qa_chain.invoke({"query": req.question})
    sources = [
        {"source": doc.metadata["source"], "chunk_id": doc.metadata["chunk_id"]}
        for doc in result["source_documents"]
    ]
    return QueryResponse(answer=result["result"], sources=sources)
```

**Service Features:**
- **Lifespan Management**: Model loading on startup
- **Async Support**: Non-blocking request handling
- **Error Handling**: Graceful failure recovery
- **Monitoring**: GPU availability logging

## 📈 Evaluation Framework

### Dataset Generation

**Question Generation Strategy:**
- **Method**: LLM-based factoid question generation
- **Model**: OpenAI GPT-4o-mini
- **Dataset Size**: 100 QA pairs
- **Sampling**: Random selection from document chunks

### Evaluation Methodology

**LLM-as-Judge Framework:**
- **Evaluator**: OpenAI GPT-4o-mini
- **Scoring Scale**: 1-5 integer scores
- **Criteria**: Correctness, accuracy, and factual alignment
- **Tolerance**: Extra valid details not penalized

**Scoring Rubric:**
- **Score 1**: Completely incorrect, inaccurate, and/or not factual
- **Score 2**: Mostly incorrect, inaccurate, and/or not factual
- **Score 3**: Somewhat correct, accurate, and/or factual
- **Score 4**: Mostly correct, accurate, and factual
- **Score 5**: Completely correct, accurate, and factual

## 📊 Performance Metrics

### Evaluation Results

**Overall Performance:**
- **Total Questions**: 100
- **Average Score**: 4.11/5.00 (82.20%)
- **Source Accuracy**: 87% (exact match presence)

**Score Distribution:**
- **Score 5**: 54 items (54%)
- **Score 4**: 24 items (24%)
- **Score 3**: 8 items (8%)
- **Score 2**: 7 items (7%)
- **Score 1**: 7 items (7%)

**Key Insights:**
- **High Accuracy**: 78% of responses score 4 or 5
- **Source Reliability**: 87% of responses cite correct sources
- **Error Analysis**: Lowest-scoring items identified for manual review

## ⚙️ Installation & Setup

### 🚀 Quick Start

```bash
# Clone and setup
git clone https://github.com/your-username/AviationLM.git
cd AviationLM
python3.10 -m venv venv
source venv/bin/activate

# Install dependencies
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
pip install -r requirements.txt

# Start the API service
cd scripts
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Installation Steps

**Clone repository**
```bash
git clone https://github.com/your-username/AviationLM.git
cd AviationLM
```

**Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows
```

**Install PyTorch with CUDA 12.4 support**
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
```

**Install remaining dependencies**
```bash
pip install -r requirements.txt
```

**Set environment variables**
```bash
export OPENAI_API_KEY="your-api-key-here"
```

### Data Preparation

**Place OCR-processed documents in data/processed/input_md/**
**Run document chunking**
```bash
python scripts/chunk_documents.py
```

**Generate embeddings and build index**
```bash
python scripts/embed_chunks.py
```

## 🚀 Usage

### Command Line Interface

**Basic RAG Query:**
```bash
python scripts/run_rag.py
```

**Generate Evaluation Dataset:**
```bash
python scripts/generate_qa_pairs.py
```

**Run Evaluation:**
```bash
python scripts/generate_response.py
python scripts/evaluate.py
python scripts/analyze_eval.py
```

## 📖 API Documentation

### API Usage

**Start FastAPI Service:**
```bash
cd scripts
uvicorn app:app --host 0.0.0.0 --port 8000
```

### Endpoints

#### POST /query

**Request:**
```json
{
  "question": "What are the requirements for flight recording systems?"
}
```

**Response:**
```json
{
  "answer": "Flight recording systems must meet specific requirements including...",
  "sources": [
    {
      "source": "RTCA DO-260B 2009 Corr 1 2011.md",
      "chunk_id": 15
    },
    {
      "source": "SAE AS8034B.md", 
      "chunk_id": 23
    }
  ]
}
```