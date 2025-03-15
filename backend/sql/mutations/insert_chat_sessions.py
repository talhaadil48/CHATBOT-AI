from typing import Dict, Tuple
from sql import Mutation

class InsertChatSession(Mutation):
    """
    Inserts a new chat session into the 'chat_sessions' table for a given chatbot_id and guest_id
    Expects input_params with 'chatbot_id' and 'guest_id'.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple[any, ...]]:
        query = "INSERT INTO chat_sessions (chatbot_id, guest_id) VALUES (%s, %s)"
        params = (
            input_params.get('chatbot_id'),
            input_params.get('guest_id')
        )
        return (query, params)