from fastapi import FastAPI, HTTPException
from db.db_connection import DBConnection
from sql.queries import GetChatbotByID
from sql.mutations import InsertMessageByChatSessionID, InsertGuest, InsertChatSession
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Custom Backend Server")
# Define allowed origins
origins = [
    "http://localhost:5173",
    "http://localhost:3000",
]

# Add CORSMiddleware to allow requests from allowed origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows specific origins
    allow_credentials=True,
    allow_methods=["*"],    # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],    # Allows all headers
)

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
        if not result:
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
    input_params = request.model_dump()
    try:
        result = mutation_obj.run(input_params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


class InsertGuestRequest(BaseModel):
    name: str
    email: str


@app.post("/guest")
def insert_guest_api(request: InsertGuestRequest):
    """
    Insert a new guest and return the number of affected rows.
    """
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


@app.post("/chat_sessions")
def insert_chat_session_api(request: InsertChatSessionRequest):
    """
    Insert a new chat session and return the number of affected rows.
    """
    connection = DBConnection.get_connection()
    cursor = DBConnection.get_cursor()
    mutation_obj = InsertChatSession(cursor, connection)
    input_params = request.model_dump()
    try:
        result = mutation_obj.run(input_params)
        return result
    except Exception as e:
        raise HTTPException(status_code=500,detail=str(e))