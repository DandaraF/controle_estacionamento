# Generated by Django 4.1.3 on 2022-12-04 17:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_parking_vehicle_alter_parking_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="parking",
            name="code",
            field=models.UUIDField(
                default=uuid.UUID("9d449820-9434-4af7-8e04-4595827d2d17"),
                editable=False,
            ),
        ),
        migrations.AlterField(
            model_name="parking",
            name="vehicle",
            field=models.CharField(
                choices=[
                    ("Carro", "Carro"),
                    ("Moto", "Moto"),
                    ("Caminhão", "Caminhão"),
                ],
                max_length=10,
            ),
        ),
    ]