import uuid
from sqlalchemy import Column, Integer, String, UUID
from ..database.db import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True)
    password = Column(String)
