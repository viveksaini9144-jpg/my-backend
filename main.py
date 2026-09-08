from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://viveksaini9144-jpg.github.io"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "Mera backend chal raha hai!"}


@app.post("/ask")
def ask_ai(data: Question):

    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=f"""
You are JEE Pro With Vivek's AI Doubt Solver.

Help a Class 11 JEE student with Physics, Chemistry and Mathematics.

Explain concepts clearly and step-by-step in simple language.

Student's doubt:
{data.question}
"""
    )

    return {"answer": response.text}
