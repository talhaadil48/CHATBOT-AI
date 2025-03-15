from models.base import BaseModel
from datetime import datetime


class Chatbot(BaseModel):
    """
    Represents the 'chatbots' table.
    """
    def __init__(self, id: int = None, clerk_user_id: str = None, name: str = None, created_at: datetime = None):
        super().__init__(id)
        self.clerk_user_id = clerk_user_id
        self.name = name
        self.created_at = created_at

    def save(self, cursor, connection) -> None:
        if self.id:
            query = "UPDATE chatbots SET clerk_user_id = %s, name = %s WHERE id = %s"
            params = (self.clerk_user_id, self.name, self.id)
            cursor.execute(query, params)
        else:
            query = "INSERT INTO chatbots (clerk_user_id, name) VALUES (%s, %s)"
            params = (self.clerk_user_id, self.name)
            cursor.execute(query, params)
            self.id = cursor.lastrowid
        connection.commit()
        
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "clerk_user_id": self.clerk_user_id,
            "name": self.name,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
