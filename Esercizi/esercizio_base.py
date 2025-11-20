"""
Stai pianificando un viaggio in auto partendo da casa tua a Torino verso una località di mare.
La destinazione scelta è la città di "Otranto", che dista esattamente 1025 chilometri.
La tua auto, una vecchia "fiat punto", ha un consumo medio dichiarato di 16.5 chilometri con un litro
di carburante. Sapendo che il prezzo attuale della benzina è di 1.829 euro al litro e che dovrai
sostenere una spesa fissa per i pedaggi autostradali pari a 74.50 euro, scrivi uno script che calcoli
la quantità di litri necessari, il costo del solo carburante e infine il costo totale del viaggio.
"""
distanza = 1025  # Distanza dalla nostra meta (idealmente variabile) [km]
CONSUMO = 16.5  # Consumo della nostra macchina [km/L]
COSTO_BENZINA = 1.829  # Costo della benzina [€/L]
costo_pedaggio = 74.50  # Costo dei pedaggi [€]

# Calcolo litri necessari
litri_necessari = distanza / CONSUMO  # km / (km / L) -> km * L/km -> L

# Calcolo costo carburante
costo_carburante = litri_necessari * COSTO_BENZINA  # L * (€ / L) -> €

# Calcolo costo totale
costo_tot = costo_carburante + costo_pedaggio

print(f"Litri necessari per la tratta: {litri_necessari:.2f}")
print(f"Costo del carburante: {costo_carburante:.2f} €")
print(f"Costo del pedaggio: {costo_pedaggio:.2f} €")
print("-" * 50)
print(f"Costo complessivo: {costo_tot:.2f} €")