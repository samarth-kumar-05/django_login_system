# Generated by Django 4.2.9 on 2024-01-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_doctor",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="customuser",
            name="is_patient",
            field=models.BooleanField(default=False),
        ),
    ]
