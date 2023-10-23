from secrets import token_urlsafe
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from safedelete import DELETED_VISIBLE_BY_PK, SOFT_DELETE_CASCADE
from safedelete.managers import SafeDeleteManager
from safedelete.models import SafeDeleteModel


def token():
    return token_urlsafe(10)

class Notemanager(SafeDeleteManager):
    _safedelete_visibility = DELETED_VISIBLE_BY_PK

class Note(SafeDeleteModel):
    deleted_by_cascade = True
    _safedelete_policy = SOFT_DELETE_CASCADE
    slug = models.CharField(max_length=16, unique=True, default=token())
    name = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200)
    obj = Notemanager()
    text = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})


