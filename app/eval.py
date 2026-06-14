import re

def _tokenize(text: str):
    return set(re.findall(r"\w+", text.lower()))

def _overlap_score(a: str, b: str) -> float:
    a_tokens = _tokenize(a)
    b_tokens = _tokenize(b)

    if not a_tokens or not b_tokens:
        return 0.0

    overlap = len(a_tokens & b_tokens)
    return round(overlap / len(a_tokens), 2)

def score_answer(question: str, answer: str, context: str):
    relevance = _overlap_score(question, answer)
    faithfulness = _overlap_score(answer, context)
    quality = round((relevance + faithfulness) / 2, 2)

    return {
        "relevance": relevance,
        "faithfulness": faithfulness,
        "quality": quality
    }