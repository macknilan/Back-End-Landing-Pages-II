# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.core.urlresolvers import reverse
from django.utils.text import slugify
# from django.utils.html import format_html
from django.utils.crypto import get_random_string
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from sorl.thumbnail import ImageField


class SlugMixin(object):

    def get_slug(self, text, model):
        slug_text = slugify(text)
        # count = 2
        # fecha_ano = datetime.date.year()
        slug = slug_text
        if (model._default_manager.filter(slug=slug).exists()):
            raise ValidationError(_('ESTE MENSAJE ESTA A PRUEBA - ERROR ESTO ESTA REPETIDO'))
        # while(model._default_manager.filter(slug=slug).exists()):
        #     slug = '{0}-{1}'.format(slug_text, count)
        return slug

def change_file_name(self, imagefilename):
    """
    FUNCION PARA CAMBIAR EL NOMBRE DE LA IMAGEN COMPONIENDOLO CON EL SLUG_DIEZ_CARACTERES_RANDOM.EXTENCION
    """
    ext = imagefilename.split('.')[-1]
    imagefilename = "%s_%s.%s" % (self.slug, get_random_string(10), ext)

    return os.path.join('fotos_categoria', imagefilename)


class Categoria(SlugMixin, models.Model):
    CAT_M = (
        ('ninguno', 'Ninguno'),
        ('comedores', 'Comedores'),
        ('cocinas', 'Cocinas'),
        ('closets', 'Closets'),
        ('puertas', 'Puertas'),
        ('banos', 'Banos'),
        )
    cat_mueble = models.CharField("Categoria del mueble", max_length=10, choices=CAT_M, default='ninguno')
    imagen_categoria = ImageField("Foto de Categoria", upload_to=change_file_name, max_length=50)
    slug = models.CharField(max_length=140, blank=True, unique=True)

    def get_absolute_url(self):
        return reverse('categorias:comedores', kwargs={"slug": self.slug})
        # return '/%s/' % self.cat_mueble

    def save(self, *args, **kargs):
        self.slug = self.get_slug(self.cat_mueble, Categoria)
        super(Categoria, self).save(*args, **kargs)

#    def foto_categoria(self):
#        """
#        MOSTRAR IMAGENES DEL ADMINISTRADOR
#        """
#        return format_html('<img src="%s">' % self.imagen_categoria.url)
#    foto_categoria.allow_tags = True

    def __unicode__(self):
        return self.cat_mueble

    def __str__(self):
        return self.cat_mueble


@receiver(pre_delete, sender=Categoria)
def delte_fotos(sender, instance, **kwargs):
    """
    BORRAR LOS ARCHIVOS DE LA CARPETA DESPUES DE ELIMINAAR DE LA BD
    """
    instance.imagen_categoria.delete(False)
