# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
# from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from sorl.thumbnail import ImageField
from categorias.models import Categoria


class SlugMixin(object):
    def get_slug(self, text, model):
        slug_text = slugify(text)
        # count = 2
        # fecha_ano = datetime.date.year()

        slug = slug_text
        # while(model._default_manager.filter(slug=slug).exists()):
        #    slug = '{0}-{1}'.format(slug_text, count)
        return slug


def change_file_name(self, imagefilename):
    """
    FUNCION PARA CAMBIAR EL NOMBRE DE LA IMAGEN COMPONIENDOLO CON EL SLUG_DIEZ_CARACTERES_RANDOM.EXTENCION
    """
    ext = imagefilename.split('.')[-1]
    imagefilename = "%s_%s.%s" % (self.slug, get_random_string(10), ext)

    return os.path.join('fotos', imagefilename)


class Mueble(SlugMixin, models.Model):
    # descripcion = models.TextField("Descripcion del mueble", max_length=240)
    descripcion = RichTextField()
    # dimensiones = models.TextField("Dimenciones del mueble", max_length=240)
    dimensiones = RichTextField()
    foto_1 = ImageField("Fotos del mueble 1", upload_to=change_file_name, max_length=50, default='static/IMAGEN_POR_DEFAULT_1200_1000.png')  # blank=False POR DEFAULT
    foto_2 = ImageField("Fotos del mueble 2", upload_to=change_file_name, max_length=50, default='static/IMAGEN_POR_DEFAULT_1200_1000.png')
    foto_3 = ImageField("Fotos del mueble 3", upload_to=change_file_name, max_length=50, default='static/IMAGEN_POR_DEFAULT_1200_1000.png')
    foto_4 = ImageField("Fotos del mueble 4", upload_to=change_file_name, max_length=50, default='static/IMAGEN_POR_DEFAULT_1200_1000.png')
    foto_5 = ImageField("Fotos del mueble 5", upload_to=change_file_name, max_length=50, default='static/IMAGEN_POR_DEFAULT_1200_1000.png')
    modelo = models.CharField("Modelo (Nombre) ", max_length=40)
    oferta = models.SmallIntegerField("¿Oferta?", default=0)
    """
    CERO = NO TIENE OFERTA, DIFERENTE DE CERO SI TIENE OFERTA
    """
    precio = models.DecimalField("Precio del mueble", max_digits=10, decimal_places=2)
    slug = models.CharField(max_length=140, unique=True, blank=True)
    categoria = models.ForeignKey(Categoria)

    def get_absolute_url(self):
        return '/%s/%s/' % (self.categoria, self.slug)
        # return reverse('detailcocinas', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = self.get_slug(self.modelo, Mueble)
        super(Mueble, self).save(*args, **kwargs)

    def __unicode__(self):
        return "%s - %s" % (self.modelo, self.descripcion)

    def __str__(self):
        return "%s - %s" % (self.modelo, self.descripcion)

@receiver(pre_delete, sender=Mueble)
def delte_fotos(sender, instance, **kwargs):
    """
    BORRAR LOS ARCHIVOS DE LA CARPETA DESPUES DE ELIMINAAR DE LA BD
    """
    instance.foto_1.delete(False)
    instance.foto_2.delete(False)
    instance.foto_3.delete(False)
    instance.foto_4.delete(False)
    instance.foto_5.delete(False)


