# Generated by Django 5.0.3 on 2024-03-15 12:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("lecture", "0002_alter_lecture_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="lecture",
            name="content",
            field=models.FileField(upload_to=""),
        ),
    ]
