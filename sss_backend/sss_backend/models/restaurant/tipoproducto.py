from django.db import models


class Tipoproducto(models.Model):
    tipprod_codigo = models.AutoField(primary_key=True)
    tipprod_nombre = models.CharField(max_length=100)

    class Meta:
        managed = False
        app_label = 'restaurant'
        db_table = 'tipoproducto'