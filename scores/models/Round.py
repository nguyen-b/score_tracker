from django.db import models
from jsonfield import JSONField


class Round(models.Model):
    name = models.CharField(max_length=64)
    start_date = models.DateField()
    end_date = models.DateField()
    scores_csv = models.FileField()
    individual_challenges = JSONField(blank=True, null=True)

    def __str__(self):
        return self.name