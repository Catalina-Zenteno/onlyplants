# Generated by Django 4.2.4 on 2023-09-16 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nombreapp', '0002_rename_usuario_usuario_nombre_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
