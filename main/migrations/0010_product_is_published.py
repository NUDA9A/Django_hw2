# Generated by Django 5.0.3 on 2024-04-28 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_product_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Статус публикации'),
        ),
    ]
