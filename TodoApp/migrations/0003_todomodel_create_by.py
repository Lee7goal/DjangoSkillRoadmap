# Generated by Django 4.0.6 on 2022-07-31 16:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('TodoApp', '0002_alter_todomodel_long_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='todomodel',
            name='create_by',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
