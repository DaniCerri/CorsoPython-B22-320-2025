"""
Security Operation Center - Sistema di gestione minacce cyber

Sei il responsabile di un SOC di cybersecurity che deve gestire un'ondata di attacchi
hacker in tempo reale. Il tuo compito è smistare le minacce agli analisti corretti
prima che i sistemi crollino.
"""

import json
import sys
from analyst import Analyst
from threat import Threat
from defense_grid import DefenseGrid

# Configura encoding UTF-8 per Windows
if sys.platform == 'win32':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


def load_analysts_from_json(filepath):
    """Carica gli analisti da file JSON"""
    with open(filepath, 'r') as f:
        data = json.load(f)

    analysts = []
    for item in data:
        analyst = Analyst(
            name=item["name"],
            specialization=item["specialization"],
            skill_level=item["skill_level"],
            stress_level=item["stress_level"]
        )
        analysts.append(analyst)

    return analysts


def load_threats_from_json(filepath):
    """Carica le minacce da file JSON"""
    with open(filepath, 'r') as f:
        data = json.load(f)

    threats = []
    for item in data:
        threat = Threat(
            threat_id=item["id"],
            threat_type=item["type"],
            severity=item["severity"],
            description=item.get("description", "")
        )
        threats.append(threat)

    return threats


if __name__ == "__main__":
    # Inizializza il sistema
    defense_grid = DefenseGrid()

    # Carica analisti e minacce da JSON
    analysts = load_analysts_from_json("analisti.json")
    threats = load_threats_from_json("attacchi.json")

    # Aggiungi al sistema
    for analyst in analysts:
        defense_grid.add_analyst(analyst)

    for threat in threats:
        defense_grid.add_threat(threat)

    print(f"Sistema SOC inizializzato:")
    print(f"  Analisti: {len(analysts)}")
    print(f"  Minacce da processare: {len(threats)}")

    # Processa le minacce
    log_processamento = defense_grid.process_threats()
    for linea in log_processamento:
        print(linea)

    # Genera report
    report = defense_grid.generate_report()
    for linea in report:
        print(linea)
