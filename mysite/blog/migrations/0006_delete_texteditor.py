# Generated by Django 4.0.4 on 2022-05-11 15:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_texteditor_title'),
    ]

    operations = [
        migrations.DeleteModel(
            name='textEditor',
        ),
    ]
