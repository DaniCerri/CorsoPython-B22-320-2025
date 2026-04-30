from django.contrib import admin
from .models import Ingrediente, Pizza, Cliente, Ordine, VocePizzaOrdine


@admin.register(Ingrediente)
class IngredienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'prezzo_extra', 'allergene', 'vegetariano']
    search_fields = ['nome']
    list_filter = ['allergene', 'vegetariano']


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'prezzo_base', 'disponibile']
    search_fields = ['nome']
    list_filter = ['disponibile']
    filter_horizontal = ['ingredienti']


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nome', 'telefono', 'indirizzo']
    search_fields = ['nome', 'telefono']


@admin.register(Ordine)
class OrdineAdmin(admin.ModelAdmin):
    list_display = ['id', 'cliente', 'stato', 'data_ora']
    list_filter = ['stato']
    search_fields = ['cliente__nome']


@admin.register(VocePizzaOrdine)
class VocePizzaOrdineAdmin(admin.ModelAdmin):
    list_display = ['ordine', 'pizza', 'quantita']
