import enum

# Facciamo la classe per gli status delle fatture
class InvoiceStatus(str, enum.Enum):
    DRAFT = "draft"
    ISSUED = "issued"
    PAID = "paid"
