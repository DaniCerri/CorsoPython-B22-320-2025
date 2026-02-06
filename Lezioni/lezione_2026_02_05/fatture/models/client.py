from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from database import Base

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
