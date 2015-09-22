# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from random import shuffle
from muebles.models import Mueble


def lista_link_muebles_relacionados(request):
    """
    LISTA DE MUEBLES RELACIONADOS COMO LINKS EN INFERIOR DE PAGINA
    """
    categoria_mueble_comedor = list(Mueble.objects.filter(categoria__cat_mueble="comedores")[:4])
    shuffle(categoria_mueble_comedor)
    categoria_mueble_cocina = list(Mueble.objects.filter(categoria__cat_mueble="cocinas")[:4])
    shuffle(categoria_mueble_cocina)
    categoria_mueble_chifonier = list(Mueble.objects.filter(categoria__cat_mueble="chifoniers")[:4])
    shuffle(categoria_mueble_chifonier)
    categoria_mueble_cuna = list(Mueble.objects.filter(categoria__cat_mueble="cunas")[:4])
    shuffle(categoria_mueble_cuna)
    return {
        'categoria_mueble_comedor': categoria_mueble_comedor,
        'categoria_mueble_cocina': categoria_mueble_cocina,
        'categoria_mueble_chifonier': categoria_mueble_chifonier,
        'categoria_mueble_cuna': categoria_mueble_cuna,
        }


# def utilities_menu(request):
#     modelo_mueble = Mueble.objects.all()
#     nom_mueble = None
# 
#     for i in modelo_mueble:
#         if request.path == i.get_absolute_url():
#             nom_mueble = i
#             break
# 
#     return {'nom_mueble': nom_mueble, 'modelo_mueble': modelo_mueble}