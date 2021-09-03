from django.shortcuts import render

from webtoon.models import Episode
from crawler import get_episodes, DetailPage


def index(request):
    episode_list = Episode.objects.order_by("-date")
    context = {"episode_list": episode_list}
    return render(request, "webtoon/episode_list.html", context)


def detail(request, episode_id):
    episode = Episode.objects.get(id=episode_id)
    episode_detail_page = DetailPage.objects.filter(episode=episode)
    return render(request, "webtoon/episode_detail.html", context={"episode_detail_page": episode_detail_page, "episode": episode})
