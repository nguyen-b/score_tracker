from django.db import models

from teams.models.School import School


class Coach(models.Model):
    last_name = models.CharField(max_length=64, description="Last Name")
    first_name = models.CharField(max_length=64, description="First Name")
    school = models.ForeignKey(School, on_delete=models.RESTRICT, description="School")
    email = models.EmailField(description="Email")

    def __str__(self):
        return self.first_name + " " + self.last_name
