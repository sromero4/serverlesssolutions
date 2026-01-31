from django.db import models

from Apps.restaurant.estado.models import Estado

class Perfil(models.Model):
    per_codigo = models.AutoField(primary_key=True)
    per_nombre = models.CharField(max_length=100)
    per_fechacreacion = models.DateTimeField()
    est_codigo = models.ForeignKey(Estado, models.DO_NOTHING)

    def __str__(self):
        return self.per_nombre