from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Utente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=50)
    
    
class The(models.Model):
    nome = models.CharField(max_length=50)
    descrizione = models.CharField(max_length=5000)
    provenienza = models.CharField(max_length=80)
    immagine = models.ImageField()
    

class Recensione(models.Model):
    id_utente = models.ForeignKey(User, on_delete=models.CASCADE)
    id_the = models.ForeignKey(The, on_delete=models.CASCADE)
    data = models.DateTimeField()
    commento = models.CharField(max_length=5000)
    voto = models.IntegerField()
    

class Preferito(models.Model):
    id_utente = models.ForeignKey(User, on_delete=models.CASCADE)
    id_the = models.ForeignKey(The, on_delete=models.CASCADE)
    
    
    
