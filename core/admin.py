from django.contrib import admin

from .models import Product, Cliente


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco', 'estoque')


class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'sobrenome', 'email')


admin.site.register(Product, ProdutoAdmin)
admin.site.register(Cliente, ClienteAdmin)
