from django.db import models


class Episode(models.Model):
    thumbnail = models.URLField(max_length=2000)
    title = models.CharField(max_length=100)
    date = models.DateField()

    class Meta:
        db_table = "episodes"


class DetailPage(models.Model):
    episode = models.ForeignKey("Episode", on_delete=models.CASCADE)
    image_url = models.URLField(max_length=2000)

    class Meta:
        db_table = "detail_pages"
