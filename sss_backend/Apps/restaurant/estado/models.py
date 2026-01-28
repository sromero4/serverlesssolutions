from django.db import models


class Estado(models.Model):
    est_codigo = models.AutoField(primary_key=True)
    est_nombre = models.CharField(max_length=100)

    
    def __str__(self):
        return self.est_nombre