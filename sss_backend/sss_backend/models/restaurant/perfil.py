from django.db import models


class Perfil(models.Model):
    per_codigo = models.AutoField(primary_key=True)
    per_nombre = models.CharField(max_length=100)
    per_fechacreacion = models.DateTimeField()
    est_codigo = models.ForeignKey('Estado', models.DO_NOTHING, db_column='est_codigo')

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'perfil'