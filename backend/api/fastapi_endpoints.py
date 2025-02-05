from fastapi import FastAPI, HTTPException
from db.db_connection import DBConnection
from sql.queries.get_chatbot_by_id import GetChatbotByID
from sql.mutations.insert_message import InsertMessageByChatSessionID
from pydantic import BaseModel

app = FastAPI(title="Custom Backend Server")

@app.get("/chatbots/{chatbot_id}")
def get_chatbot_by_id(chatbot_id: int):
    """
    Retrieve full chatbot information by ID and return nested JSON.
    """
    connection = DBConnection.get_connection()
    cursor = DBConnection.get_cursor()
    query_obj = GetChatbotByID(cursor, connection)
    try:
        input_params = {"chatbot_id": chatbot_id}
        result = query_obj.run(input_params)
        if not result.get("chatbots"):
            raise HTTPException(status_code=404, detail="Chatbot not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Request model for inserting a message
class InsertMessageRequest(BaseModel):
    chat_session_id: int
    content: str
    sender: str

@app.post("/messages")
def insert_message(request: InsertMessageRequest):
    """
    Insert a new message and return the number of affected rows.
    """
    connection = DBConnection.get_connection()
    cursor = DBConnection.get_cursor()
    mutation_obj = InsertMessageByChatSessionID(cursor, connection)
    input_params = request.dict()
    try:
        result = mutation_obj.run(input_params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))