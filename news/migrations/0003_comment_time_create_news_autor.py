# Generated by Django 4.2.7 on 2023-12-18 20:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("news", "0002_alter_images_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="time_create",
            field=models.DateTimeField(
                auto_now_add=True, null=True, verbose_name="Дата публикация"
            ),
        ),
        migrations.AddField(
            model_name="news",
            name="autor",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
    ]
