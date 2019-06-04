# Generated by Django 2.2.1 on 2019-06-04 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0010_auto_20190427_2206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='response',
            options={'verbose_name': 'response', 'verbose_name_plural': 'responses'},
        ),
        migrations.AddField(
            model_name='questions',
            name='required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='response',
            name='survey',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Survey'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='response',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='survey',
            name='title',
            field=models.CharField(default='test', max_length=50),
        ),
        migrations.AlterField(
            model_name='answers',
            name='answer',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='answers',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='response',
            unique_together={('survey', 'user')},
        ),
    ]
