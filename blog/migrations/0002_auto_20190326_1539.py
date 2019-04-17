# Generated by Django 2.1.7 on 2019-03-26 12:39

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='active',
            field=models.BooleanField(default=1, verbose_name='is_published'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(default=1, on_delete=models.SET(0), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]