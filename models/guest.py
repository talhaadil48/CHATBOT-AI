from models.base import BaseModel
from datetime import datetime

class Guest(BaseModel):
    """
    Represents the 'guests' table.
    """
    def __init__(self, id: int = None, name: str = None, email: str = None, created_at: datetime = None):
        super().__init__(id)
        self.name = name
        self.email = email
        self.created_at = created_at

    def save(self, cursor, connection) -> None:
        if self.id:
            query = "UPDATE guests SET name = %s, email = %s WHERE id = %s"
            params = (self.name, self.email, self.id)
            cursor.execute(query, params)
        else:
            query = "INSERT INTO guests (name, email) VALUES (%s, %s)"
            params = (self.name, self.email)
            cursor.execute(query, params)
            self.id = cursor.lastrowid
        connection.commit()

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "created_at": self.created_at.isoformat() if self.created_at else None
        }
