import re

STOPWORDS = {
    "what", "is", "the", "a", "an", "of", "and", "to", "in", "for",
    "how", "why", "who", "where", "when", "does", "do", "did"
}

def _split_sentences(text: str):
    parts = re.split(r'(?<=[.!?])\s+', text.strip())
    return [p.strip() for p in parts if p.strip()]

def _keywords(question: str):
    words = re.findall(r"\w+", question.lower())
    return [w for w in words if w not in STOPWORDS and len(w) > 2]

def generate_answer(question: str, context: str) -> str:
    sentences = _split_sentences(context)
    if not sentences:
        return "I do not know based on the provided context."

    keywords = _keywords(question)
    if keywords:
        matched = [s for s in sentences if any(k in s.lower() for k in keywords)]
        if matched:
            return "Based on the provided context, " + " ".join(matched[:2])

    return "Based on the provided context, " + " ".join(sentences[:2])
