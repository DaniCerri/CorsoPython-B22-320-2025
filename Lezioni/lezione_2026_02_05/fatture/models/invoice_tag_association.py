from sqlalchemy import Table, Column, Integer, ForeignKey
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
