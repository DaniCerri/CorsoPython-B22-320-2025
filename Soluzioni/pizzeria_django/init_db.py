"""
Script di popolamento DB per la versione Django.
Eseguire DOPO le migrazioni:
    python manage.py makemigrations
    python manage.py migrate
    python init_db.py
"""
import os
import django
from datetime import timedelta

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizzeria.settings')
django.setup()

from django.utils import timezone
from api.models import Ingrediente, Pizza, Cliente, Ordine, VocePizzaOrdine

if Ingrediente.objects.exists():
    print("DB già popolato, esco.")
else:
    # --- Ingredienti ---
    pomodoro = Ingrediente.objects.create(nome="Pomodoro", prezzo_extra=0.0, allergene=False, vegetariano=True)
    mozzarella = Ingrediente.objects.create(nome="Mozzarella", prezzo_extra=0.5, allergene=True, vegetariano=True)
    basilico = Ingrediente.objects.create(nome="Basilico", prezzo_extra=0.0, allergene=False, vegetariano=True)
    prosciutto = Ingrediente.objects.create(nome="Prosciutto Cotto", prezzo_extra=1.0, allergene=False, vegetariano=False)
    salamino = Ingrediente.objects.create(nome="Salamino Piccante", prezzo_extra=1.0, allergene=False, vegetariano=False)
    funghi = Ingrediente.objects.create(nome="Funghi", prezzo_extra=0.5, allergene=False, vegetariano=True)
    olive = Ingrediente.objects.create(nome="Olive", prezzo_extra=0.5, allergene=False, vegetariano=True)
    cipolla = Ingrediente.objects.create(nome="Cipolla", prezzo_extra=0.3, allergene=False, vegetariano=True)
    peperoni = Ingrediente.objects.create(nome="Peperoni", prezzo_extra=0.5, allergene=False, vegetariano=True)
    wurstel = Ingrediente.objects.create(nome="Wurstel", prezzo_extra=1.0, allergene=True, vegetariano=False)
    tonno = Ingrediente.objects.create(nome="Tonno", prezzo_extra=1.0, allergene=True, vegetariano=False)
    gorgonzola = Ingrediente.objects.create(nome="Gorgonzola", prezzo_extra=1.0, allergene=True, vegetariano=True)
    rucola = Ingrediente.objects.create(nome="Rucola", prezzo_extra=0.5, allergene=False, vegetariano=True)
    bresaola = Ingrediente.objects.create(nome="Bresaola", prezzo_extra=1.5, allergene=False, vegetariano=False)
    scamorza = Ingrediente.objects.create(nome="Scamorza", prezzo_extra=0.8, allergene=True, vegetariano=True)

    # --- Pizze ---
    def make_pizza(nome, prezzo_base, desc, *ingredienti_list):
        p = Pizza.objects.create(nome=nome, prezzo_base=prezzo_base, descrizione=desc)
        p.ingredienti.set(ingredienti_list)
        return p

    margherita = make_pizza("Margherita", 6.0, "La classica", pomodoro, mozzarella, basilico)
    marinara = make_pizza("Marinara", 5.0, "Pomodoro, aglio, origano", pomodoro)
    diavola = make_pizza("Diavola", 8.0, "Con salamino piccante", pomodoro, mozzarella, salamino)
    pr_funghi = make_pizza("Prosciutto e Funghi", 8.5, "Classica combinazione", pomodoro, mozzarella, prosciutto, funghi)
    capricciosa = make_pizza("Capricciosa", 9.0, "Completa e saporita", pomodoro, mozzarella, prosciutto, funghi, olive)
    quattro = make_pizza("Quattro Stagioni", 9.5, "Quattro gusti in una", pomodoro, mozzarella, prosciutto, funghi, olive, cipolla)
    wurstel_pizza = make_pizza("Wurstel e Patatine", 8.0, "Per i più giovani", pomodoro, mozzarella, wurstel)
    tonno_pizza = make_pizza("Tonno e Cipolla", 8.5, "Sapore marino", pomodoro, mozzarella, tonno, cipolla)

    # --- Clienti ---
    mario = Cliente.objects.create(nome="Mario Rossi", telefono="3331234567", indirizzo="Via Roma 1, Milano")
    giulia = Cliente.objects.create(nome="Giulia Bianchi", telefono="3471234567", indirizzo="Corso Italia 42, Roma")
    luca = Cliente.objects.create(nome="Luca Verdi", telefono="3209876543", indirizzo="Via Garibaldi 7, Napoli")

    ora_base = timezone.now() - timedelta(hours=2)

    # --- Ordini ---
    o1 = Ordine.objects.create(cliente=mario, data_ora=ora_base, stato='consegnato')
    VocePizzaOrdine.objects.create(ordine=o1, pizza=margherita, quantita=2)
    VocePizzaOrdine.objects.create(ordine=o1, pizza=diavola, quantita=1)

    o2 = Ordine.objects.create(cliente=giulia, data_ora=ora_base + timedelta(minutes=30), stato='consegnato', note='Senza cipolla')
    VocePizzaOrdine.objects.create(ordine=o2, pizza=capricciosa, quantita=1)

    o3 = Ordine.objects.create(cliente=luca, data_ora=ora_base + timedelta(hours=1), stato='pronto')
    VocePizzaOrdine.objects.create(ordine=o3, pizza=quattro, quantita=2)

    o4 = Ordine.objects.create(cliente=mario, data_ora=timezone.now() - timedelta(minutes=45), stato='in_preparazione', note='Extra piccante')
    v4 = VocePizzaOrdine.objects.create(ordine=o4, pizza=margherita, quantita=1)
    v4.ingredienti_extra.set([salamino, peperoni])

    o5 = Ordine.objects.create(cliente=giulia, data_ora=timezone.now() - timedelta(minutes=10), stato='ricevuto')
    VocePizzaOrdine.objects.create(ordine=o5, pizza=pr_funghi, quantita=3)

    print("DB popolato con successo!")
