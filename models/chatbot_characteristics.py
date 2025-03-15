from models.base import BaseModel
from datetime import datetime

class ChatbotCharacteristic(BaseModel):
    """
    Represents the 'chatbot_characteristics' table.
    """
    def __init__(self, id: int = None, chatbot_id: int = None, content: str = None, created_at: datetime = None):
        super().__init__(id)
        self.chatbot_id = chatbot_id
        self.content = content
        self.created_at = created_at

    def save(self, cursor, connection) -> None:
        if self.id:
            query = "UPDATE chatbot_characteristics SET chatbot_id = %s, content = %s WHERE id = %s"
            params = (self.chatbot_id, self.content, self.id)
            cursor.execute(query, params)
        else:
            query = "INSERT INTO chatbot_characteristics (chatbot_id, content) VALUES (%s, %s)"
            params = (self.chatbot_id, self.content)
            cursor.execute(query, params)
            self.id = cursor.lastrowid
        connection.commit()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "chatbot_id": self.chatbot_id,
            "content": self.content,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }