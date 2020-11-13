# Generated by Django 3.0.8 on 2020-07-17 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0010_auto_20200710_1639"),
    ]

    operations = [
        migrations.RenameField(
            model_name="hash",
            old_name="is_finished",
            new_name="is_cracking",
        ),
        migrations.RemoveField(
            model_name="hash",
            name="brute_config",
        ),
        migrations.AddField(
            model_name="hash",
            name="brute_config",
            field=models.ManyToManyField(to="main.BruteConfig"),
        ),
        migrations.RemoveField(
            model_name="hash",
            name="dictionary",
        ),
        migrations.AddField(
            model_name="hash",
            name="dictionary",
            field=models.ManyToManyField(to="main.Dictionary"),
        ),
    ]