# Generated by Django 2.2.16 on 2022-08-25 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20220825_2033'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
