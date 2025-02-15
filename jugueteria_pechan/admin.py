from django.contrib import admin
from .models import Cliente, Articulo, Compra

# Register your models here.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    pass


@admin.register(Articulo)
class ArticuloAdmin(admin.ModelAdmin):
    pass


@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    pass

