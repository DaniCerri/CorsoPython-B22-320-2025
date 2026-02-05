from sqlalchemy.orm import Session
import models, schemas

# -- Funzioni di creazione
def create_user(db: Session, user: schemas.UserCreate):
    # 1. istanziamo un nuove user "per il db"
    db_user = models.User(email=user.email)

    # 2. inseriamo l'oggetto nel db
    db.add(db_user)  # -> Questo inserimento per ora è solamente nella RAM

    # 3. "Attualizziamo" l'inserimento, salvandolo nel DB nel disco fisso
    db.commit()

    # 4. Refreshamo il db nella RAM per ottenere l'istanza completa
    db.refresh(db_user)

    # 5. Restuiamo la riga creata
    return db_user

def create_post(db: Session, post: schemas.PostCreate):
    db_post = models.Post(**post.model_dump())  # post.model_dump() O post.dict() convertono l'oggetto in dizionario
    # post = {"title": "titolo", "body": "corpo", "user_id": 3}
    # funz(**post) -> funz(title="titolo", body="corpo", user_id=3)
    # funz("prova", "body prova", user_id=6)
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def create_comment(db: Session, comment: schemas.CommentCreate):
    db_comment = models.Comment(**comment.model_dump())
    db.add(db_comment)
    db.commit()
    db.refresh(db_comment)
    return db_comment

# -- Otteniamo un utente da ID
def get_user(db: Session, user_id: int):
    # In base a come abbiamo scritto models e schemas, SQLAlchemy capisce da solo che bisogna fare una join
    # con le altre tabelle, non serve dirglielo esplicitamente come invece dobbiamo fare nella funzione di sotto
    return db.query(models.User).filter(models.User.user_id == user_id).first()

# Query: voglio ottenere tutti i commenti sotto i post di un certo utente (da id)
def get_comments_by_user_id(db: Session, user_id: int):
    # con .join() uniamo le tabelle del db, l'unione viene fatta automaticamente sugli id dichiarati nelle ForeignKey
    # e nelle relationship

    return db.query(models.Comment)\
            .join(models.Post)\
            .join(models.User)\
            .filter(models.User.user_id == user_id)\
            .all()
