from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['categorias:comedores', 'categorias:cocinas', 'categorias:closets', 'categorias:puertas', 'categorias:banos']

    def location(self, item):
        return reverse(item)
