# Generated by Django 4.0.6 on 2022-07-11 05:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Personas',
            new_name='Persona',
        ),
    ]