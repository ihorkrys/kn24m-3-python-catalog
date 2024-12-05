# import_books.py
import csv
import os

from transliterate import translit
from datetime import datetime

from catalog_app.models import Category, Item, ItemImage  # Replace 'myapp' with your actual app name
from cursova.settings import BASE_DIR


def import_csv(apps, schema_editor):
    category_model = apps.get_model('catalog_app', 'Category')
    item_model = apps.get_model('catalog_app', 'Item')
    item_image_model = apps.get_model('catalog_app', 'ItemImage')
    with open(os.path.join(BASE_DIR, 'data.csv'), 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            category = category_model.objects.filter(name=row['category']).first()
            if category is None:
                category = category_model.objects.create(name=row['category'], slug=translit(row['category'].lower(), reversed=True))
            item = item_model.objects.create(
                name=row['name'],
                description=row['description'],
                sku=row['article'],
                price=row['price'],
                stock=row['stock'],
                category=category,
                title_image='images/' + row['images'].split(',')[0].strip()
            )
            for image in row['images'].split(','):
                print(image.strip())
                item_image_model.objects.create(item_id=item.id, image='images/' + image.strip())