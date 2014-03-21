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


