# Generated by Django 4.2.9 on 2024-02-25 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='avatar',
            field=models.ImageField(default='/blog/avatar/default.png', upload_to='blog/avatar'),
        ),
    ]