from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Compromisso(models.Model):
	nome = models.CharField(max_length=150)
	descricao = models.CharField(max_length=150)
	dataInicio = models.DateField(null= True, blank=False)
	horaInicio = models.TimeField(null= True, blank=False)

	def __str__ (self):
		return self.nome

class Agenda (models.Model):
	descricao = models.CharField(max_length= 300, null= True, blank=False)
	compromissos = models.ManyToManyField(Compromisso, related_name='agendas', blank = True)
	def __str__ (self):
		return self.descricao

class AgendaFeriado(Agenda):
	feriado = models.CharField(max_length=150)
	def __str__ (self):
		return self.feriado

class Usuario(models.Model):
	
	nome = models.CharField(max_length=150)
	usuario = models.OneToOneField(User)
	email = models.CharField(max_length=200)
	agendas = models.ForeignKey(Agenda, related_name="usarios", null = True, blank=False)
	def __str__ (self):
		return self.nome
