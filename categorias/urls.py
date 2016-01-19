from django.conf.urls import url, include, patterns
from .views import ComedoresListView, CocinasListView, ClosetsListView, \
    PuertasListView, BanosListView, ContactFormView, Pyr

urlpatterns = [

    url(r'^comedores/$', ComedoresListView.as_view(), name='comedores'),
    url(r'^cocinas/$', CocinasListView.as_view(), name='cocinas'),
    url(r'^closets/$', ClosetsListView.as_view(), name='closets'),
    url(r'^puertas/$', PuertasListView.as_view(), name='puertas'),
    url(r'^banos/$', BanosListView.as_view(), name='banos'),
    url(r'^contacto/$', ContactFormView.as_view(), name='contacto'),
    url(r'^preguntas-y-respuestas/$', Pyr.as_view(), name='preguntas-y-respuestas'),
]
