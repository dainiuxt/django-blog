# Generated by Django 4.0.4 on 2022-05-11 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blogpost_pub_time_alter_comment_pub_time'),
    ]

    operations = [
        migrations.CreateModel(
            name='textEditor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('content', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-pub_time',), 'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
    ]
