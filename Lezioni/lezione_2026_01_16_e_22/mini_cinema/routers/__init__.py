# routers/__init__.py

# Il punto (.) indica "da questa cartella corrente"
from .bookings import router as booking_router
from .admin import router as admin_router
# from .products_router import router as products_router  <-- Se ne hai altri