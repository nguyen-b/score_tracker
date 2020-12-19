from django.core.validators import RegexValidator
from django.db import models

from teams.models.Coach import Coach


class Team(models.Model):
    class TeamDivisionChoices(models.Choices):
        HS = "Open Division"
        MS = "Middle School"
        AS = "All Service"

    team_id = models.CharField(max_length=7, description="Team ID", validators=[RegexValidator(r'\d{2}-\d{4}')])
    unique_id = models.CharField(max_length=19, description="Unique ID",
                                 validators=[RegexValidator(r'[A-z0-9]{4}(?:-[A-z0-9]{4}){3}')])
    coach = models.ForeignKey(Coach, on_delete=models.RESTRICT, description="Coach")
    division = TeamDivisionChoices.choices

    def __str__(self):
        return self.team_id + "(" + self.coach.school.name + ")"
