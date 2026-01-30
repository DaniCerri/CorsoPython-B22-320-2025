from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Definiamo la stringa di connessione al DB
# DATABASE_URL = "linguaggioSQL+motore://nome_utente:password_db@ip_host_db:porta_server_db/nome_db"
# TODO: mettere questo url in un file .env
DATABASE_URL = "mysql+pymysql://root:@localhost:3306/micro_blog"

# 2. Creiamo l'engine -> ci connettiamo al DB e stabiliamo il necessario
engine = create_engine(
    DATABASE_URL
)

# 3. Creiamo il gestore di sessioni
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine  # <- colleghiamo il nostro engine ad ogni sessione [*]
)
# [*] in pratica verrà utilizzato l'engine che abbiamo creato prima per gestire/far funzionare ogni sessione

# 4. Creiamo la classe che useremo per "ereditare" tutte le cose necessarie alla comunicazione con il DB dei nostri modelli
Base = declarative_base()