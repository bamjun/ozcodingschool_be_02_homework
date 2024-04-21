# Generated by Django 5.0.4 on 2024-04-12 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tabom", "0001_initial"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="like",
            constraint=models.UniqueConstraint(fields=("user", "article"), name="unique_user_article"),
        ),
    ]