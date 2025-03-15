from fastapi import HTTPException
from pydantic import BaseModel
from db import DBConnection
from sql.mutations import InsertMessageByChatSessionID, InsertGuest, InsertChatSession
from .base import BaseRouter

class PostRoutes(BaseRouter):
    def __init__(self):
        super().__init__()

        self.router.add_api_route("/messages", self.insert_message, methods=["POST"])
        self.router.add_api_route("/guest", self.insert_guest, methods=["POST"])
        self.router.add_api_route("/chat_sessions", self.insert_chat_session, methods=["POST"])

    class InsertMessageRequest(BaseModel):
        chat_session_id: int
        content: str
        sender: str

    def insert_message(self, request: InsertMessageRequest):
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = InsertMessageByChatSessionID(cursor, connection)
        input_params = request.model_dump()
        try:
            result = mutation_obj.run(input_params)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    class InsertGuestRequest(BaseModel):
        name: str
        email: str

    def insert_guest(self, request: InsertGuestRequest):
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = InsertGuest(cursor, connection)
        input_params = request.model_dump()
        try:
            result = mutation_obj.run(input_params)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    class InsertChatSessionRequest(BaseModel):
        chatbot_id: int
        guest_id: int

    def insert_chat_session(self, request: InsertChatSessionRequest):
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = InsertChatSession(cursor, connection)
        input_params = request.model_dump()
        try:
            result = mutation_obj.run(input_params)
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
