import enum # -> molto utile per "numerare" le cose
from sqlalchemy import Column, Integer, String, ForeignKey, Date, Enum, Float, Table
from sqlalchemy.orm import relationship
from database import Base

# Per prima cosa, definiamo la tabella di associazione (bridge)
# Tabella che unisce Invoice <-> Tag (relazione N:N)
invoice_tags = Table(
    "invoice_tags",
    Base.metadata,
    Column(
        "invoice_id",
        Integer,
        ForeignKey("invoices.invoice_id"),
        primary_key=True
    ),
    Column(
        "tag_id",
        Integer,
        ForeignKey("tags.tag_id"),
        primary_key=True
    )
)

# Facciamo la classe per gli status delle fatture
class InvoiceStatus(str, enum.Enum):
    DRAFT = "draft"
    ISSUED = "issued"
    PAID = "paid"

# Tabella per salvare e gestire i tag
class Tag(Base):
    __tablename__ = "tags"

    tag_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), unique=True, index=True)  # Es: "Urgente"
    color = Column(String(7))  # Es: "#FF0000" -> rosso

    # Dichiariamo la prima parte della relazione molti a molti
    invoices = relationship("Invoice", secondary=invoice_tags, back_populates="tags")

# Facciamo la classe Client per la tabella "clients".
# Ogni cliente ha id (non usiamo proprio la keyword "id"), name, vat_number, email
# Vi ricordo che è in relazione con la tabella delle fatture
class Client(Base):
    __tablename__ = "clients"

    client_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    vat_number = Column(String(20), unique=True)
    email = Column(String(100))

    invoices = relationship("Invoice", back_populates="client")

# Classe per gestire le fatture
class Invoice(Base):
    __tablename__ = "invoices"

    invoice_id = Column(Integer, primary_key=True, index=True)
    number = Column(String(20), index=True)
    date = Column(Date)
    status = Column(Enum(InvoiceStatus), default=InvoiceStatus.DRAFT)

    client_id = Column(Integer, ForeignKey("clients.client_id"))

    client = relationship("Client", back_populates="invoices")
    items = relationship("InvoiceItem", back_populates="invoice")

    # Definiamo il secondo pezzo della relazione N:N
    tags = relationship("Tag", secondary=invoice_tags, back_populates="invoices")

    # Utilizzando il decoratore @property definiamo una funzione (metodo) della nostra classe che non viene salvato
    # nel database ma che per Pydantic sembrerà una "colonna" della nostra tabella.
    # Quindi potremo fare uno schema pydantic che restituirà anche ciò che fa la funzione sotto "@property" come
    # se fosse un attributo (anche se in realtà è una funzione)
    @property
    def total_amount(self): # La funzione calcola il totale degli item nella fattura
        return sum(item.unit_price * item.quantity for item in self.items)

class InvoiceItem(Base):
    __tablename__ = "invoice_items"

    invoice_item_id = Column(Integer, primary_key=True, index=True)
    description = Column(String(500))
    quantity = Column(Float, default=1.0)
    unit_price = Column(Float)

    invoice_id = Column(Integer, ForeignKey("invoices.invoice_id"))

    invoice = relationship("Invoice", back_populates="items")

"""
======================================================== FATTURA ESEMPIO ========================================================
identificativo: ##########  -> id della fattura (lo decide il DB)
numero: 20260001  -> numero della fattura (che decide l'utente)
data: 05/02/2026  -> data di emissione/creazione della fattura
stato: issued  -> stato attuale della fattura
cliente: (info ottenute dal client_id)
    nome: PINCOPALLO SRL
    p. iva: 123456679210
    mail: pinco.pallo@gmail.com
voci della fattura:
    voce1:
        descrizione: Consulenza del 07/12/2025
        quantità: 8 [ore]
        prezzo unitario: 45 [€]
    voce2: 
        descrizione: Consulenza del 08/12/2025
        quantità: 4 [ore]
        prezzo unitario: 45 [€]
    voce3:
        descrizione: Configurazione e creazione del server principale
        quantità: 1 [volte]
        prezzo unitario: 1800 [€]
    
importo totale: <voce1.quantità * voce1.prezzo-unitario + voce2.quantità * voce.prezzo-unitario + voce3.quantità * voce3.prezzo-unitario>
-> importo totale: <8 * 45 + 4 * 45 + 1 * 1800>
importo totale: 2340 [€]

"""



