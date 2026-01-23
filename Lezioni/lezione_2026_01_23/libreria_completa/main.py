from fastapi import FastAPI
from routers import authors, books

app = FastAPI(
    title="Libreria più bella",
    description="Seconda implementazione dell'API della libreria con Pydantic",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Vai su /docs per testare l'API"
    }

app.include_router(
    authors.router,
    prefix="/authors",
    tags=['Autori']
)

app.include_router(
    books.router,
    prefix="/books",
    tags=['Libri']
)