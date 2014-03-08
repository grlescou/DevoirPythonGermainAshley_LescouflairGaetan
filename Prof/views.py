from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context

from DjApp.models import Etablissement, NomCours, Programme, Professeur, cv , Cours , AdminCours, AdminProfesseur
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse



def prof (request):
    t = get_template('Proftemplate/Accueil.html')
    html = t.render(Context())
    return HttpResponse(html)


def modif (request):
    try:
        ids = request.GET['ids']
        item_list = Cours.objects.all()
        et = Cours.objects.get(id=ids)
        adminCours = AdminProfesseur(instance=et)
        return render_to_response('Proftemplate\modification_Cours.html', {'Et2': et, 'item_list': item_list,'adminCours': adminCours}, context_instance=RequestContext(request))
        #return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list,'succes':'new page load'} ,context_instance=RequestContext(request))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)
