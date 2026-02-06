from database import SessionLocal

def get_db():
    """Dependency per ottenere una sessione del database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
