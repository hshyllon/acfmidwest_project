# Generated by Django 2.0.13 on 2019-12-16 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20191215_1846'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcomment',
            name='email',
            field=models.EmailField(blank=True, default='default@thissite.com', max_length=254),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='fullname',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
