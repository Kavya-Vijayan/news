# Generated by Django 4.1.2 on 2022-10-29 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_topstorymodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="SportModel",
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
                ("name", models.CharField(max_length=64)),
                ("description", models.TextField(max_length=800)),
                (
                    "image",
                    models.ImageField(
                        default="default/sport.png", upload_to="sport/image/"
                    ),
                ),
                ("status", models.BooleanField(default=True)),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateTimeField(auto_now=True)),
                ("category", models.ManyToManyField(to="core.categorymodel")),
            ],
        ),
    ]
