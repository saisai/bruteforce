# Generated by Django 3.0.7 on 2020-06-18 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("django_celery_beat", "0012_periodictask_expire_seconds"),
        ("main", "0003_auto_20200618_0954"),
    ]

    operations = [
        migrations.DeleteModel(
            name="AnotherPeriodicTask",
        ),
        migrations.CreateModel(
            name="OtherPeriodicTask",
            fields=[],
            options={
                "proxy": True,
                "indexes": [],
                "constraints": [],
            },
            bases=("django_celery_beat.periodictask",),
        ),
    ]