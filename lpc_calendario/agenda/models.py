from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.



class Agenda (models.Model):
	descricao = models.CharField(max_length= 300, null= True, blank=False)
	usuario = models.OneToOneField(User)
	visivel = models.BooleanField (True)
	tipo = models.CharField(max_length= 300, null= True, blank=False)
	institucional= models.BooleanField(True)
	def __str__ (self):
		return self.descricao

class Compromisso (models.Model):
	nome = models.CharField(max_length=150)
	dataI = models.DataTime()
	dataF = models.DataTime()
	agendas = models.ForeingKey(Agenda, related_name='agendas', blank = True)
