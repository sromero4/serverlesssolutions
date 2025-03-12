from django.db import models


class Habitante(models.Model):
    hab_codigo = models.IntegerField(primary_key=True)
    prop_codigo = models.ForeignKey('Propietario', models.DO_NOTHING, db_column='prop_codigo', blank=True, null=True)
    per_codigo = models.ForeignKey('Persona', models.DO_NOTHING, db_column='per_codigo', blank=True, null=True)
    hab_placa = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'habitante'