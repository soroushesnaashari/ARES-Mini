from pathlib import Path
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from pypdf import PdfReader

DOCS_DIR = Path("data/docs")

def load_txt(path: Path) -> str:
    return path.read_text(encoding="utf-8").strip()

def load_pdf(path: Path) -> str:
    reader = PdfReader(str(path))
    pages = []
    for page in reader.pages:
        text = page.extract_text()
        if text:
            pages.append(text.strip())
    return "\n".join(pages).strip()

def load_json(path: Path) -> str:
    # Read JSON as text so both structured JSON and text-like JSON content work well for retrieval
    raw = path.read_text(encoding="utf-8").strip()
    try:
        data = json.loads(raw)
        if isinstance(data, dict):
            return "\n".join(f"{k}: {v}" for k, v in data.items()).strip()
        if isinstance(data, list):
            return "\n".join(str(item) for item in data).strip()
        return str(data).strip()
    except json.JSONDecodeError:
        # If the file is not valid JSON, still use it as plain text
        return raw

def load_documents():
    if not DOCS_DIR.exists():
        raise FileNotFoundError("data/docs folder not found.")

    docs = []
    for path in DOCS_DIR.iterdir():
        if not path.is_file():
            continue

        try:
            if path.suffix.lower() == ".txt":
                text = load_txt(path)
            elif path.suffix.lower() == ".pdf":
                text = load_pdf(path)
            elif path.suffix.lower() == ".json":
                text = load_json(path)
            else:
                continue

            if text:
                docs.append(f"Source: {path.name}\n{text}")
        except Exception as e:
            print(f"Skipping {path.name}: {e}")

    if not docs:
        raise ValueError("No supported documents found in data/docs.")

    return docs

DOCUMENTS = load_documents()
vectorizer = TfidfVectorizer(stop_words="english")
doc_vectors = vectorizer.fit_transform(DOCUMENTS)

def retrieve(query: str, top_k: int = 1):
    query_vec = vectorizer.transform([query])
    scores = cosine_similarity(query_vec, doc_vectors)[0]
    best_idx = scores.argsort()[::-1][:top_k]
    return [DOCUMENTS[i] for i in best_idx]
