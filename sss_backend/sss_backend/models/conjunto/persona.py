from django.db import models


class Persona(models.Model):
    per_codigo = models.BigAutoField(primary_key=True)
    per_nombre = models.CharField(max_length=100, blank=True, null=True)
    per_documento = models.IntegerField()
    per_telefono = models.IntegerField(blank=True, null=True)
    per_email = models.CharField(max_length=100)
    per_fechacreacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        app_label = 'conjunto'
        db_table = 'persona'