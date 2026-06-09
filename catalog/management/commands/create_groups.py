from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):

    help = "Создает группы и назначает права"

    def handle(self, *args, **kwargs):

        moderator_group, created = Group.objects.get_or_create(
            name="Модератор продуктов"
        )

        delete_product = Permission.objects.get(
            codename="delete_product"
        )

        can_unpublish = Permission.objects.get(
            codename="can_unpublish_product"
        )

        moderator_group.permissions.add(delete_product)
        moderator_group.permissions.add(can_unpublish)

        self.stdout.write(
            self.style.SUCCESS(
                "Группа 'Модератор продуктов' успешно создана"
            )
        )