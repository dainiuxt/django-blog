# Generated by Django 4.0.4 on 2022-05-10 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blogpost_options_alter_comment_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Publication time'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='pub_time',
            field=models.DateTimeField(auto_now_add=True, null=True, verbose_name='Publication time'),
        ),
    ]
