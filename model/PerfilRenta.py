from django.db import models

from model import CuentaUsuario

class PerfilRenta(models.Model):
    id = models.IntegerField(primary_key=True)
    cuenta = models.ForeignKey(CuentaUsuario, on_delete=models.CASCADE)