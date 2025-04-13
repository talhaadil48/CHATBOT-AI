from typing import Dict, Tuple, List, Any
from sql import Query

class GetChatSessionByID(Query):
    """
    Retrieves a chat session by ID, including messages, related chatbot info, and guest info.
    """
    def get_statement(self, input_params: Dict[str, Any]) -> Tuple[str, Tuple]:
        chat_session_id = input_params.get("chat_session_id")
        query = """
        SELECT 
            cs.id AS session_id, cs.created_at AS session_created_at,
            m.id AS message_id, m.content AS message_content, m.sender, m.created_at AS message_created_at,
            c.name AS chatbot_name,
            g.name AS guest_name, g.email AS guest_email
        FROM chat_sessions cs
        LEFT JOIN messages m ON cs.id = m.chat_session_id
        LEFT JOIN chatbots c ON cs.chatbot_id = c.id
        LEFT JOIN guests g ON cs.guest_id = g.id
        WHERE cs.id = %s
        """
        params = (chat_session_id,)
        return (query, params)

    def transform_response(self, rows: List[Dict[str, Any]]) -> dict:
        if not rows:
            return {}

        first_row = rows[0]
        session = {
            "id": first_row["session_id"],
            "created_at": first_row["session_created_at"],
            "messages": [],
            "chatbots": {
                "name": first_row["chatbot_name"]
            },
            "guests": {
                "name": first_row["guest_name"],
                "email": first_row["guest_email"]
            }
        }

        seen_messages = set()
        for row in rows:
            msg_id = row.get("message_id")
            if msg_id and msg_id not in seen_messages:
                session["messages"].append({
                    "id": msg_id,
                    "content": row["message_content"],
                    "sender": row["sender"],
                    "created_at": row["message_created_at"]
                })
                seen_messages.add(msg_id)

        return session
