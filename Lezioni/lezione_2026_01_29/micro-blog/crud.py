from sqlalchemy.orm import Session
import models, schemas

# TODO: fare le funzioni di creazione

# TODO: fare la funzione per leggere un utente da id

# Query: voglio ottenere tutti i commenti sotto i post di un certo utente (da id)
def get_comments_by_user_id(db: Session, user_id: int):
    # con .join() uniamo le tabelle del db, l'unione viene fatta automaticamente sugli id dichiarati nelle ForeignKey
    # e nelle relationship

    return db.query(models.Comment)\
            .join(models.Post)\
            .join(models.User)\
            .filter(models.User.user_id == user_id)\
            .all()
