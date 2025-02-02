from abc import ABC, abstractmethod

# Abstract Execution Class (Parent Class)
class Execution(ABC):
    def __init__(self, db):
        self.cursor = db.cursor()
    
    @abstractmethod
    def execute(self, query, params=None):
        """The abstract execute method that must be implemented by subclasses."""
        pass

# ExecuteQuery Class (Inherits from Execution)
class ExecuteQuery(Execution):
    def execute(self, query, params=None):
        self.cursor.execute(query, params if params else ())
        return self.cursor.fetchall()

# ExecuteMutation Class (Inherits from Execution)
class ExecuteMutation(Execution):
    def execute(self, mutation, params=None):
        self.cursor.execute(mutation, params if params else ())
        self.cursor.connection.commit()
        return self.cursor.rowcount