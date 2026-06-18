from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.rag import retrieve
from app.eval import score_answer
from app.generator import generate_answer

app = FastAPI(title="ARES Mini")

app.mount("/static", StaticFiles(directory="static"), name="static")

INDEX_HTML = Path("templates/index.html")


class ChatRequest(BaseModel):
    question: str


class EvalRequest(BaseModel):
    question: str
    answer: str
    context: str


@app.get("/", response_class=HTMLResponse)
def home():
    try:
        return INDEX_HTML.read_text(encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/chat")
def chat(data: ChatRequest):
    try:
        docs = retrieve(data.question, top_k=1)
        context = docs[0]
        answer = generate_answer(data.question, context)
        return {
            "question": data.question,
            "retrieved_docs": docs,
            "answer": answer
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/evaluate")
def evaluate(data: EvalRequest):
    scores = score_answer(
        question=data.question,
        answer=data.answer,
        context=data.context
    )
    return {
        "question": data.question,
        **scores
    }
