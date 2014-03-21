from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^gestionCours/',include('gestionCours.urls',namespace='gestionCours')),
    #url(r'^$', 'gestionCours.views.home', name='home'),# home page
    # url(r'^gestionCours/',include('gestionCours.urls',namespace='gestionCours')),
    (r'^Prof/',include('Prof.urls',namespace='Prof')),
    (r'^$',include('public.urls',namespace='public')),



)
