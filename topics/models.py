from django.contrib.auth import get_user_model
from pytils.translit import slugify
from django.db import models

# Create your models here.
User = get_user_model()

class Topic(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', unique=True)
    description = models.CharField(max_length=3500, verbose_name='Описание')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Создатель темы')
    slug = models.SlugField(default='', null=False)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Topic, self).save(*args, **kwargs)

    def __str__(self):
        return self.title


class Message(models.Model):
    text = models.CharField(max_length=3500, verbose_name='Текст')
    create_date = models.DateTimeField(auto_now=True, verbose_name='Дата публикации')
    author = models.ForeignKey(User, on_delete=models.PROTECT, verbose_name='Создатель публикации')

    def __str__(self):
        return str(self.author) + ' | ' + str(self.create_date)
