# Generated by Django 3.1.6 on 2021-05-03 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_auto_20210429_2112'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estado',
            options={'verbose_name': 'Estado', 'verbose_name_plural': 'Estados'},
        ),
        migrations.AlterModelOptions(
            name='municipio',
            options={'verbose_name': 'Municipio', 'verbose_name_plural': 'Municipios'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuario', 'verbose_name_plural': 'Usuarios'},
        ),
    ]
