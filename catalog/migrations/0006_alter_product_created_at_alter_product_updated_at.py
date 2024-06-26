# Generated by Django 4.2 on 2024-06-14 17:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0005_product_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="created_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата создания"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="updated_at",
            field=models.DateTimeField(
                default=django.utils.timezone.now, verbose_name="Дата изменения"
            ),
        ),
    ]
