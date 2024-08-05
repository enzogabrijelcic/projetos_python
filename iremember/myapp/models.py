from django.db import models

# Create your models here.
class User(models.Model):
    nome = models.CharField(max_length=100)
    senha = models.CharField(max_length=100)
    email = models.EmailField()
    cpf = models.CharField(max_length=100)
    def __str__(self):
        return self.nome
