from django.db import models

# Create your models here.

class WeddingInfo(models.Model):
    name = models.CharField(max_length=60)
    surname=models.CharField(max_length=60)
    alkhogol_preferens=models.CharField(max_length=250)
    other_important_information=models.TextField(null=True, blank=True)
    second_day=models.CharField(max_length=60)
    sauna=models.CharField(max_length=60)
    beer_preferens=models.CharField(max_length=250)
    other_information=models.TextField(null=True, blank=True)

