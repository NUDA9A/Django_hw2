# Generated by Django 5.0.3 on 2024-04-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_country_alter_user_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='verification_code',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Ключ верификации'),
        ),
    ]