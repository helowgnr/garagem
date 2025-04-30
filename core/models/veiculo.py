from django.db import models
from .modelo import Modelo
from .cor import Cor
from .acessorio import acessorio

class Veiculo(models.Model):
    ano = models.IntegerField( null=True, default=0)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name="Veiculos")
    cor = models.ForeignKey (Cor, on_delete=models.PROTECT, related_name="cor")
    acessorios = models.ManyToManyField(acessorio, related_name="veiculo")
    def __str__(self):
        return f'{self.modelo.marca} {self.modelo.nome}, {self.cor.name} ({self.ano})'