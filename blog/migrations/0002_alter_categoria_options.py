# Generated by Django 4.2.4 on 2023-08-27 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'permissions': [('crear_categoria', 'Puede crear categoria'), ('editar_categoria', 'Puede editar categoria')], 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
    ]
