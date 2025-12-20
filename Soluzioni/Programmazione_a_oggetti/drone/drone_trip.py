"""
Classe DroneTrip per il sistema di ottimizzazione flotta droni
"""


class DroneTrip:
    """Rappresenta un singolo viaggio di un drone"""

    MAX_CAPACITY = 100.0  # kg

    def __init__(self, trip_number):
        """
        Inizializza un viaggio.

        Args:
            trip_number: Numero progressivo del viaggio
        """
        self.trip_number = trip_number
        self.packages = []
        self.current_weight = 0.0

    def can_add_package(self, package):
        """
        Verifica se è possibile aggiungere un pacco.

        Args:
            package: Il pacco da verificare

        Returns:
            True se c'è spazio, False altrimenti
        """
        return (self.current_weight + package.weight) <= self.MAX_CAPACITY

    def add_package(self, package):
        """
        Aggiunge un pacco al viaggio.

        Args:
            package: Il pacco da aggiungere

        Returns:
            True se aggiunto con successo, False se non c'è spazio
        """
        if self.can_add_package(package):
            self.packages.append(package)
            self.current_weight += package.weight
            return True
        return False

    def get_remaining_capacity(self):
        """Restituisce lo spazio libero rimanente"""
        return self.MAX_CAPACITY - self.current_weight

    def get_utilization_percentage(self):
        """Restituisce la percentuale di utilizzo del drone"""
        return (self.current_weight / self.MAX_CAPACITY) * 100

    def get_wasted_space_percentage(self):
        """Restituisce la percentuale di spazio sprecato"""
        return 100 - self.get_utilization_percentage()

    def __str__(self):
        return (f"Drone #{self.trip_number} - "
                f"{self.current_weight:.1f}/{self.MAX_CAPACITY}kg "
                f"({self.get_utilization_percentage():.1f}% utilizzato)")
