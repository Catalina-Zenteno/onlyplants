# Generated by Django 4.2.4 on 2023-09-16 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nombreapp', '0003_usuario_correo_alter_usuario_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='correo',
            field=models.EmailField(default='@gmail.com', max_length=300),
        ),
    ]
