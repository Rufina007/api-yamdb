import datetime
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.db import models

User = get_user_model()


class Category(models.Model):  # категория
    name = models.CharField(  # название категории
        max_length=256,
        verbose_name='Название'
    )
    slug = models.SlugField(  # слаг
        max_length=50,
        unique=True,
        verbose_name='Слаг'
    )

    def __str__(self):
        return self.name


class Genre(models.Model):  # жанр
    name = models.CharField(  # название жанра
        max_length=256,
        verbose_name='Название'
    )
    slug = models.SlugField(  # слаг
        max_length=50,
        unique=True,
        verbose_name='Слаг'
    )

    def __str__(self):
        return self.name


class Title(models.Model):  # произведение
    title = models.CharField(  # название
        max_length=256,
        verbose_name='Название')
    year = models.IntegerField(  # год выхода + чтобы не следующий
        validators=[MaxValueValidator(datetime.datetime.now().year)], verbose_name='Год выпуска'
    )
    description = models.TextField(  # описание
        blank=True,
        null=True,
        verbose_name='Описание')
    genre = models.ManyToManyField(  # связь с жанрами
        Genre, related_name='titles',
        on_delete=models.SET_NULL,
        verbose_name='Жанр')
    category = models.ForeignKey(  # связь с категориями
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.title
