# Generated by Django 5.0.7 on 2024-07-19 05:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        (
            "lostandfound",
            "0002_alter_founditem_options_alter_lostitem_options_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="founditem",
            name="description",
        ),
        migrations.RemoveField(
            model_name="founditem",
            name="user",
        ),
        migrations.RemoveField(
            model_name="lostitem",
            name="description",
        ),
        migrations.RemoveField(
            model_name="lostitem",
            name="user",
        ),
    ]
