from typing import Dict, Tuple,Any
from sql.execution import Mutation

class InsertGuest(Mutation):
    """
    Inserts a new guest into the 'guests' table.
    Expects input_params with 'name' and 'email'.
    """
    def get_statement(self, input_params: Dict[str, Any]) -> Tuple[str, Tuple[Any, ...]]:
        query = "INSERT INTO guests (name, email) VALUES (%s, %s)"
        params = (
            input_params.get('name'),
            input_params.get('email')
        )
        return (query, params)
