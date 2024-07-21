# Generated by Django 5.0.6 on 2024-07-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_alter_product_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("GC", "Compost"),
                    ("CB", "Bag"),
                    ("RC", "Cloth"),
                    ("SP", "Charger"),
                    ("UB", "Bottle"),
                    ("BC", "Cover"),
                ],
                max_length=2,
            ),
        ),
    ]
