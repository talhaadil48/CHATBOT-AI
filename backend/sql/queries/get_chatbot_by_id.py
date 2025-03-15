from typing import Dict, Tuple,List,Any
from sql.execution import Query

class GetChatbotByID(Query):
    """
    Retrieves complete chatbot information by its ID, including characteristics,
    sessions, and related messages.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        chatbot_id = input_params.get('chatbot_id')
        query = """
        SELECT 
          c.id as chatbot_id, c.clerk_user_id, c.name as chatbot_name, c.created_at as chatbot_created_at,
          cc.id as characteristic_id, cc.content as characteristic_content, cc.created_at as characteristic_created_at,
          cs.id as session_id, cs.guest_id, cs.created_at as session_created_at,
          m.id as message_id, m.content as message_content, m.sender, m.created_at as message_created_at
        FROM chatbots c
        LEFT JOIN chatbot_characteristics cc ON c.id = cc.chatbot_id
        LEFT JOIN chat_sessions cs ON c.id = cs.chatbot_id
        LEFT JOIN messages m ON cs.id = m.chat_session_id
        WHERE c.id = %s
        """
        params = (chatbot_id,)
        return (query, params)
    
    def transform_response(self, rows: List[Dict[str, Any]]) -> dict:
        if not rows:
            return {}
        
        chatbot = {
            "id": rows[0]["chatbot_id"],
            "name": rows[0]["chatbot_name"],
            "created_at": rows[0]["chatbot_created_at"],
            "chatbot_characteristics": [],
            "chat_sessions": []
        }
        characteristics_dict = {}
        sessions_dict = {}

        for row in rows:
            # Process characteristics
            if row.get("characteristic_id"):
                char_id = row["characteristic_id"]
                if char_id not in characteristics_dict:
                    characteristics_dict[char_id] = {
                        "id": char_id,
                        "content": row["characteristic_content"],
                        "created_at": row["characteristic_created_at"]
                    }

            # Process chat sessions and nested messages
            if row.get("session_id"):
                session_id = row["session_id"]
                if session_id not in sessions_dict:
                    sessions_dict[session_id] = {
                        "id": session_id,
                        "created_at": row["session_created_at"],
                        "guest_id": row["guest_id"],
                        "messages": []
                    }

                # Process message, avoid duplicates based on message_id
                if row.get("message_id"):
                    message_id = row["message_id"]
                    # Only append message if it is not already added
                    if not any(message["id"] == message_id for message in sessions_dict[session_id]["messages"]):
                        sessions_dict[session_id]["messages"].append({
                            "id": message_id,
                            "content": row["message_content"],
                            "sender": row["sender"],
                            "created_at": row["message_created_at"]
                        })

        chatbot["chatbot_characteristics"] = list(characteristics_dict.values())
        chatbot["chat_sessions"] = list(sessions_dict.values())
        
        return chatbot
