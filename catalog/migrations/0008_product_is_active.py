# Generated by Django 4.2 on 2024-06-15 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0007_alter_product_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="is_active",
            field=models.BooleanField(default=True, verbose_name="Активен"),
        ),
    ]
