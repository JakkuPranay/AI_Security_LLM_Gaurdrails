from google import genai
from config import(
    GEMINI_API_KEY,
    GEMINI_MODEL
)

client = genai.Client(
    api_key= GEMINI_API_KEY
)

def generate_response(promt: str)-> str:
    respone = client.models.generate_content(
        model= GEMINI_MODEL,
        contents= promt,
    )
    return respone.text or ""
#print(generate_respone("What is agent in 2 lines"))