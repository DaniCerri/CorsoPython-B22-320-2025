"""
Classe Threat per il Security Operation Center
"""


class Threat:
    """Rappresenta una minaccia cyber"""

    def __init__(self, threat_id, threat_type, severity, description=""):
        """
        Inizializza una minaccia.

        Args:
            threat_id: ID univoco della minaccia
            threat_type: Tipo di minaccia (Network, Crypto, Social)
            severity: Gravità (1-10)
            description: Descrizione della minaccia
        """
        self.id = threat_id
        self.type = threat_type
        self.severity = severity
        self.description = description
        self.neutralized = False
        self.assigned_to = None

    def __str__(self):
        status = "NEUTRALIZZATA" if self.neutralized else "ATTIVA"
        return f"{self.id} [{self.type}] Severity: {self.severity}/10 - {status}"
