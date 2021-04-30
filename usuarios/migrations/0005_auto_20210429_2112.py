# Generated by Django 3.1.6 on 2021-04-29 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_auto_20210429_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.estado', verbose_name='Estado'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='municipio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.municipio', verbose_name='Municipio'),
        ),
    ]
