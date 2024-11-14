from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path ('', index, name='index'),
    path('contato', contato),

    #Criando rota para produto/id
    path ('produto/<int:id>', produto, name="produto")

]