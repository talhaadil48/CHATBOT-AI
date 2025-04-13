from fastapi import HTTPException
from pydantic import BaseModel
from db import DBConnection
from sql.mutations import (
    InsertMessageByChatSessionID,
    InsertGuest,
    InsertChatSession,
    AddCharacteristics,
    CreateChatbot,
    DeleteChatbot,
    RemoveCharacteristics,
    UpdateChatbot
)

from .base import BaseRouter

class PostRoutes(BaseRouter):
    def __init__(self):
        super().__init__()

        self.router.add_api_route("/messages", self.insert_message, methods=["POST"])
        self.router.add_api_route("/guest", self.insert_guest, methods=["POST"])
        self.router.add_api_route("/chat_sessions", self.insert_chat_session, methods=["POST"])
        self.router.add_api_route("/characteristics", self.add_characteristic, methods=["POST"])
        self.router.add_api_route("/create_chatbot", self.create_chatbot, methods=["POST"])
        self.router.add_api_route("/delete_chatbot", self.delete_chatbot, methods=["POST"])
        self.router.add_api_route("/remove_characteristic", self.remove_characteristic, methods=["POST"])
        self.router.add_api_route("/update_chatbot", self.update_chatbot, methods=["POST"])
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
            
        
    # Request model for adding a characteristic
    class AddCharacteristicRequest(BaseModel):
        chatbot_id: int
        content: str


    def add_characteristic(self, request: AddCharacteristicRequest):
        """
        Add a new characteristic to a chatbot and return confirmation.
        """
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = AddCharacteristics(cursor, connection)
        input_params = request.model_dump()

        try:
            result = mutation_obj.run(input_params)  
            return {"message": "Characteristic added successfully", "rows_affected": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    class CreateChatbotRequest(BaseModel):
        user_id: str
        name: str
    def create_chatbot(self,request: CreateChatbotRequest):
        """
        Create a new chatbot and return success confirmation.
        """
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = CreateChatbot(cursor, connection)
        input_params = request.model_dump()
        
        try:
            result = mutation_obj.run(input_params)  # Assuming 'run()' executes the query
            return {"message": "Chatbot created successfully", "rows_affected": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
    class DeleteChatbotRequest(BaseModel):
        chatbot_id: int

    def delete_chatbot(self, request: DeleteChatbotRequest):
        """
        Delete an existing chatbot and return success confirmation.
        """
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = DeleteChatbot(cursor, connection)
        input_params = request.model_dump()

        try:
            result = mutation_obj.run(input_params)  # Assuming 'run()' executes the query
            return {"message": "Chatbot deleted successfully", "rows_affected": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
  
    class RemoveCharacteristicRequest(BaseModel):
        characteristic_id: int
    def remove_characteristic(self,request: RemoveCharacteristicRequest):
        """
        Remove a characteristic by ID and return success confirmation.
        """
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = RemoveCharacteristics(cursor, connection)
        input_params = request.model_dump()

        try:
            result = mutation_obj.run(input_params)  # Assuming 'run()' executes the query
            return {"message": "Characteristic removed successfully", "rows_affected": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


    class UpdateChatbotRequest(BaseModel):
        chatbot_id: int
        name: str

    
    def update_chatbot(self,request: UpdateChatbotRequest):
        """
        Update a chatbot's name using chatbot_id.
        """
        connection = DBConnection.get_connection()
        cursor = DBConnection.get_cursor()
        mutation_obj = UpdateChatbot(cursor, connection)
        input_params = request.model_dump()

        try:
            result = mutation_obj.run(input_params)
            return {"message": "Chatbot updated successfully", "rows_affected": result}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))


                        
                    
