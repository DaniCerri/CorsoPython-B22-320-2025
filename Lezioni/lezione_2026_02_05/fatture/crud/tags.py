from sqlalchemy.orm import Session
from models.tag import Tag
from schemas.tags import TagCreate

def create_tag(db: Session, tag: TagCreate):
    db_tag = Tag(**tag.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tags(db: Session):
    return db.query(Tag).all()
