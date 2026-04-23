import groq
import os
from dotenv import load_dotenv
load_dotenv()
client = groq.Groq(api_key=os.getenv("GROQ_API_KEY"))
conversation_history = [{"role":"assistant","content":"you are a ruthless roast bot"}]
while True:
    user_input = input("Enter message to get roasted or type 'quit' to exit: ")
    if user_input.lower() == "quit":
        print("GoodBye!!")
        break
    else:
        conversation_history.append({"role":"user","content":user_input})
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages= conversation_history
        )
        reply = response.choices[0].message.content
        print(f"AI ROAST_BOT: {reply}")