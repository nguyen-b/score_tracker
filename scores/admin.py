import pandas as pd
from django.contrib import admin

# Register your models here.
from scores.models import Round, TeamScore
from teams.models import Team


class RoundAdmin(admin.ModelAdmin):
    list_display = ['name', 'start_date', 'end_date']
    ordering = ['name']
    actions = ['load_scores']

    def load_scores(self, request, queryset):
        messages = []

        for rd in queryset:
            message = rd.name

            file = rd.scores_csv
            data = pd.read_csv(file, delimiter=",")
            # Calculate total rank based on division
            data['division_rank'] = data.groupby(rd.col_division)[rd.col_cum].rank(method='min', ascending=False)
            data['state_rank'] = data.groupby(rd.col_state)[rd.col_cum].rank(method='min', ascending=False)

            # Filter out only teams in our database
            teams_list = Team.objects.values_list('team_id', flat=True)
            df_teams = data[data[rd.col_team].isin(teams_list)]
            print(df_teams)

            # Initialize counters
            update_ct = 0
            create_ct = 0

            # Add to database
            for i, row in df_teams.iterrows():
                obj, created = TeamScore.objects.update_or_create(team=Team.objects.get(team_id=row[rd.col_team]),
                                                                  round=rd,
                                                                  defaults={
                                                                      'cumulative_score': row[rd.col_cum],
                                                                      'cisco_score': row[rd.col_cisco],
                                                                      'image_score': row[rd.col_image],
                                                                      'division_rank': row['division_rank'],
                                                                      'state_rank': row['state_rank'],
                                                                  })
                if created:
                    create_ct += 1
                else:
                    update_ct += 1

            message += f" (Updated {update_ct}, Created {create_ct})"
            messages.append(message)

        self.message_user(request, " | ".join(messages))


admin.site.register(Round, RoundAdmin)

