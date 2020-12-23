from django.db import models
from jsonfield import JSONField

from scores.models.Round import Round
from teams.models.Team import Team


class TeamScore(models.Model):
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    round = models.ForeignKey(Round, on_delete=models.PROTECT)
    cumulative_score = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    cisco_score = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    image_score = models.DecimalField(decimal_places=2, max_digits=5, null=True)
    individual_scores = JSONField(blank=True, null=True)
    division_rank = models.IntegerField(null=True)
    state_rank = models.IntegerField(null=True)

    class Meta:
        unique_together = ('team', 'round', )
