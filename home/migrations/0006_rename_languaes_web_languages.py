# Generated by Django 4.0.2 on 2022-03-07 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_web'),
    ]

    operations = [
        migrations.RenameField(
            model_name='web',
            old_name='languaes',
            new_name='languages',
        ),
    ]