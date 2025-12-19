from fattura import Fattura
from partita_iva import PartitaIva

mia_partiva_iva = PartitaIva(0.67, 0.2627, 0.15)
mia_partiva_iva.carica_da_file("fatture.json")

totale = mia_partiva_iva.fatturato_totale()
inps = mia_partiva_iva.calcolo_inps()
irpef = mia_partiva_iva.calcolo_irpef()
netto = mia_partiva_iva.calcolo_netto()

print(f"Fatturato totale della partita iva: {totale:.2f} €")
print(f"Da pagare all'INPS: {inps:.2f} €")
print(f"Da pagare all'IRPEF: {irpef:.2f} €")
print(f"Netto dopo le tasse: {netto:.2f} €")

# Calcolare quanto paghiamo in percentuale complessivamente di tasse
coeff_tasse_complessivo = (irpef + inps) / totale
print(f"Sul fatturato paghiamo il {coeff_tasse_complessivo:.2%} di tasse")

# Calcolo della % di netto
print(f"Quindi abbiamo il {(1 - coeff_tasse_complessivo):.2%} di netto")

print(mia_partiva_iva.conta_fatture_per_mese())