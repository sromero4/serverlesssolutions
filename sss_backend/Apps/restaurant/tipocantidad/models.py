from django.db import models


class Tipocantidad(models.Model):
    tipcant_codigo = models.AutoField(primary_key=True)
    tipcant_nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.tipcant_nombre