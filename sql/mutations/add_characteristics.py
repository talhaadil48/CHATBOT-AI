from typing import Dict, Tuple
from sql import Mutation

class AddCharacteristics(Mutation):
    """
    Inserts a new characteristic into the 'chatbot_characteristics' table.
    Expects input_params with 'chatbot_id' and 'content'.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        query = "INSERT INTO chatbot_characteristics (chatbot_id, content) VALUES (%s, %s)"
        params = (
            input_params.get('chatbot_id'),
            input_params.get('content')
        )
        return (query, params)

