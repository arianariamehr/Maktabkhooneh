# Generated by Django 4.2.9 on 2024-03-07 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date'], 'verbose_name_plural': 'Comments'},
        ),
    ]