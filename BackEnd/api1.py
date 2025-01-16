from chatbot1 import ask_bot

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

class Question(BaseModel):
    name: str
    question: str
app = FastAPI()


origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials = ["*"],
    allow_methods = ["*"],
    allow_headers = ["*"]
    
)

@app.get("/")
def index():
    return {"message":"This is the homepage"}
    
    
@app.post("/ask")
async def chat(user_message:Question):
    response_data = await ask_bot(user_message.question)
    return {"Chat_Response": f"{response_data}"}
