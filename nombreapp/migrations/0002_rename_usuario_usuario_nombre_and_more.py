# Generated by Django 4.2.4 on 2023-09-15 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nombreapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='usuario',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='creditos',
        ),
    ]
