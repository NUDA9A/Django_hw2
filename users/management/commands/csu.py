from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.create(
            email="Admin@admin.ru",
            first_name="Admin",
            last_name="Adminov",
            is_staff=True,
            is_superuser=True
        )

        user.set_password("12345Admin12345")
        user.save()

