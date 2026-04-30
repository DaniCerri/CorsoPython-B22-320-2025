from fastapi import FastAPI
from database import engine, Base
from routers import ingrediente

# Crea tutte le tabelle come descritte in models
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API Pizzeria completa",
    description="Fine esempio per l'API della pizzeria",
    version="1.0.0"
)

app.include_router(ingrediente.router)
# Da ripetere per tutti i router

# Altra cosa qua in mezzo: Gestione CORS e Middleware

@app.get("/")
def root():
    return {"message": "Benvenuto da Mario"}

