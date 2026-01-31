from django.db import models

from Apps.restaurant.estado.models import Estado
from Apps.restaurant.usuario.models import Usuario

class Producto(models.Model):
    prod_codigo = models.AutoField(primary_key=True)
    prod_nombre = models.CharField(max_length=100)
    prod_descripcion = models.TextField(blank=True, null=True)
    prod_precio = models.DecimalField(max_digits=10, decimal_places=2)
    prod_imagen = models.CharField(max_length=255, blank=True, null=True)
    prod_fechacreacion = models.DateTimeField()
    prod_fechamodificacion = models.DateTimeField(blank=True, null=True)
    est_codigo = models.ForeignKey(Estado, models.DO_NOTHING)
    usu_codigo = models.ForeignKey(Usuario, models.DO_NOTHING)

    def __str__(self):
        return self.prod_nombre