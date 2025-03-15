from fastapi import HTTPException
from db import DBConnection
from sql.queries import GetChatbotByID, GetChatbotByUser, GetGuestByID
from .base import BaseRouter

class GetRoutes(BaseRouter):
    def __init__(self):
        super().__init__()

        self.router.add_api_route("/chatbots/{chatbot_id}", self.get_chatbot_by_id, methods=["GET"])
        self.router.add_api_route("/guests/{guest_id}", self.get_guest_by_id, methods=["GET"])
        self.router.add_api_route("/chatbotbyuser/{clerk_user_id}", self.get_chatbot_by_user, methods=["GET"])

    def get_chatbot_by_id(self, chatbot_id: int):
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        query_obj = GetChatbotByID(cursor, connection)
        try:
            input_params = {"chatbot_id": chatbot_id}
            result = query_obj.run(input_params)
            if not result:
                raise HTTPException(status_code=404, detail="Chatbot not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_guest_by_id(self, guest_id: int):
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        query_obj = GetGuestByID(cursor, connection)
        try:
            input_params = {"guest_id": guest_id}
            result = query_obj.run(input_params)
            if not result:
                raise HTTPException(status_code=404, detail="Guest not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_chatbot_by_user(self, clerk_user_id: str):
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        query_obj = GetChatbotByUser(cursor, connection)
        try:
            input_params = {"clerk_user_id": clerk_user_id}
            result = query_obj.run(input_params)
            if not result:
                raise HTTPException(status_code=404, detail="Chatbot not found")
            return result
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
