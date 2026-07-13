import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title, User

DATA_DIR = os.path.join(settings.BASE_DIR, 'static', 'data')


class Command(BaseCommand):
    help = 'Импорт данных из CSV-файлов'

    def handle(self, *args, **options):
        self._import_users()
        self._import_categories()
        self._import_genres()
        self._import_titles()
        self._import_genre_title()
        self._import_reviews()
        self._import_comments()
        self.stdout.write(self.style.SUCCESS('Импорт завершён успешно'))

    def _import_users(self):
        with open(
            os.path.join(DATA_DIR, 'users.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                User.objects.get_or_create(
                    id=row['id'],
                    defaults={
                        'username': row['username'],
                        'email': row['email'],
                        'role': row['role'],
                        'bio': row['bio'],
                        'first_name': row['first_name'],
                        'last_name': row['last_name'],
                    }
                )

    def _import_categories(self):
        with open(
            os.path.join(DATA_DIR, 'category.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                Category.objects.get_or_create(
                    id=row['id'],
                    defaults={'name': row['name'], 'slug': row['slug']}
                )

    def _import_genres(self):
        with open(
            os.path.join(DATA_DIR, 'genre.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                Genre.objects.get_or_create(
                    id=row['id'],
                    defaults={'name': row['name'], 'slug': row['slug']}
                )

    def _import_titles(self):
        with open(
            os.path.join(DATA_DIR, 'titles.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                category = Category.objects.get(id=row['category'])
                Title.objects.get_or_create(
                    id=row['id'],
                    defaults={
                        'name': row['name'],
                        'year': row['year'],
                        'category': category,
                    }
                )

    def _import_genre_title(self):
        with open(
            os.path.join(DATA_DIR, 'genre_title.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                title = Title.objects.get(id=row['title_id'])
                genre = Genre.objects.get(id=row['genre_id'])
                title.genre.add(genre)

    def _import_reviews(self):
        with open(
            os.path.join(DATA_DIR, 'review.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                author = User.objects.get(id=row['author'])
                Review.objects.get_or_create(
                    id=row['id'],
                    defaults={
                        'title_id': row['title_id'],
                        'text': row['text'],
                        'author': author,
                        'score': row['score'],
                        'pub_date': row['pub_date'],
                    }
                )

    def _import_comments(self):
        with open(
            os.path.join(DATA_DIR, 'comments.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                author = User.objects.get(id=row['author'])
                Comment.objects.get_or_create(
                    id=row['id'],
                    defaults={
                        'review_id': row['review_id'],
                        'text': row['text'],
                        'author': author,
                        'pub_date': row['pub_date'],
                    }
                )
