# Generated by Django 4.1.2 on 2022-10-28 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_remove_lateststorymodel_price"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lateststorymodel",
            name="description",
            field=models.TextField(max_length=800),
        ),
    ]
