from django.db import models

class Modelo(models.Model):
    nome = models.CharField(max_length=40)
    marca = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return self.nome