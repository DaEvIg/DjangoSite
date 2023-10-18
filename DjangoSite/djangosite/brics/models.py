from secrets import token_urlsafe
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


def token():
    return token_urlsafe(10)

class Note(models.Model):
    slug = models.CharField(max_length=16, unique=True, default=token())
    name = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    text = models.TextField()


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


