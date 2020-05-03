from django.db import models
from django.utils import timezone
from django.conf import settings


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    tag = models.CharField(max_length=60)
    text = models.TextField()
    image = models.ImageField(upload_to ='', default='default.jfif', help_text='Загрузить изображение', blank=True, null=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    @property
    def formatted_date(self):
        return self.created_date.strftime('%d %B %Y %H:%M')

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)


class View(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='views')
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


class Like(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    author = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
