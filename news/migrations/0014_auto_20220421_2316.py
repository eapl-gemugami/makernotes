# Generated by Django 2.2.5 on 2022-04-21 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0013_auto_20220421_1842'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='story',
            options={'verbose_name_plural': 'stories'},
        ),
    ]