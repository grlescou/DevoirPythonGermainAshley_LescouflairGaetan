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
    url(r'^cours/', 'gestionCours.views.home', name='home'),
    #url(r'^institution/', 'gestionCours.views.form', name='form'),
    url(r'^enregistrement/', 'gestionCours.views.getPageForm', name='getPageForm'),
    url(r'^bigup/', 'gestionCours.views.getBigUp', name='getBigUp'),
    url(r'^donnee/', 'gestionCours.views.donnee', name='donnee'),
    url(r'^donnee_info/', 'gestionCours.views.donnee1', name='donnee1'),
    url(r'^donnee_supp/', 'gestionCours.views.Esupp', name='Esupp'),
    url(r'^donnee_suppload/', 'gestionCours.views.Esuppload' ,name='Esuppload'),
    url(r'^donnee_Esuppnow/', 'gestionCours.views.Esuppnow', name='Esuppnow'),
    url(r'^Adming/', 'gestionCours.views.Adming', name='Adming'),

    ##
    ##Url Pour la partie  etablissement

    url(r'^listing_etablissement/', 'gestionCours.views.admin_listing_etablissement', name='admin_listing_etablissement'),
    url(r'^enregistrement_etablissement/', 'gestionCours.views.admin_enregistrer_etablissement', name='admin_enregistrer_etablissement'),
    url(r'^enregistrement_etablissement_form/', 'gestionCours.views.admin_enregistrer_etablissement_form', name='admin_enregistrer_etablissement_form'),
    url(r'^modification_etablissement/', 'gestionCours.views.admin_modification_etablissement', name='admin_modification_etablissement'),
    url(r'^modification_etablissement_getInfo/', 'gestionCours.views.admin_modification_getInfo', name='admin_modification_getInfo'),
    url(r'^modification_etablissement_Update/', 'gestionCours.views.admin_modification_Update', name='admin_modification_Update'),
    url(r'^supression_etablissement/', 'gestionCours.views.admin_supression_etablissement', name='admin_supression_etablissement'),
    url(r'^supression_etablissement_getInfo/', 'gestionCours.views.admin_supression_getInfo', name='admin_supression_getInfo'),
    url(r'^supression_etablissement_Update/', 'gestionCours.views.admin_supression_Update', name='admin_supression_Update'),

    ##
    ## Url Pour la partie  NomCours

     url(r'^listing_NomCours/', 'gestionCours.views.admin_listing_NomCours', name='admin_listing_NomCours'),
    url(r'^enregistrement_NomCours/', 'gestionCours.views.admin_enregistrer_NomCours', name='admin_enregistrer_NomCours'),
    url(r'^enregistrement_NomCours_form/', 'gestionCours.views.admin_enregistrer_NomCours_form', name='admin_enregistrer_NomCours_form'),
    url(r'^modification_NomCours/', 'gestionCours.views.admin_modification_NomCours', name='admin_modification_NomCours'),
    url(r'^modification_NomCours_getInfo/', 'gestionCours.views.admin_modification_NomCours_getInfo', name='admin_modification_NomCours_getInfo'),
    url(r'^modification_NomCours_Update/', 'gestionCours.views.admin_modification_NomCours_Update', name='admin_modification_NomCours_Update'),
    url(r'^supression_NomCours/', 'gestionCours.views.admin_supression_NomCours', name='admin_supression_NomCours'),
    url(r'^supression_NomCours_getInfo/', 'gestionCours.views.admin_supression_NomCours_getInfo', name='admin_supression_NomCours_getInfo'),
    url(r'^supression_NomCours_Update/', 'gestionCours.views.admin_supression_NomCours_Update', name='admin_supression_NomCours_Update'),


    ##
    ## Url Pour la partie  Programme

     url(r'^listing_Programme/', 'gestionCours.views.admin_listing_Programme', name='admin_listing_Programme'),
    url(r'^enregistrement_Programme/', 'gestionCours.views.admin_enregistrer_Programme', name='admin_enregistrer_Programme'),
    url(r'^enregistrement_Programme_form/', 'gestionCours.views.admin_enregistrer_Programme_form', name='admin_enregistrer_Programme_form'),
    url(r'^modification_Programme/', 'gestionCours.views.admin_modification_Programme', name='admin_modification_Programme'),
    url(r'^modification_Programme_getInfo/', 'gestionCours.views.admin_modification_Programme_getInfo', name='admin_modification_Programme_getInfo'),
    url(r'^modification_Programme_Update/', 'gestionCours.views.admin_modification_Programme_Update', name='admin_modification_Programme_Update'),
    url(r'^supression_Programme/', 'gestionCours.views.admin_supression_Programme', name='admin_supression_Programme'),
    url(r'^supression_Programme_getInfo/', 'gestionCours.views.admin_supression_Programme_getInfo', name='admin_supression_Programme_getInfo'),
    url(r'^supression_Programme_Update/', 'gestionCours.views.admin_supression_Programme_Update', name='admin_supression_Programme_Update'),


    ##
    ## Url Pour la partie  Professeur

     url(r'^listing_Professeur/', 'gestionCours.views.admin_listing_Professeur', name='admin_listing_Professeur'),
    url(r'^enregistrement_Professeur/', 'gestionCours.views.admin_enregistrer_Professeur', name='admin_enregistrer_Professeur'),
    url(r'^enregistrement_Professeur_form/', 'gestionCours.views.admin_enregistrer_Professeur_form', name='admin_enregistrer_Professeur_form'),
    url(r'^modification_Professeur/', 'gestionCours.views.admin_modification_Professeur', name='admin_modification_Professeur'),
    url(r'^modification_Professeur_getInfo/', 'gestionCours.views.admin_modification_Professeur_getInfo', name='admin_modification_Professeur_getInfo'),
    url(r'^modification_Professeur_Update/', 'gestionCours.views.admin_modification_Professeur_Update', name='admin_modification_Professeur_Update'),
    url(r'^supression_Professeur/', 'gestionCours.views.admin_supression_Professeur', name='admin_supression_Professeur'),
    url(r'^supression_Professeur_getInfo/', 'gestionCours.views.admin_supression_Professeur_getInfo', name='admin_supression_Professeur_getInfo'),
    url(r'^supression_Professeur_Update/', 'gestionCours.views.admin_supression_Professeur_Update', name='admin_supression_Professeur_Update'),
    url(r'^Show_CV_professeur/', 'gestionCours.views.admin_Show_CV_professeur', name='admin_Show_CV_professeur'),

    ##
    ## Url Pour la partie  Cours

     url(r'^listing_Cours/', 'gestionCours.views.admin_listing_Cours', name='admin_listing_Cours'),
    url(r'^enregistrement_Cours/', 'gestionCours.views.admin_enregistrer_Cours', name='admin_enregistrer_Cours'),
    url(r'^enregistrement_Cours_form/', 'gestionCours.views.admin_enregistrer_Cours_form', name='admin_enregistrer_Cours_form'),
    url(r'^modification_Cours/', 'gestionCours.views.admin_modification_Cours', name='admin_modification_Cours'),
    url(r'^modification_Cours_getInfo/', 'gestionCours.views.admin_modification_Cours_getInfo', name='admin_modification_Cours_getInfo'),
    url(r'^modification_Cours_Update/', 'gestionCours.views.admin_modification_Cours_Update', name='admin_modification_Cours_Update'),
    url(r'^supression_Cours/', 'gestionCours.views.admin_supression_Cours', name='admin_supression_Cours'),
    url(r'^supression_Cours_getInfo/', 'gestionCours.views.admin_supression_Cours_getInfo', name='admin_supression_Cours_getInfo'),
    url(r'^supression_Cours_Update/', 'gestionCours.views.admin_supression_Cours_Update', name='admin_supression_Cours_Update'),
    url(r'^Show_CV_Cours/', 'gestionCours.views.admin_Show_CV_Cours', name='admin_Show_CV_Cours'),



)
