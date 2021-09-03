from django.urls import path

from . import views

app_name = "webtoon"

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:episode_id>/", views.detail, name="detail"),
]
