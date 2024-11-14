from django.contrib import admin
from core.models import Produto, Client
# Register your models here.

class ProdutoAdmin (admin.ModelAdmin) :
    list_display = "nome", "preco", "estoque" #Nome das colunas

class ClienteAdmin (admin.ModelAdmin) :
    list_display = "nome", "sobrenome", "email"

admin.site.register(Produto, ProdutoAdmin) #registrar tambem a classe a cima
admin.site.register(Client, ClienteAdmin)
