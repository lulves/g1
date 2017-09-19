from django.shortcuts import render
from django.http import HttpResponse
from agenda.models import *

# Create your views here.

def TodaAgenda(request):
    retorno = "'<h1> Agenda </h1>'"
    listaAgendas = Agenda.objects.all()
    for a in listaAgendas:
    	retorno += '<br> Agenda {}'.format(a.descricao)
    return HttpResponse(retorno)

def InstanciaId (request, id):
	retorno = '<h1> Usuario </h1>'
	u = Usuario.objects.get(pk=id)
	retorno += "<br> Nome do Usuario: {} ".format(u.nome)

def TodosCompromissos(request):
    retorno = "'<h1> Compromissos </h1>'"
    listaCompromissos = Compromisso.objects.all()
    for c in listaCompromissos:
    	retorno += '<br> Compromisso {}'.format(c.nome)
    return HttpResponse(retorno)	