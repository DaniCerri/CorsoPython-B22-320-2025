from django.db import models

class Luogo(models.Model):
    nome = models.CharField(max_length=100)
    piano = models.IntegerField(default=0)
    note = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.nome} (Piano {self.piano})"

class Software(models.Model):
    nome = models.CharField(max_length=100)
    versione = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nome} v.{self.versione}"

class Dispositivo(models.Model):
    luogo = models.ForeignKey(
        Luogo,
        on_delete=models.SET_NULL,
        null=True, # Siccome abbiamo già la tabella nella versione precedente, andando a creare la colonna,
        # viene impostato il valore a null
        blank=True,
        related_name='dispositivi'
    )

    software_installati = models.ManyToManyField(
        Software,
        blank=True,
        related_name='dispositivi',
        # Non mettiamo "on_delete" perchè chiaramente cancellare un software non vuol dire cancellare un dispositivo
    )

    codice = models.CharField(max_length=50, unique=True)  # Identificativo
    descrizione = models.TextField(blank=True, null=True)  # Paragrafo di testo, può essere testo vuoto o non essere settato
    stato_operativo = models.BooleanField(default=True)  # Booleano, di default settato a True
    data_registrazione = models.DateTimeField(auto_now_add=True)  # Datetime in cui viene registrato il dispositivo nel DB,
    # Anche questo si "setta" da solo

    def __str__(self):
        return self.codice

class Manutenzione(models.Model):
    dispositivo = models.ForeignKey(
        Dispositivo,
        on_delete=models.CASCADE,  # Se il dispositivo a cui fa riferimento la manutenzione viene cancellato, anche il log
        # di manutenzione viene cancellato
        related_name="manutenzioni"
    )

    tecnico = models.CharField(max_length=100)  # TODO: fare una tabella tecnici
    descrizione_intervento = models.TextField()
    data_intervento = models.DateField()
    costo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.dispositivo.codice} - {self.data_intervento}"



















