from django.db import models

from model import Vehiculo

class VehiculoPapeles(models.Model):
    idPapeles = models.IntegerField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE)