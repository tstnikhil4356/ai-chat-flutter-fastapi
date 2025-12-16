import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import google.generativeai as genai

# -------------------------
# App setup
# -------------------------

app = FastAPI()

# -------------------------
# Configure Gemini
# -------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError("GEMINI_API_KEY not found")

genai.configure(api_key=GEMINI_API_KEY)

# -------------------------
# Data models
# -------------------------

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    role: str
    content: str

# -------------------------
# System prompt
# -------------------------

SYSTEM_PROMPT = (
    "You are a helpful assistant. "
    "Explain concepts clearly, step by step, in simple language."
)

# -------------------------
# Routes
# -------------------------

@app.get("/")
def root():
    return {"status": "Backend running with Gemini"}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    try:
        model = genai.GenerativeModel("models/gemini-flash-lite-latest")

        prompt = f"""
System:
{SYSTEM_PROMPT}

User:
{request.message}
"""

        response = model.generate_content(prompt)

        return {
            "role": "assistant",
            "content": response.text
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
