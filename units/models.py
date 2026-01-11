from django.db import models


class Unit(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
