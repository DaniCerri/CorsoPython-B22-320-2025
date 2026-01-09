from fastapi import FastAPI, HTTPException
import json

# Per prima cosa istanziamo un oggetto di classe FastAPI
app = FastAPI(title="API Menu v1")

# Successivamente carichiamo all'avvio del server i dati dal JSON
with open("menu.json", "r", encoding="utf-8") as file_in:
    MENU = json.load(file_in)

# 1.Endpoint base -> ROOT
@app.get("/")
def get_info_ristorante():
    # FastAPI si preoccupa al posto nostro di convertire il dizionario in JSON e di gestire
    # la coda del server
    return {
        "nome": "Ristorante Immaginazione",
        "luogo": "via Carlo Alberto 22/A",
        "orari": [
            {"lun-ven": ["09:00-12:00", "15:00-21:00"]},
            {"sab-dom": ["11:00-12:00", "18:00-21:00"]}
        ]
    }

@app.get("/categories")
def get_categories():
    """
    Funzione che restituisce l'elenco completo delle categorie disponibili
    :return: Lista di categorie uniche
    """
    # set_categorie = set()  # Set vuoto che conterrà le categorie
    # for piatto in MENU:
    #     set_categorie.add(piatto['categoria'])
    # set_categorie = list(set_categorie)

    set_categorie = list(set(piatto['categoria'] for piatto in MENU))

    return {
        "categories": set_categorie,
        "count": len(set_categorie)
    }

# TODO: fare un endpoint che restituisca gli ingredienti unici








