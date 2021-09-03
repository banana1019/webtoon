# webtoon_crawling

<br>

1. requirements.txt에 있는 라이브러리를 설치해 주세요.

```
pip install -r requirements.txt
```

2. DB를 생성해 주세요.

```
python manage.py migrate
```

3. crawler.py 파일을 먼저 실행해 주세요. 저는 3분 45초 정도 걸렸습니다.

```
python crawler.py
```

크롤링이 완료되면 "모든 크롤링이 완료되었습니다." 라는 문구가 뜹니다. 조금만 기다려 주세요.

4. 서버를 실행시킵니다.

```
python manage.py runserver
```

5. http://127.0.0.1:8000/webtoon/ 로 접속하시면 웹툰 회차 리스트 페이지가 나옵니다.