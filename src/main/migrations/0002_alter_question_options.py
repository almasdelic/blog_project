# Generated by Django 4.2.3 on 2023-07-10 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'The Question', 'verbose_name_plural': 'Peoples Questions'},
        ),
    ]