from models.base import BaseModel
from datetime import datetime

class Message(BaseModel):
    """
    Represents the 'messages' table.
    """
    def __init__(self, id: int = None, chat_session_id: int = None, content: str = None, sender: str = None, created_at: datetime = None):
        super().__init__(id)
        self.chat_session_id = chat_session_id
        self.content = content
        self.sender = sender
        self.created_at = created_at

    def save(self, cursor, connection) -> None:
        if self.id:
            query = "UPDATE messages SET chat_session_id = %s, content = %s, sender = %s WHERE id = %s"
            params = (self.chat_session_id, self.content, self.sender, self.id)
            cursor.execute(query, params)
        else:
            query = "INSERT INTO messages (chat_session_id, content, sender) VALUES (%s, %s, %s)"
            params = (self.chat_session_id, self.content, self.sender)
            cursor.execute(query, params)
            self.id = cursor.lastrowid
        connection.commit()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "chat_session_id": self.chat_session_id,
            "content": self.content,
            "sender": self.sender,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }