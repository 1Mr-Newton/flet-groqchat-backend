from ..schema.userauth import UserRegisterRequest
from ..models.user_class import User
from sqlalchemy.orm import Session


class UserRepo:
    def __init__(self, db: Session):
        self.db = db

    def get_user_by_id(self, user_id):
        return self.db.query(User).filter(User.id == user_id).first()

    def get_user_by_email(self, email):
        return self.db.query(User).filter(User.email == email).first()

    def create_user(self, user_input: User):
        user = self.db.query(User).filter(User.email == user_input.email).first()

        if user:
            return user
        user = User(email=user_input.email, password=user_input.password)

        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def update_user(self, user):
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete_user(self, user):
        self.db.delete(user)
        self.db.commit()
