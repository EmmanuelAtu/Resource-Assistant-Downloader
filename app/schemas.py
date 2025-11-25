from pydantic import BaseModel

class ChatRequest(BaseModel):
    message :str
    
    class Config:
        from_attributes = True