from sqlalchemy.orm import Session
from models.ingrediente import Ingrediente
from schemas.ingrediente import IngredienteCreate, IngredienteUpdate


def get_ingredienti(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Ingrediente).offset(skip).limit(limit).all()


def get_ingrediente(db: Session, ingrediente_id: int):
    return db.query(Ingrediente).filter(Ingrediente.ingrediente_id == ingrediente_id).first()


def create_ingrediente(db: Session, ingrediente: IngredienteCreate):
    db_ingrediente = Ingrediente(**ingrediente.model_dump())
    db.add(db_ingrediente)
    db.commit()
    db.refresh(db_ingrediente)
    return db_ingrediente


def update_ingrediente(db: Session, ingrediente_id: int, ingrediente: IngredienteUpdate):
    db_ingrediente = get_ingrediente(db, ingrediente_id)
    if not db_ingrediente:
        return None
    for key, value in ingrediente.model_dump(exclude_unset=True).items():
        setattr(db_ingrediente, key, value)
    db.commit()
    db.refresh(db_ingrediente)
    return db_ingrediente


def delete_ingrediente(db: Session, ingrediente_id: int):
    db_ingrediente = get_ingrediente(db, ingrediente_id)
    if not db_ingrediente:
        return None
    db.delete(db_ingrediente)
    db.commit()
    return db_ingrediente
