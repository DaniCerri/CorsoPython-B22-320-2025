from django.db import models


class Ingrediente(models.Model):
    nome = models.CharField(max_length=80, unique=True)
    prezzo_extra = models.FloatField(default=0.0)
    allergene = models.BooleanField(default=False)
    vegetariano = models.BooleanField(default=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "ingredienti"


class Pizza(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    prezzo_base = models.FloatField()
    descrizione = models.CharField(max_length=500, blank=True, null=True)
    disponibile = models.BooleanField(default=True)
    ingredienti = models.ManyToManyField(Ingrediente, blank=True, related_name='pizze')

    def __str__(self):
        return self.nome

    @property
    def prezzo_totale(self):
        return self.prezzo_base + sum(i.prezzo_extra for i in self.ingredienti.all())

    class Meta:
        verbose_name_plural = "pizze"


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    indirizzo = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "clienti"


class Ordine(models.Model):
    STATO_CHOICES = [
        ('ricevuto', 'Ricevuto'),
        ('in_preparazione', 'In Preparazione'),
        ('pronto', 'Pronto'),
        ('consegnato', 'Consegnato'),
    ]

    data_ora = models.DateTimeField()
    stato = models.CharField(max_length=20, choices=STATO_CHOICES, default='ricevuto')
    note = models.TextField(blank=True, null=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT, related_name='ordini')

    def __str__(self):
        return f"Ordine #{self.pk} - {self.cliente.nome} - {self.stato}"

    class Meta:
        verbose_name_plural = "ordini"


class VocePizzaOrdine(models.Model):
    ordine = models.ForeignKey(Ordine, on_delete=models.CASCADE, related_name='voci')
    pizza = models.ForeignKey(Pizza, on_delete=models.PROTECT, related_name='voci')
    quantita = models.IntegerField(default=1)
    ingredienti_extra = models.ManyToManyField(Ingrediente, blank=True, related_name='voci_extra')

    def __str__(self):
        return f"{self.pizza.nome} x{self.quantita}"

    class Meta:
        verbose_name_plural = "voci ordine"
