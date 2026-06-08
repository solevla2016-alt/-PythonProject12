from django.core.management import call_command
from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Очистка базы и загрузка фикстур"

    def handle(self, *args, **options):

        # очистка базы
        Product.objects.all().delete()
        Category.objects.all().delete()

        # загрузка фикстур
        call_command("loaddata", "category_fixture.json")
        call_command("loaddata", "products_fixture.json")

        self.stdout.write(self.style.SUCCESS("Данные загружены из фикстур"))
