# Generated by Django 4.2.2 on 2023-10-13 23:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("ads",
         "0002_alter_ad_options_alter_comment_options_ad_author_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_at",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
