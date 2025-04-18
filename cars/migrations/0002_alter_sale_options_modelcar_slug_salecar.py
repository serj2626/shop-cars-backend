# Generated by Django 5.0.7 on 2025-03-09 10:44

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cars", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="sale",
            options={"verbose_name": "Типы акций", "verbose_name_plural": "Типы акций"},
        ),
        migrations.AddField(
            model_name="modelcar",
            name="slug",
            field=models.SlugField(
                blank=True, null=True, unique=True, verbose_name="Слаг"
            ),
        ),
        migrations.CreateModel(
            name="SaleCar",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                (
                    "car",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cars.car",
                        verbose_name="Машина",
                    ),
                ),
                (
                    "sale",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cars.sale",
                        verbose_name="Акция",
                    ),
                ),
            ],
            options={
                "verbose_name": "Акция",
                "verbose_name_plural": "Акции",
            },
        ),
    ]
