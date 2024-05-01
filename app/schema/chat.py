from pydantic import BaseModel
from typing import List
from datetime import datetime
from typing import List, Optional


class UserMessage(BaseModel):
    # id: Optional[str] = None
    content: str
    role: str = "user"
    # timestamp: datetime


class GroqMessage(BaseModel):
    # id: Optional[str] = None
    content: str
    role: str = "assistant"
    # timestamp: datetime


class Conversation(BaseModel):
    user_message: UserMessage
    groq_message: GroqMessage


class ChatRequest(BaseModel):
    chat_id: Optional[str] = None
    user_message: str


class ChatMessage(BaseModel):
    chat_id: Optional[str] = None
    user_message: str
    groq_message: str
