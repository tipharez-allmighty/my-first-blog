# Generated by Django 4.2.14 on 2024-08-10 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0012_rename_postdocuments_postdocument"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postdocument",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="document",
                to="blog.post",
            ),
        ),
    ]
