from django.db import models

from Apps.restaurant.estado.models import Estado

class Usuario(models.Model):
    usu_codigo = models.AutoField(primary_key=True)
    usu_nombre = models.CharField(max_length=100)
    usu_telefono = models.CharField(max_length=20, blank=True, null=True)
    usu_login = models.CharField(max_length=50)
    usu_clave = models.CharField(max_length=255)
    usu_apellido = models.CharField(max_length=100, blank=True, null=True)
    usu_fechacreacion = models.DateTimeField()
    usu_fechamodificacion = models.DateTimeField(blank=True, null=True)
    est_codigo = models.ForeignKey(Estado, models.DO_NOTHING)
    # per_codigo = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='per_codigo')

    def __str__(self):
        return self.usu_nombre