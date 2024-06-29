# Generated by Django 5.0.6 on 2024-06-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('front', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='raca',
            name='logica',
        ),
        migrations.AddField(
            model_name='raca',
            name='logica_de_criacao',
            field=models.JSONField(default=dict),
        ),
        migrations.AddField(
            model_name='raca',
            name='versao',
            field=models.CharField(default='1.0', max_length=10),
        ),
        migrations.AlterField(
            model_name='raca',
            name='atributos',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='raca',
            name='habilidades',
            field=models.CharField(max_length=255),
        ),
    ]
