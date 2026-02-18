from django.db import models

class Professore(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    settore = models.CharField(max_length=100)
    data_nascita = models.DateField()

    def __str__(self):
        return f"Prof. {self.cognome}"

class Studente(models.Model):
    nome = models.CharField(max_length=50)
    cognome = models.CharField(max_length=50)
    data_nascita = models.DateField()
    matricola = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.nome} {self.cognome} - {self.matricola}"

class Corso(models.Model):
    nome = models.CharField(max_length=100)
    crediti = models.IntegerField(default=6)  # suggerimento da universitario
    codice = models.CharField(max_length=10, unique=True)

    # Foreign Key
    professore = models.ForeignKey(
        Professore,
        # Mettiamo null perchè i corsi dell'università esistono a prescindere
        # da chi li insegna, eliminato un professore, il corso verrà assegnato
        # a qualcun'altro
        on_delete=models.SET_NULL,
        related_name='corsi_insegnati'
    )

    # Foreign Key N:N -> Django genera automaticamente una tabella nel DB per
    # gestire questa relazione
    studenti = models.ManyToManyField(
        Studente,
        blank=True,
        null=True,
        related_name='corsi_seguiti'
    )

    def __str__(self):
        return f"{self.codice} - {self.nome}"



