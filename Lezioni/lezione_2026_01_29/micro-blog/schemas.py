from pydantic import BaseModel
from typing import List, Optional

# partiamo dagli schemi con meno dipendenze -> commenti
class CommentBase(BaseModel):
    text: str

class CommentCreate(CommentBase):
    # per creare un nuovo commento, ci serve l'id del post di riferimento
    post_id: int

class Comment(CommentBase):
    comment_id: int
    post_id: int
    class Config:
        from_attributes = True

# Schemi dei post
class PostBase(BaseModel):
    title: str
    body: str

class PostCreate(PostBase):
    # Per creare un post ci serve l'id del proprietario
    user_id: int

class Post(PostBase):  # questa la usiamo per rispondere alle richieste
    post_id: int
    user_id: int
    comments: List[Comment] = []  # Qua mettiamo la lista di commenti, di default è vuota

    class Config:
        from_attributes = True

# Provate a fare le 3 classi analoghe per gli utenti, sapendo che un utente viene creato con la mail
# Per la classe UserBase, pensate ai parametri/o che sono sempre presenti
class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    user_id: int
    posts: List[Post] = []  # Di default un utente non ha post, finché non ne crea uno

    class Config:
        from_attributes = True