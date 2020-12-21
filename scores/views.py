import pandas as pd
from django.http import Http404
from django.shortcuts import render

# Create your views here.
from scores.models.Round import Round
from teams.models import Team


def load_scores(request, round_id):
    try:
        round = Round.objects.get(pk=round_id)
    except Round.DoesNotExist:
        raise Http404("Round does not exist")

    file = round.scores_csv
    data = pd.read_csv(file, delimiter=",")
    return render(request, template_name="scores/load_scores.html", context={
        'round': str(round),
        'rows_ct': len(data),
        'teams_ct': Team.objects.count()
    })
