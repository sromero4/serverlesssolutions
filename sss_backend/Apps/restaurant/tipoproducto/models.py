from django.db import models


class Tipoproducto(models.Model):
    tipprod_codigo = models.AutoField(primary_key=True)
    tipprod_nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipprod_nombre