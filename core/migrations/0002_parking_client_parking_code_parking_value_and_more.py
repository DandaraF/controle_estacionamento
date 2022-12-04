# Generated by Django 4.1.3 on 2022-12-04 17:12

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="parking",
            name="client",
            field=models.CharField(
                default="2022-12-04 14:11:20.220777", max_length=255
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="parking",
            name="code",
            field=models.UUIDField(
                default=uuid.UUID("4b16f1ab-6b05-4708-b189-b521f8b1ea31"),
                editable=False,
            ),
        ),
        migrations.AddField(
            model_name="parking",
            name="value",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="parking",
            name="date_output",
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name="parking",
            name="id",
            field=models.AutoField(
                auto_created=True, primary_key=True, serialize=False
            ),
        ),
    ]