# Generated by Django 3.1 on 2020-09-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0021_otherperiodictask"),
    ]

    operations = [
        migrations.AddField(
            model_name="database",
            name="last_check_success",
            field=models.BooleanField(default=True),
        ),
    ]