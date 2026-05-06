from django.db import models
import catalog


# Create your models here.
class Product(models.Model):
    name = (
        models.CharField(
            max_length=100,
            verbose_name="Наименование продукта",
            help_text="Введите наименование продукта",
        ),
    )
    description = (
        models.TextFieldField(
            verbose_name="Описание продукта",
            help_text="Введите описание продукта",
            blank=True,
            null=True,
        ),
    )
    photo = (
        models.ImageField(
            upload_to="catalog/photo",
            blank=True,
            null=True,
            verbose_name=" Фото продукта",
            help_text="Загрузите фото продукта",
        ),
    )
    category = (
        models.CharField(
            max_length=100,
            verbose_name="Категория продукта",
            help_text="Введите категорию продукта",
        ),
    )
    price = (
        models.IntegerField(
            max_length=50,
            verbose_name="Цена продукта",
            help_text="Введите цену продукта",
        ),
    )
    created_at = (
        models.DateField(
            max_length=10,
            verbose_name="Дата создания",
            help_text="Введите дату создания",
        ),
    )
    updated_at = models.DateField(
        max_length=10,
        verbose_name="Дата последнего изменения",
        help_text="Введите дату последнего изменения",
    )


class Meta:
    verbose_name = ("Наименование продукта",)
    verbose_name_plurul = "Наименование продуктов"
    ordering = ["name", "description", "category", "price", "updated_at", "created_at"]

    def __str__(self):
        return self.verbose_name


class Category(models.Model):
    name = (
        models.CharField(
            max_length=100,
            verbose_name="Название категории продукта",
            help_text="Введите Название категории продукта",
        ),
    )
    description = (
        models.TextField(
            verbose_name="Описание категории продукта",
            help_text="Введите описание категории продукта",
            blank=True,
            null=True,
        ),
    )


class Meta:
    verbose_name = ("Название категории продукта",)
    verbose_name_plurul = "Название категории продуктов"
    ordering = ["name", "description"]

    def __str__(self):
        return self.verbose_name


# наименование,описание, изображение, категория, цена  за покупку, дата  создания, дата последнего  изменения.
