# Generated by Django 5.0.3 on 2024-03-22 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='slug',
        ),
    ]