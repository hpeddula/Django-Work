# Generated by Django 2.0.1 on 2018-01-14 04:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20180113_1751'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['date_of_birth']},
        ),
    ]