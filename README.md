# RAG Document Q&A System

Production-style Retrieval-Augmented Generation (RAG) system that lets users upload documents and ask natural language questions with source citations.

## Features
- Document ingestion & intelligent chunking
- Embedding generation + Vector store (FAISS / Chroma)
- FastAPI backend with clean REST endpoints
- Prompt engineering for accurate answers + reduced hallucinations
- Source citation in responses
- Evaluation-friendly structure

## Tech Stack
- Python 3.10+
- FastAPI
- Sentence-Transformers / OpenAI embeddings
- FAISS or Chroma
- Pydantic
- Uvicorn

## How to Run
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

API docs available at: `http://localhost:8000/docs`

## Project Structure
```
rag-document-qa/
├── main.py              # FastAPI application
├── rag_pipeline.py      # Core RAG logic
├── prompts.py           # System & user prompts
├── requirements.txt
└── README.md
```

## Key Endpoints
- `POST /upload` – Upload document
- `POST /ask` – Ask a question
- `GET /health` – Health check

Built with focus on practical deployment and iterative prompt improvement.
