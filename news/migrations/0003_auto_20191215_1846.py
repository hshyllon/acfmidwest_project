# Generated by Django 2.0.13 on 2019-12-16 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_blog_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='blog',
            field=models.IntegerField(default=1),
        ),
    ]
