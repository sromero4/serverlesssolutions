from django.db import models


class Tipocantidad(models.Model):
    tipcant_codigo = models.AutoField(primary_key=True)
    tipcant_nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'tipocantidad'