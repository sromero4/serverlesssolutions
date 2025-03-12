from django.db import models


class Apartamento(models.Model):
    apto_codigo = models.IntegerField(primary_key=True)
    apto_nombre = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'apartamento'