from django.urls import path

from . import views

urlpatterns = [
    path('load_scores/<int:round_id>/', views.load_scores),
]
