# Generated by Django 4.2.4 on 2023-10-10 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('nombreapp', '0010_preferencias_conexion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='preferencias',
            options={'ordering': ['conexion'], 'verbose_name': 'Preferencia', 'verbose_name_plural': 'Preferencias'},
        ),
        migrations.AlterField(
            model_name='preferencias',
            name='conexion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterModelTable(
            name='preferencias',
            table='Preferencia',
        ),
    ]
