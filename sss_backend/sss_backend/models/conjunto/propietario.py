from django.db import models


class Propietario(models.Model):
    prop_codigo = models.BigAutoField(primary_key=True)
    tor_codigo = models.ForeignKey('Torre', models.DO_NOTHING, db_column='tor_codigo', blank=True, null=True)
    apto_codigo = models.ForeignKey('Apartamento', models.DO_NOTHING, db_column='apto_codigo', blank=True, null=True)
    per_codigo = models.ForeignKey('Persona', models.DO_NOTHING, db_column='per_codigo', blank=True, null=True)
    per_codigo_emer = models.ForeignKey('Persona', models.DO_NOTHING, db_column='per_codigo_emer', related_name='propietario_per_codigo_emer_set')

    class Meta:
        managed = False
        db_table = 'propietario'