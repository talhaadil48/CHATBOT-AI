from typing import Dict, Tuple
from sql import Mutation

class DeleteChatbot(Mutation):
    """
    Deletes a chatbot from the 'chatbots' table using the 'chatbot_id'.
    Expects input_params with 'chatbot_id'.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]: 
        query = "DELETE FROM chatbots WHERE id = %s"
        params = (input_params.get('chatbot_id'))
        return (query, params)
