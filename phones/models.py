from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=60)
    price = models.PositiveIntegerField()
    image = models.CharField(max_length=120)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.CharField(max_length=60)

