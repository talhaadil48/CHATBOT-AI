from typing import Dict, Tuple
from sql import Mutation

class CreateChatbot(Mutation):
    """
    Inserts a new chatbot into the 'chatbots' table.
    Expects input_params with 'clerk_user_id' and 'name'.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        query = "INSERT INTO chatbots (clerk_user_id, name) VALUES (%s, %s)"
        params = (
            input_params.get('user_id'),
            input_params.get('name')
        )
        return (query, params)
