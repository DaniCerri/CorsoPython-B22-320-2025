from pydantic import BaseModel

# Schemi per i CLIENT
class ClientBase(BaseModel):
    name: str
    vat_number: str
    email: str

class ClientCreate(ClientBase):
    pass

class Client(ClientBase):
    client_id: int
    
    class Config:
        from_attributes = True
