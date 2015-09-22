from django.conf.urls import url
from .views import HomeView, ComedoresTemplateDetailView, CocinasTemplateDetailView, ChifoniersTemplateDetailView, CunasTemplateDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^comedores/(?P<slug>[\w\-]+)/$', ComedoresTemplateDetailView.as_view(), name='detailcomedores'),
    url(r'^cocinas/(?P<slug>[\w\-]+)/$', CocinasTemplateDetailView.as_view(), name='detailcocinas'),
    url(r'^chifoniers/(?P<slug>[\w\-]+)/$', ChifoniersTemplateDetailView.as_view(), name='detailchifoniers'),
    url(r'^cunas/(?P<slug>[\w\-]+)/$', CunasTemplateDetailView.as_view(), name='detailcunas'),
]
