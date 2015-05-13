from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^$', 'perfis.views.index'),
    url(r'^perfis/(?P<perfil_id>\d+)$', 'perfis.views.exibir')
)