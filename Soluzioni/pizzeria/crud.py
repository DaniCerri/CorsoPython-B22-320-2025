from sqlalchemy.orm import Session
import models, schemas

# -- Funzioni di creazione
def create_pizza(db: Session, pizza: schemas.PizzaCreate):
    # 1. istanziamo una nuova pizza "per il db"
    db_pizza = models.Pizza(**pizza.model_dump())

    # 2. inseriamo l'oggetto nel db (per ora solo in RAM)
    db.add(db_pizza)

    # 3. attualizziamo l'inserimento sul disco
    db.commit()

    # 4. refreshamo l'oggetto per avere l'id appena assegnato
    db.refresh(db_pizza)

    # 5. restituiamo la riga creata
    return db_pizza

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.model_dump())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def create_order(db: Session, order: schemas.OrderCreate):
    db_order = models.Order(**order.model_dump())
    # order.model_dump() converte l'oggetto in dizionario:
    # {"quantity": 2, "customer_id": 1, "pizza_id": 3}
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order

# -- Otteniamo un cliente da ID (con tutti i suoi ordini)
def get_customer(db: Session, customer_id: int):
    return db.query(models.Customer).filter(models.Customer.customer_id == customer_id).first()

# Query: voglio ottenere tutti gli ordini per una certa pizza (da nome)
def get_orders_by_pizza_name(db: Session, name: str):
    # Con .join() uniamo le tabelle, l'unione viene fatta automaticamente
    # sugli id dichiarati nelle ForeignKey e nelle relationship
    return db.query(models.Order)\
            .join(models.Pizza)\
            .filter(models.Pizza.name == name)\
            .all()
