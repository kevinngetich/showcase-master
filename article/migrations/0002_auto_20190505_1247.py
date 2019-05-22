# Generated by Django 2.2 on 2019-05-05 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='article_created',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='article',
            name='article_last_update',
            field=models.DateField(default=datetime.date.today),
        ),
    ]