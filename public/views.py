from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import  redirect, render
from DjApp.models import Etablissement, NomCours, Programme, Professeur, cv , Cours , AdminCours, User, UserForm
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def home(request):
    html = get_template('esih4.html')
    return HttpResponse(html.render(Context()))



def esih4_Cours_gestion (request):
    html = get_template('esih4_gestion.html')
    return HttpResponse(html.render(Context()))



def esih4_Cours_SInfo (request):
    html = get_template('esih4_SI.html')
    return HttpResponse(html.render(Context()))


def list_cours (request):
    try:
        dom = request.GET['m']
        sem = request.GET['s']
        niv = request.GET['niv']
        if dom.__eq__("EG"):
            dom = "E&G"
        item_list = Cours.objects.filter(IDprogramme__Mention=dom ,IDcours__Semestre=sem,IDcours__Grade=niv)
        ##=============================================

        paginator = Paginator(item_list, 6) # Show 25 contacts per page

        page = request.GET.get('page')
        try:
            cours_l = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            cours_l = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            cours_l = paginator.page(paginator.num_pages)




        ##--------------------------------------------------

        t = get_template('pubListing_Cours.html')


        html = t.render(Context({'item_list': cours_l}))
        #html = t.render(Context())
        return HttpResponse(html)

    except Exception as e :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)



def public_Show_CV_Cours (request):
    try:

        ids= request.GET['id']
        t = get_template('cours.html')
        #item_list = Cours.objects.all()
        et = Cours.objects.get(id=ids)


        html = t.render(Context({'item': et}))
        #html = t.render(Context())
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


def public_Show_CV_professeur (request):
    try:

        ids= request.GET['id']
        t = get_template('cv.html')
        item_list = Professeur.objects.all()
        et = Professeur.objects.get(id=ids)


        html = t.render(Context({'prof': et}))
        #html = t.render(Context())
        return HttpResponse(html)
    except  Exception as e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)


