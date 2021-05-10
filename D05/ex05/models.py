from django.db import models


class Movies(models.Model):
    title = models.CharField(max_length=64, blank=False)
    episode_nb = models.AutoField(primary_key=True)
    opening_crawl = models.TextField()
    director = models.CharField(max_length=32, blank=False)
    producer = models.CharField(max_length=128, blank=False)
    release_date = models.DateField(blank=False)

    def __str__(self):
        return self.title
