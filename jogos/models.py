
from ast import Str
from unittest.util import _MAX_LENGTH
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Cliente(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    cliente = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11) 
    email = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)
    data_nasc = models.DateField()
    

    def __str__(self):
        return self.cliente



class Mega(models.Model):
    numero = models.CharField(max_length=250)
    #id = models.IntegerField(primary_key=True),
    nome = models.ForeignKey(User,on_delete=models.CASCADE)
   # nome = models.OneToOneField(Cliente,on_delete=models.CASCADE)
    #nome = models. ManyToManyField(User)

    
    def __str__(self):
        return self.numero

class Bicho(models.Model):
    numero_bicho = models.CharField(max_length=250)
    #id = models.IntegerField(primary_key=True),
    nome = models.ForeignKey(User,on_delete=models.CASCADE)
   # nome = models.OneToOneField(Cliente,on_delete=models.CASCADE)
    #nome = models. ManyToManyField(User)

      
    def __str__(self):
     return str(self.numero_bicho)



class Carteira(models.Model):
    saldo = models.CharField(max_length=50)
    nome = models.ForeignKey(User,on_delete=models.CASCADE)

  
    def __str__(self):
     return str(self.saldo)


class Rmega(models.Model):
    resultado = models.CharField(max_length=50)

    def __str__(self):
        return str(self.resultado)

class Rbicho(models.Model):
    resultado1 = models.CharField(max_length=50)
    def __str__(self):
        return str(self.resultado1)



   
 



