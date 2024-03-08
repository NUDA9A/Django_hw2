from django.core.management import BaseCommand
import json

from main.models import Category, Product


class Command(BaseCommand):

    @staticmethod
    def get_json_product():
        with open('./dumped_data/product_dump.json', encoding='utf-8') as file:
            data = json.load(file)
            return data

    @staticmethod
    def get_json_category():
        with open('./dumped_data/category_dump.json', encoding='utf-8') as file:
            data = json.load(file)
            return data

    def handle(self, *args, **kwargs):
        #Так как продукты связаны с категориями при удалении категории удаляются и продукты с этой категорией
        Category.objects.all().delete()

        category_for_create = []
        product_for_create = []

        for category in Command.get_json_category():
            category_for_create.append(Category(category['pk'], category['fields']['name'], category['fields']['description']))

        Category.objects.bulk_create(category_for_create)

        for product in Command.get_json_product():
            product_for_create.append((Product(
                id=product['pk'],
                name=product['fields']['name'],
                description=product['fields']['description'],
                category=Category.objects.get(pk=product['fields']['category']),
                price=product['fields']['price']
            )))

        Product.objects.bulk_create(product_for_create)
