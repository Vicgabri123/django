from django.shortcuts import render
from core.models import Produto

# Create your views here.
def index(request):
    produto = Produto.objects.all() #Criando todos os produtos
    conteudos = {#Criando dicionario
        'curso' : 'Programação em Python - Django FrameWork',
        'produto': produto
    }
    return render(request, 'index.html', conteudos)

    
def contato(request):
    return render(request, 'contato.html')

def produto(request, id):
    prod = Produto.objects.get(id=id)
    conteudos = {
        'produto': prod 
    }
    return render(request, 'produto.html', conteudos)