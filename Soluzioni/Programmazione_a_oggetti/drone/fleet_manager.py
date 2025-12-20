"""
Classe FleetManager per il sistema di ottimizzazione flotta droni
"""

from drone_trip import DroneTrip


class FleetManager:
    """Gestisce l'ottimizzazione della flotta droni"""

    def __init__(self):
        """Inizializza il gestore della flotta"""
        self.trips = []
        self.all_packages = []

    def load_packages(self, packages):
        """
        Carica la lista di pacchi da processare.

        Args:
            packages: Lista di oggetti Package
        """
        self.all_packages = packages

    def optimize_allocation(self):
        """
        Ottimizza l'allocazione dei pacchi sui droni.

        Utilizza un algoritmo First-Fit Decreasing:
        1. Ordina i pacchi per peso decrescente
        2. Per ogni pacco, cerca il primo drone che può contenerlo
        3. Se nessun drone può contenerlo, crea un nuovo viaggio

        Returns:
            Lista di stringhe con il log dell'ottimizzazione
        """
        linee = []
        # Ordina i pacchi per peso decrescente (pacchi più pesanti prima)
        sorted_packages = sorted(self.all_packages, key=lambda p: p.weight, reverse=True)

        linee.append("=" * 80)
        linee.append("OTTIMIZZAZIONE ALLOCAZIONE PACCHI")
        linee.append("=" * 80)
        linee.append(f"\nPacchi totali da processare: {len(sorted_packages)}")
        linee.append(f"Peso totale: {sum(p.weight for p in sorted_packages):.1f}kg")

        # Processa ogni pacco
        for package in sorted_packages:
            allocated = False

            # Cerca un drone esistente che può contenere il pacco
            for trip in self.trips:
                if trip.add_package(package):
                    allocated = True
                    break

            # Se nessun drone può contenerlo, crea un nuovo viaggio
            if not allocated:
                new_trip = DroneTrip(len(self.trips) + 1)
                new_trip.add_package(package)
                self.trips.append(new_trip)

        linee.append(f"\n✓ Allocazione completata!")
        linee.append(f"  Viaggi necessari: {len(self.trips)}")

        return linee

    def generate_report(self):
        """
        Genera il report finale dell'ottimizzazione.

        Returns:
            Lista di stringhe con il report
        """
        linee = []
        linee.append("\n" + "=" * 80)
        linee.append("REPORT OTTIMIZZAZIONE FLOTTA")
        linee.append("=" * 80)

        linee.append(f"\n📦 STATISTICHE GENERALI:")
        linee.append(f"   Pacchi totali: {len(self.all_packages)}")
        linee.append(f"   Viaggi necessari: {len(self.trips)}")

        total_weight = sum(p.weight for p in self.all_packages)
        theoretical_min_trips = (total_weight / DroneTrip.MAX_CAPACITY)
        linee.append(f"   Viaggi teorici minimi: {theoretical_min_trips:.1f}")

        if theoretical_min_trips > 0:
            efficiency = (theoretical_min_trips / len(self.trips)) * 100
            linee.append(f"   Efficienza algoritmo: {efficiency:.1f}%")

        linee.append(f"\n🚁 DETTAGLIO VIAGGI:")
        total_wasted = 0

        for trip in self.trips:
            linee.append(f"\n   {trip}")
            linee.append(f"      Pacchi a bordo: {len(trip.packages)}")
            linee.append(f"      Spazio libero: {trip.get_remaining_capacity():.1f}kg "
                         f"({trip.get_wasted_space_percentage():.1f}% sprecato)")

            total_wasted += trip.get_remaining_capacity()

            # Mostra primi 3 pacchi (se ce ne sono tanti)
            if len(trip.packages) <= 5:
                for pkg in trip.packages:
                    linee.append(f"        - {pkg}")
            else:
                for pkg in trip.packages[:3]:
                    linee.append(f"        - {pkg}")
                linee.append(f"        ... e altri {len(trip.packages) - 3} pacchi")

        linee.append(f"\n📊 ANALISI EFFICIENZA:")
        avg_wasted = total_wasted / len(self.trips) if self.trips else 0
        linee.append(f"   Spazio totale sprecato: {total_wasted:.1f}kg")
        linee.append(f"   Media spazio sprecato per viaggio: {avg_wasted:.1f}kg")

        avg_utilization = sum(t.get_utilization_percentage() for t in self.trips) / len(self.trips) if self.trips else 0
        linee.append(f"   Utilizzo medio droni: {avg_utilization:.1f}%")

        return linee
