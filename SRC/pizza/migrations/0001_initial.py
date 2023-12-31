# Generated by Django 4.2.8 on 2023-12-31 00:59

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="menu",
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
                ("nom", models.CharField(max_length=200)),
                ("ingredients", models.CharField(max_length=400)),
                ("prix", models.FloatField(default=0)),
                ("vegetarienne", models.BooleanField(default=False)),
            ],
        ),
    ]
