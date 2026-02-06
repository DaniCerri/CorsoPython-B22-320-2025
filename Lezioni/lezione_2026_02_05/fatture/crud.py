from sqlalchemy.orm import Session
import models, schemas

# =================== TAGS ===================
def create_tag(db: Session, tag: schemas.TagCreate):
    db_tag = models.Tag(**tag.model_dump())
    db.add(db_tag)
    db.commit()
    db.refresh(db_tag)
    return db_tag

def get_tags(db: Session):
    return db.query(models.Tag).all()

# =================== CLIENTS ===================
def create_client(db: Session, client: schemas.ClientCreate):
    db_client = models.Client(**client.model_dump())
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client

def get_clients(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Client).offset(skip).limit(limit).all()

def get_client_by_id(db: Session, client_id: int):
    return db.query(models.Client).filter(models.Client.client_id == client_id).first()

# =================== INVOICES ===================
def create_invoice(db: Session, invoice: schemas.InvoiceCreate):
    # 1. è necessario recuperare dalla fattura il campo con la lista di ID dei tags
    tag_ids = invoice.tag_ids  # 1.1 li prendiamo dall'oggetto
    invoice_data = invoice.model_dump()  # 1.2 Estraiamo i dati della nostra fattura
    invoice_data.pop('tag_ids')  # rimuoviamo dal dizionario con i dati la lista di tag

    # 2. Creiamo la fattura di base
    db_invoice = models.Invoice(**invoice_data)

    # 3. Cerchiamo nel DB i tag corrispondenti agli id che abbiamo nella lista
    if tag_ids:
        # 3.1 facciamo la query per i nostri tag
        # SELECT * FROM tags WHERE tag_id IN ([lista di id]);
        tags = db.query(models.Tag).filter(models.Tag.tag_id.in_(tag_ids)).all()
        # Con i riferimenti che abbiamo scritto in models.py SQLAlchemy conosce la relazione e le tabelle necessarie
        # per gestirla, infatti andrà a popolare automaticamente la tabella di JOIN (o bridge) con le chiavi di tag e
        # fattura corrispondenti
        db_invoice.tags = tags

    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Invoice).offset(skip).limit(limit).all()

def get_invoice(db: Session, invoice_id: int):
    return db.query(models.Invoice).filter(models.Invoice.invoice_id == invoice_id).first()

# =================== ITEMS ===================
def create_invoice_item(db: Session, item: schemas.InvoiceItemCreate, invoice_id: int):
    db_item = models.InvoiceItem(**item.model_dump(), invoice_id=invoice_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item














