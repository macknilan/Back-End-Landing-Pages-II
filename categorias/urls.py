from django.conf.urls import url, include, patterns
from .views import ComedoresListView, CocinasListView, ChifoniersListView, CunasListView, ContactFormView, Pyr

urlpatterns = [

    url(r'^comedores/$', ComedoresListView.as_view(), name='comedores'),
    url(r'^cocinas/$', CocinasListView.as_view(), name='cocinas'),
    url(r'^chifoniers/$', ChifoniersListView.as_view(), name='chifoniers'),
    url(r'^cunas/$', CunasListView.as_view(), name='cunas'),
    url(r'^contacto/$', ContactFormView.as_view(), name='contacto'),
    url(r'^preguntas-y-respuestas/$', Pyr.as_view(), name='preguntas-y-respuestas'),
]
