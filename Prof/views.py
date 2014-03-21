from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import  redirect, render
from DjApp.models import Etablissement, NomCours, Programme, Professeur, cv , Cours , AdminCours, AdminProfesseur , User
from django.template import RequestContext
from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger





def loginPage (request):
    try:
        if 'User' in request.session :
            if  request.session['Status'].__eq__("professeur"):
                return redirect("Prof/")

        html = get_template('loginprof.html')
        return HttpResponse(html.render(Context()))
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page'}))
        return HttpResponse(html)



def login (request):
    try:

        if 'User' in request.POST :
            user = request.POST['User']
            password = request.POST['Password']

            found =  User.objects.filter(User=user).exists()

            if  found :
                user1 = User.objects.get(User=user)
                if user1.Password.__eq__(password) :
                    request.session['User'] = user1.User
                    request.session['Status'] = user1.Status
                    request.session['ids'] =  user1.ids
                    return render(request, 'Proftemplate/Accueil.html')
                    #return redirect("/Prof/Adming/")
                else:
                    success = "User or password doesn't match"
                    html = get_template('loginprof.html')
                    return HttpResponse(html.render(Context({'success':success})))
            else:
                success = "User or password doesn't match"
                html = get_template('loginprof.html')
                return HttpResponse(html.render(Context({'success':success})))
        else :
            success = "All fields required"
            html = get_template('loginprof.html')
            return HttpResponse(html.render(Context({'success':success})))

    except Exception as e :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


def logout (request) :
    try:
        del request.session['User']
        del request.session['Status']
        del request.session['ids']
        return redirect("/")
    except Exception as e :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)









def prof (request):
    if 'User' not in request.session :
        return redirect("/Prof/prof_login/")
    else:
        if not request.session['Status'].__eq__("professeur"):
             return redirect("/Prof/prof_login/")

    t = get_template('Proftemplate/Accueil.html')
    html = t.render(Context())
    return HttpResponse(html)



def prof_listing_Cours (request):
    try:
        if 'User' not in request.session :
            return redirect("/Prof/prof_login/")
        else:
            if not request.session['Status'].__eq__("professeur"):
                return redirect("/Prof/prof_login/")

        item_list = Cours.objects.filter(IDprofesseur=request.session['ids'])
        ##=============================================

        paginator = Paginator(item_list, 4) # Show 25 contacts per page

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

        t = get_template('Proftemplate/Listing_Cours.html')


        html = t.render(Context({'item_list': cours_l}))
        #html = t.render(Context())
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)



def prof_Show_CV_Cours (request):
    try:
        if 'User' not in request.session :
            return redirect("/Prof/prof_login/")
        else:
            if not request.session['Status'].__eq__("professeur"):
                return redirect("/Prof/prof_login/")

        ids= request.GET['id']
        t = get_template('Proftemplate/cours.html')
        #item_list = Cours.objects.all()
        et = Cours.objects.get(id=ids)


        html = t.render(Context({'item': et}))
        #html = t.render(Context())
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


def prof_Show_CV_professeur (request):
    try:
        if 'User' not in request.session :
            return redirect("/Prof/prof_login/")
        else:
            if not request.session['Status'].__eq__("professeur"):
                return redirect("/Prof/prof_login/")

        #ids= request.GET['id']
        t = get_template('Proftemplate/cv.html')
        item_list = Professeur.objects.all()
        et = Professeur.objects.get(id=request.session['ids'])


        html = t.render(Context({'prof': et}))
        #html = t.render(Context())
        return HttpResponse(html)
    except  Exception as e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)




def modif (request):
    try:
        if 'User' not in request.session :
            return redirect("/Prof/prof_login/")
        else:
            if not request.session['Status'].__eq__("professeur"):
                return redirect("/Prof/prof_login/")

        #ids = request.GET['ids']
        ids= 2
        item_list = Cours.objects.all()
        et = Cours.objects.get(id=ids)
        adminCours = AdminProfesseur(instance=et)
        return render_to_response('Proftemplate/modification_Cours.html', {'Et2': et, 'item_list': item_list,'adminCours': adminCours}, context_instance=RequestContext(request))
        #return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list,'succes':'new page load'} ,context_instance=RequestContext(request))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)






def modif (request):
    try:
        if 'User' not in request.session :
            return redirect("/Prof/prof_login/")
        else:
            if not request.session['Status'].__eq__("professeur"):
                return redirect("/Prof/prof_login/")


            if request.method == 'POST': # If the form has been submitted...
                 if not request.POST.has_key('annuler'):
                    id = request.POST['id']
                    et = Cours.objects.get(id=id)
                    adminCours = AdminProfesseur(request.POST,instance=et) # A form bound to the POST data
                    if adminCours.is_valid(): # All validation rules pass


                        adminCours.save()
                        adminCours = AdminProfesseur()
                        item_list = Cours.objects.all()
                        return render_to_response('Proftemplate/modification_Cours.html', {'item_list': item_list,'AdminProfesseur': adminCours}, context_instance=RequestContext(request)) # Redirect after POST
                    item_list = Cours.objects.all()
                    return render_to_response('Proftemplate/modification_Cours.html', {'item_list': item_list} ,context_instance=RequestContext(request))

                 else:
                     item_list = Cours.objects.filter(IDprofesseur=request.session['ids'])
                     return render_to_response('Proftemplate/modification_Cours.html', {'item_list': item_list} ,context_instance=RequestContext(request))
            else:
                item_list =Cours.objects.filter(IDprofesseur=request.session['ids'])
                return render_to_response('Proftemplate/modification_Cours.html', {'item_list': item_list} ,context_instance=RequestContext(request))

    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)


def prof_modification_Cours_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/Prof/prof_login/")
        else:
            if not request.session['Status'].__eq__("professeur"):
                return redirect("/Prof/prof_login/")

        ids = request.GET['id']
        item_list = Cours.objects.filter(IDprofesseur=request.session['ids'])
        et = Cours.objects.get(id=ids)
        adminCours = AdminProfesseur(instance=et)
        return render_to_response('Proftemplate/modification_Cours.html', {'Et2': et, 'item_list': item_list,'AdminProfesseur': adminCours}, context_instance=RequestContext(request))
        #return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list,'succes':'new page load'} ,context_instance=RequestContext(request))
        return HttpResponse(html)
    except Exception as e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>> '+e.__str__()}))
        return HttpResponse(html)