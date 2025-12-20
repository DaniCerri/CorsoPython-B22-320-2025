"""
Ottimizzazione flotta droni per spedizioni

La tua ditta di spedizioni a Neo-Tokyo è in crisi energetica e i superiori hanno ordinato
di ridurre drasticamente il numero di decolli. Il tuo compito è scrivere il software per
il "Dispatcher AI" centrale che ottimizza l'allocazione dei pacchi sui droni.
"""

import json
import sys
from package import Package
from fleet_manager import FleetManager

# Configura encoding UTF-8 per Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def load_packages_from_json(filepath):
    """Carica i pacchi da file JSON"""
    with open(filepath, 'r') as f:
        data = json.load(f)

    packages = []
    for item in data:
        package = Package(
            pkg_id=item["id"],
            content=item["content"],
            weight=item["weight"],
            value=item["value"]
        )
        packages.append(package)

    return packages


if __name__ == "__main__":
    # Inizializza il sistema
    fleet_manager = FleetManager()

    # Carica i pacchi da JSON
    packages = load_packages_from_json("dati.json")

    print(f"Sistema Fleet Manager inizializzato")
    print(f"Pacchi caricati: {len(packages)}")

    # Carica i pacchi nel sistema
    fleet_manager.load_packages(packages)

    # Ottimizza l'allocazione
    log_ottimizzazione = fleet_manager.optimize_allocation()
    for linea in log_ottimizzazione:
        print(linea)

    # Genera report
    report = fleet_manager.generate_report()
    for linea in report:
        print(linea)
