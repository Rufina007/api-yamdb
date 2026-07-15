import csv
import os

from django.conf import settings
from django.core.management.base import BaseCommand

from reviews.models import Category, Comment, Genre, Review, Title, User

DATA_DIR = os.path.join(settings.BASE_DIR, 'static', 'data')

IMPORT_ORDER = [
    ('users.csv', User, {}),
    ('category.csv', Category, {}),
    ('genre.csv', Genre, {}),
    ('titles.csv', Title, {'category': 'category_id'}),
    ('review.csv', Review, {'author': 'author_id'}),
    ('comments.csv', Comment, {'author': 'author_id'}),
]


class Command(BaseCommand):
    help = 'Импорт данных из CSV-файлов'

    def handle(self, *args, **options):
        for filename, model, renames in IMPORT_ORDER:
            self._import(filename, model, renames)
        self._link_genres()
        self.stdout.write(self.style.SUCCESS('Импорт завершён успешно'))

    def _import(self, filename, model, renames):
        with open(
            os.path.join(DATA_DIR, filename), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                for old, new in renames.items():
                    row[new] = row.pop(old)
                obj_id = row.pop('id')
                model.objects.get_or_create(id=obj_id, defaults={**row})

    def _link_genres(self):
        with open(
            os.path.join(DATA_DIR, 'genre_title.csv'), encoding='utf-8'
        ) as f:
            for row in csv.DictReader(f):
                Title.objects.get(
                    id=row['title_id']
                ).genre.add(row['genre_id'])
