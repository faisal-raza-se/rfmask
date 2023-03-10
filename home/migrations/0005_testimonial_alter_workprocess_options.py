# Generated by Django 4.1.5 on 2023-01-23 23:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_workprocess"),
    ]

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                ("name", models.CharField(max_length=100)),
                ("profession", models.CharField(max_length=100)),
                ("body", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        upload_to="post",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                ["png", "jpg", "jpeg"]
                            )
                        ],
                    ),
                ),
            ],
        ),
        migrations.AlterModelOptions(
            name="workprocess", options={"ordering": ("id",)},
        ),
    ]
