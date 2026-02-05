from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Definiamo l'URL di connessione al DB
# Formato: mysql+pymysql://username:password@host:porta/nome_database
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/fatture"

# Definiamo l'engine
engine = create_engine(DATABASE_URL)

# Definiamo il gestore di sessione
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Definiamo la base per i modelli
Base = declarative_base()
