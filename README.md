# webtoon_crawling

<br>

1. git clone

```
git clone https://github.com/banana1019/webtoon.git
```

2. requirements.txt에 있는 라이브러리를 설치해 주세요.

```
pip install -r requirements.txt
```

3. my_settings.py 파일 수정 후 migrate 진행해 주세요.

DB는 MySQL을 사용했으며 DB NAME은 "specter" 입니다. 
my_settings.py 에서 DATABASES 부분을 본인 PASSWORD로 변경해 주세요.

```
# my_settings.py
SECRET_KEY = "django-insecure-hn89f1pcy$438t96i)0-!3^ftw9hfpd%l=qia4i^@ef*)m*!ns"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "specter",
        "USER": "root",
        "PASSWORD": "본인 것으로 변경",
        "HOST": "127.0.0.1",
        "PORT": "3306",
    }
}
```

my_settings.py 파일 수정이 완료되었으면 migrate를 진행해 주세요.

```
python manage.py migrate
```

4. crawler.py 파일을 먼저 실행해 주세요. 저는 3분 45초 정도 걸렸습니다.

```
python crawler.py
```

크롤링이 완료되면 "모든 크롤링이 완료되었습니다." 라는 문구가 뜹니다. 조금만 기다려 주세요.

5. 서버를 실행시킵니다.

```
python manage.py runserver
```

6. http://127.0.0.1:8000/webtoon/ 로 접속하시면 웹툰 회차 리스트 페이지가 나옵니다.