# Generated by Django 2.1.7 on 2019-04-27 19:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_merge_20190417_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='answers',
            options={'verbose_name': 'answer', 'verbose_name_plural': 'answers'},
        ),
    ]