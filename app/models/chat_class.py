import datetime
import uuid
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..database.db import Base


class ConversationModel(Base):
    __tablename__ = "conversations"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    chat_id = Column(String, ForeignKey("chats.id"))
    user_message = Column(String, nullable=False)
    groq_message = Column(String, nullable=True)


class ChatModel(Base):
    __tablename__ = "chats"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversations = relationship("ConversationModel", backref="chat")
