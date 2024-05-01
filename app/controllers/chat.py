from typing import List
from sqlalchemy.orm import Session

from core.exceptions.simple_exception import SimpleException

from ..schema.chat import ChatRequest, ChatMessage
from ..models.chat_class import ChatModel
from ..repo.chat import ChatRepo
from ..utils.system_message import system_message
from core.groqchat.chat import GroqChat, Message


class ChatController:
    def __init__(self, db: Session) -> None:
        self.chat_repo = ChatRepo(db)

    def chat(self, chat_input: ChatRequest) -> dict:

        if chat_input.chat_id:
            conversation = self.chat_repo.get_chat_by_id(chat_input.chat_id)
            if not conversation:
                raise SimpleException("Chat not found", 404)

            req_messages: List[Message] = [system_message]

            for msg in conversation.conversations:
                req_messages.append(Message(role="user", content=msg.user_message))
                req_messages.append(Message(role="assistant", content=msg.groq_message))

            req_messages.append(Message(role="user", content=chat_input.user_message))

            groq_chat = GroqChat(messages=req_messages).make_response()

            self.chat_repo.update_chat(
                chat_input.chat_id,
                ChatMessage(
                    user_message=chat_input.user_message,
                    groq_message=groq_chat,
                ),
            )

            return {
                "chat_id": chat_input.chat_id,
                "groq_message": groq_chat,
            }

        # For a new chat session
        groq_chat = GroqChat(
            messages=[
                system_message,
                Message(role="user", content=chat_input.user_message),
            ],
            stream=False,
        ).make_response()
        chat_id = self.chat_repo.create_new_chat(
            ChatMessage(
                user_message=chat_input.user_message,
                groq_message=groq_chat,
            )
        )
        return {
            "chat_id": chat_id,
            "groq_message": groq_chat,
        }


# "Tell me more about yourself in the form of 80s rap song lyrics"
