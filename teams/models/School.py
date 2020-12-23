from django.db import models


class School(models.Model):
    name = models.CharField(max_length=64)
    district = models.CharField(max_length=64)
    street_address = models.CharField(max_length=128, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=3, default="CA")
    zip = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return self.name + " (" + self.district + ")"
