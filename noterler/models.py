from django.db import models


# from django.utils import timezone


class Noterler(models.Model):
    noterIli = models.CharField(max_length=255)
    noterAdi = models.CharField(max_length=255)
    noterAdiSoyadi = models.CharField(max_length=255)
    noterlikSinifi = models.IntegerField()
    noterSinifi = models.IntegerField()
    noterAsilVekil = models.CharField(max_length=2)
    noterTelefonu = models.CharField(max_length=16)
    noterFaksi = models.CharField(max_length=16)
    noterAdresi = models.CharField(max_length=255)
    noterHarita = models.CharField(max_length=2080)
