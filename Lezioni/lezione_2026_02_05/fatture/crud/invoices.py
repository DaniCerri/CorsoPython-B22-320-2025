from sqlalchemy.orm import Session
from models.invoice import Invoice
from models.invoice_item import InvoiceItem
from models.tag import Tag
from schemas.invoices import InvoiceCreate, InvoiceItemCreate

def create_invoice(db: Session, invoice: InvoiceCreate):
    # 1. è necessario recuperare dalla fattura il campo con la lista di ID dei tags
    tag_ids = invoice.tag_ids  # 1.1 li prendiamo dall'oggetto
    invoice_data = invoice.model_dump()  # 1.2 Estraiamo i dati della nostra fattura
    invoice_data.pop('tag_ids')  # rimuoviamo dal dizionario con i dati la lista di tag

    # 2. Creiamo la fattura di base
    db_invoice = Invoice(**invoice_data)

    # 3. Cerchiamo nel DB i tag corrispondenti agli id che abbiamo nella lista
    if tag_ids:
        # 3.1 facciamo la query per i nostri tag
        # SELECT * FROM tags WHERE tag_id IN ([lista di id]);
        tags = db.query(Tag).filter(Tag.tag_id.in_(tag_ids)).all()
        # Con i riferimenti che abbiamo scritto in models.py SQLAlchemy conosce la relazione e le tabelle necessarie
        # per gestirla, infatti andrà a popolare automaticamente la tabella di JOIN (o bridge) con le chiavi di tag e
        # fattura corrispondenti
        db_invoice.tags = tags

    db.add(db_invoice)
    db.commit()
    db.refresh(db_invoice)
    return db_invoice

def get_invoices(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Invoice).offset(skip).limit(limit).all()

def get_invoice(db: Session, invoice_id: int):
    return db.query(Invoice).filter(Invoice.invoice_id == invoice_id).first()

def create_invoice_item(db: Session, item: InvoiceItemCreate, invoice_id: int):
    db_item = InvoiceItem(**item.model_dump(), invoice_id=invoice_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
