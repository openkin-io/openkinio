# Generated by Django 5.0.3 on 2024-05-25 16:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="birth_place_object_id",
            field=models.PositiveIntegerField(null=True),
        ),
    ]
