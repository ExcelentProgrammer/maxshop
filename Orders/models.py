from django.db import models


class Orders(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    product = models.CharField(max_length=255)
    stream = models.URLField(max_length=255)
