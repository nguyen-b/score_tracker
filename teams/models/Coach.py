from django.db import models

from teams.models.School import School


class Coach(models.Model):
    last_name = models.CharField(max_length=64, verbose_name="Last Name")
    first_name = models.CharField(max_length=64, verbose_name="First Name")
    school = models.ForeignKey(School, on_delete=models.RESTRICT, verbose_name="School")
    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return self.first_name + " " + self.last_name
