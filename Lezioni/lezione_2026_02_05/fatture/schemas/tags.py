from pydantic import BaseModel

# Schemi per i TAG
class TagBase(BaseModel):
    name: str
    color: str = "#CCCCCC"  # Diamo un grigio di default

class TagCreate(TagBase):  # Non aggiungiamo niente dal TagBase
    pass

class Tag(TagBase):
    tag_id: int
    
    class Config:
        from_attributes = True
