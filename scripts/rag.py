# scripts/rag.py

from pathlib import Path
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFacePipeline
from langchain.chains import RetrievalQA
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline, BitsAndBytesConfig

import torch

def load_vectorstore():
    # 1. Reinstantiate the same embedding model
    embedding_model = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3",
        model_kwargs={"device": "cuda"},
        encode_kwargs={"normalize_embeddings": True},
    )

    # 2. Load from the directory where you saved index.faiss + index.pkl
    index_path = Path("data/vectorstore/faiss_bge_m3_index")
    vectorstore = FAISS.load_local(
        str(index_path),
        embedding_model,
        allow_dangerous_deserialization=True,
        )
    print(f"✅ Loaded FAISS index with {vectorstore.index.ntotal} vectors")
    return vectorstore

def setup_llm():
    # Load the LLM model and tokenizer
    model_name = "mistralai/Mistral-7B-Instruct-v0.3"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        quantization_config=BitsAndBytesConfig(
            load_in_8bit=True,
            llm_int8_enable_fp32_cpu_offload=False,
        ),
        device_map="auto",
        torch_dtype=torch.float16
    )
    
    # Create the pipeline
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=256,
        do_sample=True,
        use_cache=True,
        temperature=0.7,
        top_p=0.95,
        repetition_penalty=1.15,
        pad_token_id=tokenizer.eos_token_id,
    )
    
    # Create LangChain LLM
    llm = HuggingFacePipeline(pipeline=pipe)
    return llm

def create_rag_chain(vectorstore, llm):
    # Create the prompt template
    template = """<s>[INST] Answer the question based on the context provided. Response should be relevant to the question.
    If the answer cannot be deduced from the context, do not give an answer, don't try to make up an answer.
    
    Context: {context}
    
    Question: {question} [/INST]</s>"""
    
    prompt = PromptTemplate(
        template=template,
        input_variables=["context", "question"]
    )
    
    # Create the retriever
    retriever = vectorstore.as_retriever(
        search_type="similarity",
        search_kwargs={"k": 4}
    )
    
    # Create the RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return qa_chain