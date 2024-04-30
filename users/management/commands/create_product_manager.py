from django.core.management import BaseCommand
from django.contrib.auth.models import Group

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="Product@manager.ru",
            first_name="Product",
            last_name="Manager",
            is_staff=True,
            is_superuser=False
        )

        user.set_password("12345ProductManager12345")
        g = Group.objects.get(name="manager")
        user.groups.add(g)
        user.save()
