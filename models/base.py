from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, Any

class BaseModel(ABC):
    def __init__(self, id: int = None, created_at: datetime = None, is_active: bool = True):
        self.id = id
        self.created_at = created_at or datetime.now(datetime.timezone.utc)
        self.is_active = is_active

    @abstractmethod
    def save(self) -> None:
        """Saves the current object to the database (could be insert or update)."""
        pass

    @abstractmethod
    def to_dict(self) -> Dict[str, Any]:
        """Converts the object into a dictionary."""
        pass

    @abstractmethod
    def __repr__(self) -> str:
        """Returns a string representation of the object."""
        pass

    def delete(self) -> None:
        """Deletes the current object (soft-delete by default)."""
        pass
        
    def update(self, **kwargs):
        """Update the object attributes."""
        pass 
