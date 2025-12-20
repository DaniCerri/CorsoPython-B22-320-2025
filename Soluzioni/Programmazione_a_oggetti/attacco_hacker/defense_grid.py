"""
Classe DefenseGrid per il Security Operation Center
"""


class DefenseGrid:
    """Sistema centrale di gestione del SOC"""

    def __init__(self):
        """Inizializza il sistema di difesa"""
        self.analysts = []
        self.threats = []
        self.threats_neutralized = 0
        self.threats_breached = 0

    def add_analyst(self, analyst):
        """Aggiunge un analista al team"""
        self.analysts.append(analyst)

    def add_threat(self, threat):
        """Aggiunge una minaccia alla coda"""
        self.threats.append(threat)

    def find_available_analyst(self, threat):
        """
        Trova un analista disponibile per gestire la minaccia.

        Args:
            threat: La minaccia da assegnare

        Returns:
            L'analista disponibile o None
        """
        # Cerca analisti con la specializzazione corretta e non in burnout
        available_analysts = [
            a for a in self.analysts
            if a.can_handle_threat(threat)
        ]

        if not available_analysts:
            return None

        # Sceglie l'analista con il livello di stress più basso
        return min(available_analysts, key=lambda a: a.stress_level)

    def process_threats(self):
        """
        Processa tutte le minacce in coda.

        Returns:
            Lista di stringhe con il log del processamento
        """
        linee = []
        linee.append("=" * 80)
        linee.append("INIZIO PROCESSAMENTO MINACCE")
        linee.append("=" * 80)

        for threat in self.threats:
            linee.append(f"\n⚠️  Minaccia rilevata: {threat.id} - {threat.description}")
            linee.append(f"   Tipo: {threat.type} | Gravità: {threat.severity}/10")

            # Trova analista disponibile
            analyst = self.find_available_analyst(threat)

            if analyst is None:
                linee.append(f"   ❌ NESSUN ANALISTA DISPONIBILE - SISTEMA COMPROMESSO!")
                self.threats_breached += 1
                continue

            linee.append(f"   → Assegnata a: {analyst.name} (Skill: {analyst.skill_level})")

            # L'analista gestisce la minaccia
            threat.assigned_to = analyst.name
            success = analyst.handle_threat(threat)

            if success:
                linee.append(f"   ✓ NEUTRALIZZATA da {analyst.name}")
                threat.neutralized = True
                self.threats_neutralized += 1
            else:
                linee.append(f"   ✗ FALLITA - Sistema bucato! {analyst.name} stress +5")
                self.threats_breached += 1

            # Mostra stato stress analista
            if analyst.is_burned_out():
                linee.append(f"   ⚠️  {analyst.name} è in BURNOUT!")

        return linee

    def generate_report(self):
        """
        Genera il report finale.

        Returns:
            Lista di stringhe con il report
        """
        linee = []
        linee.append("\n" + "=" * 80)
        linee.append("REPORT FINALE SOC")
        linee.append("=" * 80)

        linee.append(f"\n📊 STATISTICHE MINACCE:")
        linee.append(f"   Minacce totali: {len(self.threats)}")
        linee.append(f"   ✓ Neutralizzate: {self.threats_neutralized}")
        linee.append(f"   ✗ Subite: {self.threats_breached}")

        if len(self.threats) > 0:
            percentuale_successo = (self.threats_neutralized / len(self.threats)) * 100
            linee.append(f"   Tasso di successo: {percentuale_successo:.1f}%")

        linee.append(f"\n👥 STATO TEAM:")
        for analyst in self.analysts:
            linee.append(f"\n   {analyst}")
            linee.append(f"      Minacce gestite: {analyst.minacce_gestite}")
            linee.append(f"      Neutralizzate: {analyst.minacce_neutralizzate}")
            linee.append(f"      Fallite: {analyst.minacce_fallite}")

        # Conta analisti in burnout
        burnout_count = sum(1 for a in self.analysts if a.is_burned_out())
        linee.append(f"\n   Analisti in burnout: {burnout_count}/{len(self.analysts)}")

        return linee
