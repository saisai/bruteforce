# Generated by Django 3.1.1 on 2020-11-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0022_database_last_check_success"),
    ]

    operations = [
        migrations.AddField(
            model_name="database",
            name="dsn",
            field=models.TextField(blank=True, default="", null=True),
        ),
    ]
