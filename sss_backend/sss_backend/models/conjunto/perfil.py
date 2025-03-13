from django.db import models


class Perfil(models.Model):
    per_codigo = models.BigAutoField(primary_key=True)
    per_nombre = models.CharField(max_length=100, blank=True, null=True)
    per_fechacreacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'conjunto'
        db_table = 'perfil'