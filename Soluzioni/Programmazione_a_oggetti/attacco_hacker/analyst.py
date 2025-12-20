"""
Classe Analyst per il Security Operation Center
"""


class Analyst:
    """Rappresenta un analista di sicurezza del SOC"""

    def __init__(self, name, specialization, skill_level, stress_level=0):
        """
        Inizializza un analista.

        Args:
            name: Nome dell'analista
            specialization: Specializzazione (Network, Crypto, Social)
            skill_level: Livello di competenza (1-10)
            stress_level: Livello di stress iniziale (default 0)
        """
        self.name = name
        self.specialization = specialization
        self.skill_level = skill_level
        self.stress_level = stress_level
        self.minacce_gestite = 0
        self.minacce_neutralizzate = 0
        self.minacce_fallite = 0

    def is_burned_out(self):
        """Verifica se l'analista è in burnout"""
        return self.stress_level > 10

    def can_handle_threat(self, threat):
        """
        Verifica se l'analista può gestire una minaccia.

        Args:
            threat: La minaccia da verificare

        Returns:
            True se può gestire, False se in burnout o specializzazione errata
        """
        if self.is_burned_out():
            return False
        if self.specialization != threat.type:
            return False
        return True

    def handle_threat(self, threat):
        """
        Gestisce una minaccia.

        Args:
            threat: La minaccia da gestire

        Returns:
            True se neutralizzata, False se fallita
        """
        if not self.can_handle_threat(threat):
            return False

        self.minacce_gestite += 1

        # Se skill >= gravità: successo
        if self.skill_level >= threat.severity:
            self.stress_level += 1
            self.minacce_neutralizzate += 1
            return True
        # Se skill < gravità: fallimento
        else:
            self.stress_level += 5
            self.minacce_fallite += 1
            return False

    def __str__(self):
        status = "BURNOUT" if self.is_burned_out() else "Operativo"
        return (f"{self.name} [{self.specialization}] - Skill: {self.skill_level}/10 | "
                f"Stress: {self.stress_level}/10 | Status: {status}")
