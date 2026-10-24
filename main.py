from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from rag_pipeline import RAGPipeline
import uvicorn

app = FastAPI(
    title="RAG Document Q&A System",
    description="Production-style RAG pipeline with prompt engineering and source citations",
    version="1.0.0"
)

rag = RAGPipeline()

class QuestionRequest(BaseModel):
    question: str
    top_k: int = 3

class AnswerResponse(BaseModel):
    answer: str
    sources: list[str]
    confidence: str

@app.get("/health")
def health():
    return {"status": "ok", "message": "RAG system is running"}

@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    if not file.filename.endswith((".txt", ".pdf", ".md")):
        raise HTTPException(status_code=400, detail="Only .txt, .pdf, .md supported in this demo")
    
    content = await file.read()
    text = content.decode("utf-8", errors="ignore")
    
    doc_id = rag.add_document(text, metadata={"filename": file.filename})
    return {
        "message": "Document uploaded and indexed successfully",
        "doc_id": doc_id,
        "filename": file.filename
    }

@app.post("/ask", response_model=AnswerResponse)
def ask_question(req: QuestionRequest):
    if not req.question.strip():
        raise HTTPException(status_code=400, detail="Question cannot be empty")
    
    result = rag.query(req.question, top_k=req.top_k)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
