# Generated by Django 4.2.9 on 2024-01-09 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_customuser_is_doctor_customuser_is_patient"),
    ]

    operations = [
        migrations.RemoveField(model_name="customuser", name="is_doctor",),
        migrations.RemoveField(model_name="customuser", name="is_patient",),
    ]
