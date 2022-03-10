from django.db import models

# Create your models here.

class Bolig(models.Model):
    address = models.CharField(max_length=100)
    desc = models.TextField
    lat = models.DecimalField(max_digits=9, decimal_places=6)



