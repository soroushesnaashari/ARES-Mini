from fastapi import FastAPI, HTTPException, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from app.rag import retrieve
from app.eval import score_answer
from app.generator import generate_answer

app = FastAPI(title="ARES Mini")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

class ChatRequest(BaseModel):
    question: str

class EvalRequest(BaseModel):
    question: str
    answer: str
    context: str

@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
