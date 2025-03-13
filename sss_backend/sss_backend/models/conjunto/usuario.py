from django.db import models

from .perfil import *
class Usuario(models.Model):
    usu_codigo = models.BigAutoField(primary_key=True)
    usu_nombre = models.CharField(max_length=100, blank=True, null=True)
    usu_apellido = models.CharField(max_length=100, blank=True, null=True)
    usu_documento = models.IntegerField()
    usu_email = models.CharField(max_length=100)
    usu_telefono = models.IntegerField(blank=True, null=True)
    usu_login = models.CharField(max_length=50, blank=True, null=True)
    usu_clave = models.CharField(max_length=50, blank=True, null=True)
    usu_estado = models.BooleanField(blank=True, null=True)
    usu_fechacreacion = models.DateTimeField(blank=True, null=True)
    usu_fechamodificacion = models.DateTimeField(blank=True, null=True)
    per_codigo = models.ForeignKey('Perfil', models.DO_NOTHING, db_column='per_codigo', blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'conjunto'
        db_table = 'usuario'