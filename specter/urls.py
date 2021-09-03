from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("webtoon/", include("webtoon.urls")),
]
