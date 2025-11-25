from fastapi import FastAPI
import google.generativeai as genai
from . import schemas
from .config import settings
from fastapi.middleware.cors import CORSMiddleware


genai.configure(api_key=settings.google_api_key)
model = genai.GenerativeModel("gemini-2.0-flash")


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For testing; later restrict to Flutter app URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


chat = model.start_chat()

@app.get("/")
async def Test():
    return {"message": "Hello, World!"}

@app.post("/home_screen")
def Home(cha:schemas.ChatRequest):
  
    response = chat.send_message(cha.message)
    return {"reply":response.text}

