from django.db import models


class Torre(models.Model):
    tor_codigo = models.BigAutoField(primary_key=True)
    tor_nombre = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'torre'