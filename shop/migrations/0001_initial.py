# Generated by Django 4.1 on 2024-01-04 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CategoryModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=6)),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
        migrations.CreateModel(
            name="ProductModule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("pCategory", models.CharField(max_length=20)),
                ("price", models.IntegerField()),
                ("brand", models.CharField(max_length=10)),
                ("reward_points", models.IntegerField()),
                ("description", models.TextField()),
                ("size", models.TextField()),
                ("color", models.TextField()),
                ("image", models.ImageField(upload_to="Products")),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="shop.categorymodule",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Products",
            },
        ),
    ]
