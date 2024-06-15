

from django.db import models
from django.utils import timezone

from users.models import User


class Category(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=70,
        verbose_name="Наименование",
        help_text="Введите название продукта",
    )
    description = models.TextField(
        blank=True, null=True, verbose_name="Описание", help_text="Введите описание"
    )
    photo = models.ImageField(
        upload_to="product/photo",
        blank=True,
        null=True,
        verbose_name="Фото",
        help_text="Загрузите фото",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите название категории",
        blank=True,
        null=True,
        related_name='products',
    )
    price = models.FloatField(
        verbose_name="Цена",
        help_text="Введите описание"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата создания')

    updated_at = models.DateTimeField(
        default=timezone.now,
        verbose_name='Дата изменения')

    manufactured_at = models.DateField(
        blank=True, null=True, verbose_name="Дата производства продукта"
    )
    is_active = models.BooleanField(default=True, verbose_name='Активен')

    slug = models.SlugField(
        blank=True,
        null=True,
        max_length=150,
        unique=True,
        verbose_name="slug"
    )

    viewed = models.IntegerField(
        default=0,
        verbose_name='Количество просмотров'
    )
    owner = models.ForeignKey(
        User, verbose_name='Владелец',
        help_text='укажите владельца продукта',
        blank=True,
        null=True,
        on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "category", "created_at", "updated_at"]
        permissions = [
            ("can_edit_category", "Edit Category"),
            ("can_edit_description", "Edit Description"),
            ("can_edit_is_active", "Edit Is Active")
        ]
    def __str__(self):
        return self.name


class Version(models.Model):
    """Версия продукта"""
    name = models.CharField(
        max_length=150,
        verbose_name='Наименование',
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Продукт',
        related_name='versions',
    )
    version_number = models.PositiveIntegerField(
        verbose_name='Номер версии',
    )
    is_actual = models.BooleanField(
        default=True,
        verbose_name='Актуальная',
    )

    def __str__(self):
        return f'{self.name}, версия - {self.version_number}'

    class Meta:
        verbose_name = 'Версия'
        verbose_name_plural = 'Версии'
        ordering = ['product', 'version_number']