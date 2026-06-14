---
title: ARES Mini
emoji: 🤖
colorFrom: black
colorTo: white
sdk: docker
app_port: 7860
pinned: false
---

# ARES Mini

A lightweight Retrieval-Augmented Generation (RAG) application inspired by the ideas behind the [ARES](https://arxiv.org/abs/2311.09476) paper.

ARES Mini demonstrates a complete RAG pipeline:

User Question  
↓  
Document Retrieval  
↓  
Context Selection  
↓  
LLM Generation  
↓  
Answer Evaluation  

<br>

### Features

- Supports `.txt`, `.pdf`, and `.json` documents
- Local document retrieval from `data/docs`
- TF-IDF based similarity search
- Gemini-powered answer generation
- Basic RAG evaluation scores
- FastAPI backend
- Simple web interface

<br>

### Project Structure

```
ARES-Mini/
│
├── app/
│   ├── main.py
│   ├── rag.py
│   ├── generator.py
│   └── eval.py
│
├── data/
│   └── docs/
│
├── templates/
│   └── index.html
│
├── static/
│   └── style.css
│
├── requirements.txt
├── Dockerfile
└── README.md
```

<br>

### How It Works
The user submits a question.<br>
The retrieval module searches the uploaded documents and finds the most relevant information.<br>
The retrieved context is sent to a language model, which generates an answer based only on the provided information.<br>
Finally, the evaluation module measures the answer quality.

<br>

### Local Setup

Install dependencies:
```bash
pip install -r requirements.txt
```

Create a `.env` file:
```env
GOOGLE_API_KEY=your_api_key_here
```

Run:
```bash
uvicorn app.main:app --reload --port 8000
```

Open:
```
http://127.0.0.1:8000
```

<br>

### Deployment
This project is designed to run on Hugging Face Spaces using Docker.<br>
The API key should be added as a Space Secret instead of uploading it to GitHub.

<br>

### Author
Mohammad Soroush Esnaashari
