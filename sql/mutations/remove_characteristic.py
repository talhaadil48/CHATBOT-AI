from typing import Dict, Tuple
from sql import Mutation

class RemoveCharacteristics(Mutation):
    """
    Deletes a characteristic from the 'chatbot_characteristics' table.
    Expects input_params with 'chatbot_id'.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        query = "DELETE FROM chatbot_characteristics WHERE id = %s"
        params = (input_params.get('characteristic_id'),)
        return (query, params)
