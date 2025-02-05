from typing import Dict, Tuple
from sql.execution import Mutation

class InsertMessageByChatSessionID(Mutation):
    """
    Inserts a new message into the 'messages' table for a given chat_session_id.
    Expects input_params with 'chat_session_id', 'content', and 'sender'.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        query = "INSERT INTO messages (chat_session_id, content, sender) VALUES (%s, %s, %s)"
        params = (
            input_params.get('chat_session_id'),
            input_params.get('content'),
            input_params.get('sender')
        )
        return (query, params)