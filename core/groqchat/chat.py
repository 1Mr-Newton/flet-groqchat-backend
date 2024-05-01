import os
from typing import Dict, List
from groq import Groq
from groq.types.chat.completion_create_params import Message
from groq.types.chat.chat_completion import ChatCompletion
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


class GroqChat:
    def __init__(
        self,
        *,
        model: str = "llama3-70b-8192",
        stream: bool = False,
        messages: List[Message]
    ):
        self.stream = stream
        self.chat = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=False,
        )

    def make_response(self) -> str:
        return self.chat.choices[0].message.content
