import requests
from bs4 import BeautifulSoup

import datetime
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "specter.settings")
import django

django.setup()

from webtoon.models import Episode, DetailPage

URL = "https://m.comic.naver.com/webtoon/list?titleId=650305&page="


def extract_pages():
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"class": "paging_type2"})
    pages = pagination.find("span", {"class": "total"})
    pages = int(pages.string)
    return pages


def extract_episode_data(html):
    thumbnail = html.find("div", {"class": "thumbnail"}).find("img")["src"]
    print("♥ thumbnail :", thumbnail)
    title = html.find("span", {"class": "name"}).get_text(strip=True)
    print("♥ title :", title)
    link = html.find("a", {"class": "link"})["href"]
    link = "https://m.comic.naver.com" + link
    print("♥ link :", link)
    
    detail_page = []
    no = link.split("&")[1]
    link = f"https://comic.naver.com/webtoon/detail?titleId=650305&{no}"
    result = requests.get(link)
    soup = BeautifulSoup(result.text, "html.parser")
    detail_imgs = soup.select("div.view_area div.wt_viewer img")
    for detail_img in detail_imgs:
        detail_page.append(detail_img["src"])
    
    date = html.find("span", {"class": "date"}).get_text(strip=True)
    date = ('20' + date).replace(".", "-")
    print("♥ date :", date)
    
    return {
        "thumbnail": thumbnail,
        "title": title,
        "date": date,
        "detail_page": detail_page,
    }


def extract_episodes(last_page):
    episodes = []
    n = 0
    for page in range(1, last_page + 1):
        result = requests.get(f"{URL}{page}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("li", {"class": "item", "data-title-id": "650305"})
        for result in results:
            if result.find("span", {"class": "date"}):
                episode = extract_episode_data(result)
                episodes.append(episode)
                n += 1
                print(f'{n} 번째 크롤링 완료')
            else:
                pass
            
    return episodes


def get_episodes():
    last_page = extract_pages()
    episodes = extract_episodes(last_page)
    return episodes


if __name__ == "__main__":
    episodes = list(reversed(get_episodes()))
    if len(episodes) > Episode.objects.count():
        results = episodes[-(len(episodes) - Episode.objects.count()):]
        for episode in results:
            Episode(
                thumbnail=episode["thumbnail"],
                title=episode["title"],
                date=episode["date"]
            ).save()
            for image in episode["detail_page"]:
                DetailPage(
                    episode = Episode.objects.last(),
                    image_url = image
                ).save()
    print("모든 크롤링이 완료되었습니다.")
