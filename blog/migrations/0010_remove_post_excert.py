# Generated by Django 4.2.9 on 2024-02-22 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excert',
        ),
    ]
