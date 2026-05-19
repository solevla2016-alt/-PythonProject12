from django.db import models
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название категории продукта",
        help_text="Введите название категории продукта",
        default="Введите название",
    )
    description = models.TextField(
        verbose_name="Описание категории продукта",
        help_text="Введите описание категории продукта",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Название категории продукта"
        verbose_name_plural = "Названия категорий продуктов"
        ordering = ["name", "description"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
        blank=True,
        null=True,
    )
    photo = models.ImageField(
        upload_to="catalog/photo/",
        blank=True,
        null=True,
        verbose_name="Фото продукта",
        help_text="Загрузите фото продукта",
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Выберите категорию продукта",
        blank=True,
        null=True,
        related_name="photo",
    )
    price = models.IntegerField(
        verbose_name="Цена продукта", help_text="Введите цену продукта", default=0
    )
    created_at = models.DateField(
        verbose_name="Дата создания",
        help_text="Введите дату создания",
        default=timezone.now,
    )
    updated_at = models.DateField(
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
        default=timezone.now,
    )

    class Meta:
        verbose_name = "Наименование продукта"
        verbose_name_plural = "Наименования продуктов"
        ordering = ["name", "category", "price", "updated_at", "created_at"]

    def __str__(self):
        return self.name


class Contact(models.Model):
    city = models.CharField(max_length=100, verbose_name="Город")
    phone = models.CharField(max_length=30, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    address = models.TextField(verbose_name="Адрес", blank=True)

    def __str__(self):
        return self.city
