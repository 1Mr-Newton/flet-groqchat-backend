from core.exceptions.simple_exception import SimpleException
from ..schema.chat import ChatMessage, ChatRequest
from ..models.chat_class import ChatModel, ConversationModel
from sqlalchemy.orm import Session


class ChatRepo:
    def __init__(self, db: Session):
        self.db = db

    def create_new_chat(self, chat_input: ChatMessage):
        try:

            chat = ChatModel()
            conversation = ConversationModel(
                chat_id=chat.id,
                user_message=chat_input.user_message,
                groq_message=chat_input.groq_message,
            )
            chat.conversations.append(conversation)

            self.db.add(chat)
            self.db.commit()
            return str(chat.id)

        except Exception as e:
            self.db.rollback()
            raise SimpleException(str(e), 500)
            # raise e
        finally:
            self.db.close()

    def get_chat_by_id(self, chat_id: str):
        return self.db.query(ChatModel).filter(ChatModel.id == chat_id).first()

    def update_chat(self, chat_id: str, chat_input: ChatMessage):
        chat = self.get_chat_by_id(chat_id)
        if not chat:
            raise SimpleException("Chat not found", 404)
        conversation = ConversationModel(
            chat_id=chat_id,
            user_message=chat_input.user_message,
            groq_message=chat_input.groq_message,
        )
        chat.conversations.append(conversation)
        self.db.commit()
        return chat.conversations
