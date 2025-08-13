from django.db import models


class Estado(models.Model):
    est_codigo = models.AutoField(primary_key=True)
    est_nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'estado'