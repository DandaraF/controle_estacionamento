# Generated by Django 4.1.3 on 2022-12-03 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Parking",
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
                ("plate", models.CharField(max_length=8)),
                ("paid", models.BooleanField(default=False)),
                ("left", models.BooleanField(default=False)),
                ("date_input", models.DateTimeField(auto_now_add=True)),
                ("date_output", models.DateTimeField(null=True)),
            ],
        ),
    ]