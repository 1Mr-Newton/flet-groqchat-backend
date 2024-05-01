from fastapi import APIRouter

from ...schema.chat import ChatRequest
from ...controllers.chat import ChatController

from ...database.db import session

chat_router = APIRouter(prefix="/c")

chat_controller = ChatController(session)


@chat_router.post("/{chat_id}")
def newchat(chat: ChatRequest):
    return chat_controller.chat(chat)
