from typing import Dict, Tuple,List,Any
from sql.execution import Query

class GetChatbotByUser(Query):
    """
    Retrieves complete chatbot information by its User, including characteristics,
    sessions, and related messages.
    """
    def get_statement(self, input_params: Dict[str, any]) -> Tuple[str, Tuple]:
        clerk_user_id = input_params.get('clerk_user_id')
        query = """
        SELECT 
          c.id as chatbot_id, c.name as chatbot_name, c.created_at as chatbot_created_at,
          cc.id as characteristic_id, cc.content as characteristic_content, cc.created_at as characteristic_created_at,
          cs.id as session_id, cs.guest_id, cs.created_at as session_created_at,
          m.id as message_id, m.content as message_content, m.sender, m.created_at as message_created_at
        FROM chatbots c
        LEFT JOIN chatbot_characteristics cc ON c.id = cc.chatbot_id
        LEFT JOIN chat_sessions cs ON c.id = cs.chatbot_id
        LEFT JOIN messages m ON cs.id = m.chat_session_id
        WHERE c.clerk_user_id = %s
        """
        params = (clerk_user_id,)
        return (query, params)
    def transform_response(self, rows: List[Dict[str, Any]]) -> List[dict]:
        if not rows:
            return []

        chatbots_dict = {}
        
        for row in rows:
            chatbot_id = row["chatbot_id"]
            if chatbot_id not in chatbots_dict:
                chatbots_dict[chatbot_id] = {
                    "id": chatbot_id,
                    "name": row["chatbot_name"],
                    "created_at": row["chatbot_created_at"],
                    "chatbot_characteristics": {},
                    "chat_sessions": {}
                }

            chatbot = chatbots_dict[chatbot_id]
            
            # Process characteristics
            if row.get("characteristic_id"):
                char_id = row["characteristic_id"]
                if char_id not in chatbot["chatbot_characteristics"]:
                    chatbot["chatbot_characteristics"][char_id] = {
                        "id": char_id,
                        "content": row["characteristic_content"],
                        "created_at": row["characteristic_created_at"]
                    }

            # Process chat sessions
            if row.get("session_id"):
                session_id = row["session_id"]
                if session_id not in chatbot["chat_sessions"]:
                    chatbot["chat_sessions"][session_id] = {
                        "id": session_id,
                        "created_at": row["session_created_at"],
                        "guest_id": row["guest_id"],
                        "messages": {}
                    }
                
                session = chatbot["chat_sessions"][session_id]
                
                # Process messages
                if row.get("message_id"):
                    message_id = row["message_id"]
                    if message_id not in session["messages"]:
                        session["messages"][message_id] = {
                            "id": message_id,
                            "content": row["message_content"],
                            "sender": row["sender"],
                            "created_at": row["message_created_at"]
                        }
        
        # Convert dictionaries to lists
        for chatbot in chatbots_dict.values():
            chatbot["chatbot_characteristics"] = list(chatbot["chatbot_characteristics"].values())
            for session in chatbot["chat_sessions"].values():
                session["messages"] = list(session["messages"].values())
            chatbot["chat_sessions"] = list(chatbot["chat_sessions"].values())
        
        return list(chatbots_dict.values())
