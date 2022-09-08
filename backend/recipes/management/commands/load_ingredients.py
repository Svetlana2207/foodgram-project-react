import json

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str)

    def handle(self, *args, **options):
        with open(options['file_path'], 'r', encoding='utf-8') as f:
            data = json.load(f)
            for i in data:
                Ingredient.objects.create(
                    name=i['name'],
                    measurement_unit=i['measurement_unit']
                )
                print(i['name'], i['measurement_unit'])
