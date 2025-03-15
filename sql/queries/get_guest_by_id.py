from typing import Dict, Tuple,List,Any
from sql import Query

class GetGuestByID(Query):
    """
    Retrieves complete chatbot information by its ID, including characteristics,
    sessions, and related messages.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        guest_id = input_params.get('guest_id')
        query = """
        SELECT 
            id,name,email
            from guests
            where guests.id = %s
        """
        params = (guest_id)
        return (query, params)
    
    def transform_response(self, rows: List[Dict[str, Any]]) -> dict:
        if not rows:
            return {}
        
        guest = {
            "id": rows[0]["id"],
            "name": rows[0]["name"],
            "email": rows[0]["email"],
           
        }
        return guest