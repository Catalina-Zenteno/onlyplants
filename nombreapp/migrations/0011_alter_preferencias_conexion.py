# Generated by Django 4.2.4 on 2023-09-20 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nombreapp', '0010_alter_preferencias_conexion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='preferencias',
            name='conexion',
            field=models.ForeignKey(db_column='nombre', default='cata', on_delete=django.db.models.deletion.CASCADE, to='nombreapp.usuario'),
        ),
    ]
