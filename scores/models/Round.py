from django.db import models
from jsonfield import JSONField


class Round(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    scores_csv = models.FileField()
    individual_challenges = JSONField(blank=True, null=True)
    col_team = models.CharField(max_length=64)
    col_division = models.CharField(max_length=64)
    col_state = models.CharField(max_length=64)
    col_cum = models.CharField(max_length=64)
    col_cisco = models.CharField(max_length=64)
    col_image = models.CharField(max_length=64)

    def __str__(self):
        return self.name
