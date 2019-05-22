from django.db import models
from django.urls import reverse
import datetime


# Create your models here.

class Article(models.Model):
    article_title = models.CharField(max_length=250)
    article_text = models.TextField(default="A bunch of Stuff")
    article_summary = models.CharField(max_length=110)
    article_author = models.CharField(max_length=250)
    article_created = models.DateField(default=datetime.date.today)
    article_last_update = models.DateField(default=datetime.date.today)
    article_upvotes = models.IntegerField(default=0)
    article_downvotes = models.IntegerField(default=0)
    article_comments = models.IntegerField(default=0)
    article_views = models.IntegerField(default=0)
    article_tags = models.CharField(max_length=250, default="#code")
    image = models.FileField(default=None)

    def get_absolute_url(self):
        return reverse('article:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.pk) + "-" + self.article_title

class Comments(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True)
    user = models.CharField(max_length=250)
    comment = models.TextField(default="A bunch of Stuff")
    comment_date = models.DateField(default=datetime.date.today)

    def __str__(self):
        return self.comment