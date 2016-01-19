# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 21:41
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import muebles.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categorias', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', ckeditor.fields.RichTextField()),
                ('dimensiones', ckeditor.fields.RichTextField()),
                ('foto_1', sorl.thumbnail.fields.ImageField(default='static/IMAGEN_POR_DEFAULT_1200_1000.png', max_length=50, upload_to=muebles.models.change_file_name, verbose_name='Fotos del mueble 1')),
                ('foto_2', sorl.thumbnail.fields.ImageField(default='static/IMAGEN_POR_DEFAULT_1200_1000.png', max_length=50, upload_to=muebles.models.change_file_name, verbose_name='Fotos del mueble 2')),
                ('foto_3', sorl.thumbnail.fields.ImageField(default='static/IMAGEN_POR_DEFAULT_1200_1000.png', max_length=50, upload_to=muebles.models.change_file_name, verbose_name='Fotos del mueble 3')),
                ('foto_4', sorl.thumbnail.fields.ImageField(default='static/IMAGEN_POR_DEFAULT_1200_1000.png', max_length=50, upload_to=muebles.models.change_file_name, verbose_name='Fotos del mueble 4')),
                ('foto_5', sorl.thumbnail.fields.ImageField(default='static/IMAGEN_POR_DEFAULT_1200_1000.png', max_length=50, upload_to=muebles.models.change_file_name, verbose_name='Fotos del mueble 5')),
                ('modelo', models.CharField(max_length=40, verbose_name='Modelo (Nombre) ')),
                ('oferta', models.SmallIntegerField(default=0, verbose_name='\xbfOferta?')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio del mueble')),
                ('slug', models.CharField(blank=True, max_length=140, unique=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categorias.Categoria')),
            ],
            bases=(muebles.models.SlugMixin, models.Model),
        ),
    ]
