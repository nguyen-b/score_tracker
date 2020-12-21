from django.db import models
from jsonfield import JSONField

from scores.models.Round import Round
from teams.models.Team import Team


class TeamScore(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    round = models.ForeignKey(Round, on_delete=models.PROTECT)
    cumulative_score = models.DecimalField(decimal_places=2, max_digits=5)
    cisco_score = models.DecimalField(decimal_places=2, max_digits=5)
    image_score = models.DecimalField(decimal_places=2, max_digits=5)
    individual_scores = JSONField(blank=True, null=True)
    total_rank = models.IntegerField()
    state_rank = models.IntegerField()
