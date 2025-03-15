from abc import ABC, abstractmethod
from typing import Dict, Tuple, List, Any

class BaseSQL(ABC):
    """
    Abstract base class for SQL operations.
    """
    def __init__(self, cursor, connection):
        self.cursor = cursor
        self.connection = connection

    @abstractmethod
    def get_statement(self, input_params: Dict[str, Any]) -> Tuple[str, Tuple]:
        """
        Returns a tuple of (SQL statement, parameters) based on the input.
        """
        pass

class Query(BaseSQL):
    """
    Base class for SELECT queries.
    """
    
    def run(self, input_params: Dict[str, Any]) -> dict:
        statement, params = self.get_statement(input_params)
        self.cursor.execute(statement, params)
        rows = self.cursor.fetchall()
        return self.transform_response(rows)
    
    def transform_response(self, rows: List[Dict[str, Any]]) -> dict:
        """
        Converts flat query results to a JSON object wrapping the rows under "data".
        Subclasses can override this method for custom nested transformation.
        """
        return {"data": rows}

class Mutation(BaseSQL):
    """
    Base class for modification operations (INSERT/UPDATE/DELETE).
    """
    def run(self, input_params: Dict[str, Any]) -> Dict[str, Any]:
        statement, params = self.get_statement(input_params)
        self.cursor.execute(statement, params)
        self.connection.commit()
        affected = self.cursor.rowcount
        return {"affected_rows": affected}