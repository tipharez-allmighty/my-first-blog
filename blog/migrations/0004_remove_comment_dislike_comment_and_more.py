# Generated by Django 4.2.14 on 2024-08-05 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_remove_comment_approved_comment_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="comment",
            name="dislike_comment",
        ),
        migrations.RemoveField(
            model_name="comment",
            name="like_comment",
        ),
        migrations.AddField(
            model_name="comment",
            name="approved_comment",
            field=models.BooleanField(default=False),
        ),
    ]
