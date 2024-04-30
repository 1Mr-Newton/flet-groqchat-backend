from pydantic import BaseModel
from typing import List
from datetime import datetime


class UserMessage(BaseModel):
    id: str
    text: str
    timestamp: datetime


class GroqMessage(BaseModel):
    id: str
    text: str
    timestamp: datetime


class Conversation(BaseModel):
    user_message: UserMessage
    groq_message: GroqMessage


class Chat(BaseModel):
    messages: List[Conversation]
