from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'crepes.views.home', name='home'),
    # url(r'^crepes/', include('crepes.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    #url(r'^cours/','home'),
    # url(r'^institution/','form'),
    # url(r'^enregistrement/','getPageForm'),
    # url(r'^bigup/','getBigUp')
    url(r'^$', 'public.views.home', name='home'),
    url(r'^esih4_Cours_gestion/', 'public.views.esih4_Cours_gestion', name='esih4_Cours_gestion'),
    url(r'^esih4_Cours_SInfo/', 'public.views.esih4_Cours_SInfo', name='esih4_Cours_SInfo'),
    url(r'^list_cours/', 'public.views.list_cours', name='list_cours'),

    url(r'^public_Show_CV_Cours/', 'public.views.public_Show_CV_Cours', name='public_Show_CV_Cours'),
    url(r'^public_Show_CV_professeur/', 'public.views.public_Show_CV_professeur', name='public_Show_CV_professeur'),






)

