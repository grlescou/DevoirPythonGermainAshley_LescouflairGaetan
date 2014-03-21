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
    url(r'^ProfPage/', 'Prof.views.prof', name='prof'),
     url(r'^modif/', 'Prof.views.modif', name='modif'),
      url(r'^prof_modification_Cours_getInfo/', 'Prof.views.prof_modification_Cours_getInfo', name='prof_modification_Cours_getInfo'),
    #url(r'^institution/', 'gestionCours.views.form', name='form'),


    ##
    ## login part
    url(r'^prof_login/', 'Prof.views.loginPage', name='loginPage'),
     url(r'^prof_login_validation/', 'Prof.views.login', name='login'),
      url(r'^prof_logout/', 'Prof.views.logout', name='logout'),
       url(r'^prof_listing_Cours/', 'Prof.views.prof_listing_Cours', name='prof_listing_Cours'),
       url(r'^prof_Show_CV_Cours/', 'Prof.views.prof_Show_CV_Cours', name='prof_Show_CV_Cours'),
       url(r'prof_Show_CV_professeur/', 'Prof.views.prof_Show_CV_professeur', name='prof_Show_CV_professeur'),





)
