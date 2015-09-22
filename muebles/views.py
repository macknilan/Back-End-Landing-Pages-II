# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from categorias.models import Categoria
from .models import Mueble

def page_404(request):
    """
    FUNCION PARA PERSONALIZAR LA PAGINA DE ERROR 404 _FALTA SOLUCIONAR_
    """
    return render(request, '404.html')


def page_500(request):
    """
    FUNCION PARA PERSONALIZAR LA PAGINA DE ERROR 500 _FALTA SOLUCIONAR_
    """
    return render(request, '500.html')


class HomeView(TemplateView):
    """
    CLASE PARA MOSTRAR LAS FOTOGRAFIAS EN LA PAGINA INCIAL
    """
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['pictures_fpss'] = Categoria.objects.all()
        return context
#        import ipdb; ipdb.set_trace() # ESTO ES PARA DEBUGEAR


class ComedoresTemplateDetailView(DetailView):
    """
    CLASE PARA MOSTRAR LOS COMEDORES EN FORMA DE DETALLE/INDIVIDUAL
    """
    model = Mueble
    template_name = "MuebleTemplateDetailView.html"

    def get_queryset(self):
        if self.kwargs.get('slug'):
            queryset = self.model.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_content_data(self, **kwargs):
        context = super(ComedoresTemplateDetailView, self).get_context_data(**kwargs)
        context['categoria'] = 'comedores'
        return context


class CocinasTemplateDetailView(DetailView):
    """
    CLASE PARA MOSTRAR LOS COCINAS EN FORMA DE DETALLE/INDIVIDUAL
    """
    model = Mueble
    template_name = "MuebleTemplateDetailView.html"

    def get_queryset(self):
        if self.kwargs.get('slug'):
            queryset = self.model.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_content_data(self, **kwargs):
        context = super(CocinasTemplateDetailView, self).get_context_data(**kwargs)
        context['categoria'] = 'cocinas'
        return context


class ChifoniersTemplateDetailView(DetailView):
    """
    CLASE PARA MOSTRAR LOS CHIFONIERS EN FORMA DE DETALLE/INDIVIDUAL
    """
    model = Mueble
    template_name = "MuebleTemplateDetailView.html"

    def get_queryset(self):
        if self.kwargs.get('slug'):
            queryset = self.model.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_content_data(self, **kwargs):
        context = super(ChifoniersTemplateDetailView, self).get_context_data(**kwargs)
        context['categoria'] = 'chifoniers'
        return context


class CunasTemplateDetailView(DetailView):
    """
    CLASE PARA MOSTRAR LOS CUNAS EN FORMA DE DETALLE/INDIVIDUAL
    """
    model = Mueble
    template_name = "MuebleTemplateDetailView.html"

    def get_queryset(self):
        if self.kwargs.get('slug'):
            queryset = self.model.objects.filter(slug=self.kwargs['slug'])
        return queryset

    def get_content_data(self, **kwargs):
        context = super(CunasTemplateDetailView, self).get_context_data(**kwargs)
        context['categoria'] = 'cunas'
        return context
