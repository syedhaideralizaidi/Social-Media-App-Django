# Generated by Django 4.2.3 on 2023-07-26 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base", "0004_follow_date"),
    ]

    operations = [
        migrations.AlterModelManagers(
            name="stream",
            managers=[
                ("stream", django.db.models.manager.Manager()),
            ],
        ),
        migrations.AlterField(
            model_name="follow",
            name="following",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="following",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
