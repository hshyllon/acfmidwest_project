# Generated by Django 2.0.13 on 2019-12-09 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Is Blog Published?'),
        ),
    ]
