from fastapi import FastAPI
from pydantic import BaseModel
import groq
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))

conversation_history = [
    {"role": "system", "content": "You are RoastBot. Roast the user savagely but keep it funny."}
]

class UserMessage(BaseModel):
    message: str

@app.post("/chat")
def chat(user_message: UserMessage):
    conversation_history.append({"role": "user", "content": user_message.message})
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=conversation_history
    )
    reply = response.choices[0].message.content
    conversation_history.append({"role": "assistant", "content": reply})
    return {"reply": reply}