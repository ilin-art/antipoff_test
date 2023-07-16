from django.db import models


class Cadastre(models.Model):
    cadastre_number = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    result = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
