from models.base import BaseModel
from datetime import datetime

class ChatSession(BaseModel):
    """
    Represents the 'chat_sessions' table.
    """
    def __init__(self, id: int = None, chatbot_id: int = None, guest_id: int = None, created_at: datetime = None):
        super().__init__(id)
        self.chatbot_id = chatbot_id
        self.guest_id = guest_id
        self.created_at = created_at

    def save(self, cursor, connection) -> None:
        if self.id:
            query = "UPDATE chat_sessions SET chatbot_id = %s, guest_id = %s WHERE id = %s"
            params = (self.chatbot_id, self.guest_id, self.id)
            cursor.execute(query, params)
        else:
            query = "INSERT INTO chat_sessions (chatbot_id, guest_id) VALUES (%s, %s)"
            params = (self.chatbot_id, self.guest_id)
            cursor.execute(query, params)
            self.id = cursor.lastrowid
        connection.commit()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "chatbot_id": self.chatbot_id,
            "guest_id": self.guest_id,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }