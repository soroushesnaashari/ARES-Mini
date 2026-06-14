from dotenv import load_dotenv
load_dotenv()

from google import genai

client = genai.Client()

MODEL_NAME = "gemini-3.5-flash"

def generate_answer(question: str, context: str) -> str:
    prompt = (
        "Answer the question using only the context below. "
        "If the context does not contain the answer, say: "
        "'I do not know based on the provided context.'\n\n"
        f"Question: {question}\n\n"
        f"Context:\n{context}"
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text.strip()