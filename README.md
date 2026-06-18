---
title: ARES Mini
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
pinned: false
---
# ARES Mini

A lightweight RAG + evaluation demo that works without any external API key.

<br>

### Features
- Local document retrieval from `data/docs`
- Supports `.txt`, `.pdf`, and `.json`
- Simple extractive answer generation
- Basic evaluation scores
- FastAPI backend
<br>

### Setup Locally

#### 1. Clone the repository
```bash
git clone https://github.com/soroushesnaashari/ARES-Mini.git
cd ARES-Mini
```

#### 2. Install dependencies
```bash
pip install -r requirements.txt
```
#### 3. Add your documents
Put your files inside:
```bash
data/docs/
```
Supported formats:

- `.txt`
- `.pdf`
- `.json`

#### 4. Run the app locally
```bash
uvicorn app.main:app --reload --port 8000
```

#### 5. Open the app
Go to:
```bash
http://127.0.0.1:8000
```
