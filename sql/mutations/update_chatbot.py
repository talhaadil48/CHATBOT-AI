from typing import Dict, Tuple
from sql import Mutation

class UpdateChatbot(Mutation):
    """
    Updates the name of a chatbot in the 'chatbots' table using 'clerk_user_id'.
    Expects input_params with 'clerk_user_id' and 'name'.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        query = "UPDATE chatbots SET name = %s WHERE id = %s"
        params = (
            input_params.get('name'),
            input_params.get('chatbot_id')
        )
        return (query, params)
