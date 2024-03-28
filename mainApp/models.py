from django.contrib.auth.models import User
from django.db import models


class Muallif(models.Model):
    ism = models.CharField(max_length=100)
    yosh = models.IntegerField()
    kasb = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism


class Maqola(models.Model):
    sarlavha = models.CharField(max_length=255)
    sana = models.DateField()
    maqola_mavzusi = models.CharField(max_length=255)
    matn = models.TextField()
    muallif = models.ForeignKey(Muallif, on_delete=models.CASCADE)

    def __str__(self):
        return self.sarlavha
