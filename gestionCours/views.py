from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import  redirect, render
from DjApp.models import Etablissement, NomCours, Programme, Professeur, cv , Cours , AdminCours, User, UserForm
from django.template import RequestContext
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template import Library

register = Library()



# def my_view(request):
#     c = {}
#     c.update(csrf(request))
#     # ... view code here
#     return render_to_response("a_template.html", c)


from django.shortcuts import render
from myApp.chartReport import volumeHoraire

from myApp.Stat import Stat


def loginPage (request):
    try:

        found =  User.objects.filter(User="admin").exists()
        if not found :
            User(User="admin",Password="password",Status = "administration", ids="admin").save()

        if 'User' in request.session :
            if  request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/Adming/")

        html = get_template('loginadm.html')
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
                    #return render(request, 'adminG.html')
                    return redirect("/gestionCours/Adming/")
                else:
                    success = "User or password doesn't match"
                    html = get_template('loginadm.html')
                    return HttpResponse(html.render(Context({'success':success})))
            else:
                success = "User or password doesn't match"
                html = get_template('loginadm.html')
                return HttpResponse(html.render(Context({'success':success})))
        else :
            success = "All fields required"
            html = get_template('loginadm.html')
            return HttpResponse(html.render(Context({'success':success})))

    except Exception as e :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


def logout (request) :
    try:
        del request.session['User']
        del request.session['Status']
        return redirect("/")
    except Exception as e :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)




def form(request):
    nom = request.GET['nom']
    lieu = request.GET['lieu']
    t = get_template('form.html')
    Etablissement(Nom=nom, Lieu=lieu).save()
    html = t.render(Context({'reponse':'donnee enregistree'}))
    return HttpResponse(html)


def getPageForm (request):

    html = get_template('form.html')
    return HttpResponse(html.render(Context()))


def getBigUp (request):
    html = get_template('bigup.html')
    return HttpResponse(html.render(Context()))


def donnee (request):
    t = get_template('donnee.html')
    html = t.render(Context())
    return HttpResponse(html)


def donnee1(request):
    nom = request.GET['nom']
    t = get_template('donnee.html')
    item_list = Etablissement.objects.filter(Nom=nom)
    html = t.render(Context({'item_list': item_list}))
    return HttpResponse(html)


def Esuppload (request):
    t = get_template('supprimer_etablissement.html')
    item_list = Etablissement.objects.all()
    html = t.render(Context({'item_list': item_list}))
    return HttpResponse(html)


def Esupp (request):
    ids = request.GET['ids']
    t = get_template('supprimer_etablissement.html')
    item_list = Etablissement.objects.all()
    et = Etablissement.objects.get(id=ids)
    html = t.render(Context({'item_list': item_list, 'Et': et}))
    return HttpResponse(html)


def Esuppnow (request):
    id = request.GET['id']
    t = get_template('supprimer_etablissement.html')
    E = Etablissement.objects.get(id=id)

    t.render(Context({'succes': "L'etablissement {} a ete supprime ".format(E.Nom)}))
    Etablissement.objects.get(id=id).delete()
    item_list = Etablissement.objects.all()
    html = t.render(Context({'item_list': item_list}))
    return HttpResponse(html)


"""
 Administration page loader

"""

def Adming (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")



            stat = Stat()

        S_ETCS_A= False
        G_ETCS_A = False
        S_Hour_A = False
        G_Hour_A = False

        D_ETCS = False
        D_Hour =False

        if "donnee" in request.GET :

            if request.GET['donnee'].__eq__("S-ETCS-A"):


                volume = volumeHoraire()
                volume.s1_Y_SI_E = stat.getETCS_S1__by_Year_SI()
                volume.s2_Y_SI_E = stat.getETCS_S2__by_Year_SI()
                S_ETCS_A= True


            if request.GET['donnee'].__eq__("G-ETCS-A"):
                volume = volumeHoraire()
                volume.s1_Y_EG_E =stat.getETCS_S1__by_Year_EG()
                volume.s2_Y_EG_E =stat.getETCS_S2__by_Year_EG()
                G_ETCS_A = True


            if request.GET['donnee'].__eq__("S-Hour-A"):


                volume = volumeHoraire()
                volume.s1_Y_SI_H = stat.getHour_S1__by_Year_SI()
                volume.s2_Y_SI_H = stat.getHour_S2__by_Year_SI()
                S_Hour_A = True



            if request.GET['donnee'].__eq__("G-Hour-A"):
                volume = volumeHoraire()
                volume.s1_Y_EG_H =stat.getHour_S1__by_Year_EG()
                volume.s2_Y_EG_H =stat.getHour_S2__by_Year_EG()
                G_Hour_A = True

            if request.GET['donnee'].__eq__("D-ETCS"):

                volume = volumeHoraire()
                (volume.D_SI_E, volume.D_EG_E) = stat.VolumeECTS_Diplome()
                D_ETCS = True




            if request.GET['donnee'].__eq__("D-Hour"):
                volume = volumeHoraire()
                (volume.D_SI_H,volume.D_EG_H) =stat.VolumeHour_Diplome()

                D_Hour  = True




        else:
            volume = volumeHoraire()
            (volume.D_SI_E, volume.D_EG_E) = stat.VolumeECTS_Diplome()
            D_ETCS = True




        t = get_template('adminG.html')
        html = t.render(Context({'hor': volume,"S_ETCS_A":S_ETCS_A,"G_ETCS_A":G_ETCS_A, "S_Hour_A":S_Hour_A, "G_Hour_A": G_Hour_A,"D_ETCS": D_ETCS,"D_Hour": D_Hour}))
        return render(request,'adminG.html',{'hor': volume,"S_ETCS_A":S_ETCS_A,"G_ETCS_A":G_ETCS_A, "S_Hour_A":S_Hour_A, "G_Hour_A": G_Hour_A,"D_ETCS": D_ETCS,"D_Hour": D_Hour})
        #return HttpResponse(html)
    except Exception as e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>>'+e.__str__()}))
        return HttpResponse(html)



"""
Partie Etablissemnet

"""

"""
 Listing   Etablissemet

"""


def admin_listing_etablissement (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
        
        t = get_template('Admintemplate/Listing_etablissement.html')
        item_list = Etablissement.objects.all()

         ##=============================================

        paginator = Paginator(item_list, 5) # Show 25 contacts per page

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

        html = t.render(Context({'item_list':  cours_l}))
        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page'}))
        return HttpResponse(html)




"""
 Enregistrer  Etablissemet

"""

def admin_enregistrer_etablissement (request):
    if 'User' not in request.session :
        return redirect("/gestionCours/admin_login/")
    else:
        if not request.session['Status'].__eq__("administration"):
             return redirect("/gestionCours/admin_login/")
        
    t = get_template('Admintemplate/enregistrement_etablissement.html')
    #item_list = Etablissement.objects.all()
    html = t.render(Context())
    #html = t.render(Context())
    return HttpResponse(html)


def admin_enregistrer_etablissement_form (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        nom = request.GET['nom']
        lieu = request.GET['lieu']
        t = get_template('Admintemplate/enregistrement_etablissement.html')
        isIn =  Etablissement.objects.filter(Nom=nom, Lieu=lieu).exists()

        if isIn:
             html = t.render(Context({'reponse':'Donnee existe deja'}))
        else :
            Etablissement(Nom=nom, Lieu=lieu).save()
            html = t.render(Context({'reponse':'Donnee enregistree'}))

        return HttpResponse(html)

    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page'}))
        return HttpResponse(html)



"""
 modification  Etablissemet

"""


def admin_modification_etablissement (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_etablissement.html')
        item_list = Etablissement.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
            t = get_template('404Error.html')
            html = t.render(Context({'info': 'Erreur dans la page ou base nbase'}))
            return HttpResponse(html)



def admin_modification_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/modification_etablissement.html')
        item_list = Etablissement.objects.all()
        et = Etablissement.objects.get(id=ids)
        html = t.render(Context({'item_list': item_list, 'Et2': et}))
        return HttpResponse(html)
    except:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_modification_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_etablissement.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            nom = request.GET['nom']
            lieu = request.GET['lieu']
            et = Etablissement.objects.get(id=id)
            t.render(Context({'succes': "id: {} L'etablissement {} a ete modifier ".format(et.Nom, et.id)}))
            et.Nom = nom
            et.Lieu = lieu
            et.save()
            item_list = Etablissement.objects.all()
            html = t.render(Context({'item_list': item_list}))
        else:
            item_list = Etablissement.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except :
            t = get_template('404Error.html')
            html = t.render(Context({'info': 'Erreur dans la page'}))
            return HttpResponse(html)




"""
 supression  Etablissemet

"""

def admin_supression_etablissement (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_etablissement.html')
        item_list = Etablissement.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)

    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_supression_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/supression_etablissement.html')
        item_list = Etablissement.objects.all()
        et = Etablissement.objects.get(id=ids)
        html = t.render(Context({'item_list': item_list, 'Et': et}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_etablissement.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            et = Etablissement.objects.get(id=id)
            #t.render(Context({'succes': "id: {} L'etablissement {} a ete modifier ".format(et.Nom, et.id)}))

            t.render(Context({'succes': "L'etablissement {} a ete supprime ".format(et.Nom)}))
            Etablissement.objects.get(id=id).delete()
            item_list = Etablissement.objects.all()
            html = t.render(Context({'item_list':item_list}) )
        else:
            item_list = Etablissement.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)








"""
Partie NomCours

"""

"""
 Listing   NomCours

"""


def admin_listing_NomCours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/Listing_NomCours.html')
        item_listNcours = NomCours.objects.all()


         ##=============================================

        paginator = Paginator(item_listNcours, 5) # Show 25 contacts per page

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


        #t.render(Context({'item_listNcours': item_listNcours}))
        item_listEt = Etablissement.objects.all()
        html = t.render(Context({'item_listEt': item_listEt, 'item_listNcours': cours_l}))
        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)



"""
 Enregistrer  NomCours

"""

def admin_enregistrer_NomCours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/enregistrement_NomCours.html')
        item_list = Etablissement.objects.all()
        html = t.render(Context({'item_list': item_list}))

        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_enregistrer_NomCours_form (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        nom = request.GET['nom']
        grade = request.GET['Grade']
        semestre = request.GET['Semestre']
        idEtablissement = request.GET['Etablissement']
        et = Etablissement.objects.get(id=idEtablissement)
        t = get_template('Admintemplate/enregistrement_NomCours.html')
        NomCours(Nom=nom, Grade=grade, Semestre=semestre, CodeEtablissement=et).save()
        t.render(Context({'reponse':'Donnee enregistree'}))
        item_list = Etablissement.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)



"""
 modification NomCours

"""


def admin_modification_NomCours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_NomCours.html')
        item_list = NomCours.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_modification_NomCours_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/modification_NomCours.html')
        item_list = NomCours.objects.all()
        item_listEt = Etablissement.objects.all()
        et = NomCours.objects.get(id=ids)
        html = t.render(Context({'item_listEt': item_listEt, 'Et2': et, 'item_list': item_list }))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_modification_NomCours_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_NomCours.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            nom = request.GET['nom']
            grade = request.GET['Grade']
            semestre = request.GET['Semestre']
            idEtablissement = request.GET['Etablissement'] #Etablissement=2&Grade=L2&Semestre=S1&nom=SSI+2&id=6
            item_list = NomCours.objects.all()
            et = Etablissement.objects.get(id=idEtablissement)
            nc = NomCours.objects.get(id=id)
            isIn = NomCours.objects.filter(Nom=nom, Grade=grade, Semestre=semestre, CodeEtablissement=et).exists()

            if isIn:
                html= t.render(Context({'succes':'Donnee existe deja', 'item_list': item_list}))

            else :
                t.render(Context({'succes': "id: {} L'NomCours {} a ete modifier ".format(nc.id, nc.Nom)}))
                nc.Nom= nom
                nc.Grade= grade
                nc.Semestre= semestre
                nc.CodeEtablissement= et
                nc.save()
                item_list = NomCours.objects.all()
                html = t.render(Context({'item_list': item_list, 'succes': "id: {} L'NomCours {} a ete modifier ".format(nc.id, nc.Nom)}))
        else:
            item_list = NomCours.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


"""
 supression  NomCours

"""

def admin_supression_NomCours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_NomCours.html')
        item_list = NomCours.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_NomCours_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/supression_NomCours.html')
        item_list = NomCours.objects.all()
        item_listEt = Etablissement.objects.all()
        et = NomCours.objects.get(id=ids)
        html = t.render(Context({'item_listEt': item_listEt, 'Et2': et, 'item_list': item_list }))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_NomCours_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_NomCours.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            et = NomCours.objects.get(id=id)
            #t.render(Context({'succes': "id: {} L'NomCours {} a ete modifier ".format(et.Nom, et.id)}))
            mess="L'NomCours {} a ete supprime ".format(et.Nom)
            NomCours.objects.get(id=id).delete()
            item_list = NomCours.objects.all()
            html = t.render(Context({'item_list':item_list, 'succes':mess}) )
        else:
            item_list = NomCours.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)





"""
Partie Programme

"""

"""
 Listing   Programme

"""


def admin_listing_Programme (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/Listing_Programme.html')
        item_list = Programme.objects.all()

         ##=============================================

        paginator = Paginator(item_list, 5) # Show 25 contacts per page

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




        html = t.render(Context({'item_list':  cours_l}))
        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)



"""
 Enregistrer  Programme

"""

def admin_enregistrer_Programme (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/enregistrement_Programme.html')
        item_list = Programme.objects.all()
        html = t.render(Context({'item_list': item_list}))

        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_enregistrer_Programme_form (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        Domaine= request.GET['Domaine']
        Mention= request.GET['Mention']
        Specialite= request.GET['Specialite']
        Type= request.GET['Type']
        Langue= request.GET['Langue']

        if Domaine.__eq__("ST"):
            if Mention.__eq__("SI"):
                if Specialite.__eq__("TEL") or Specialite.__eq__("BDD") or Specialite.__eq__("ONE") or Specialite.__eq__("NOSP"):

                    if not (Langue.__eq__("Creole") or  Langue.__eq__("Francais") or   Langue.__eq__("Anglais") ):
                        t = get_template('Admintemplate/enregistrement_Programme.html')
                        html = t.render(Context({'reponse':'Erreur dans la Langue, Langue={Creole,Francais,Anglais}'}))
                        return HttpResponse(html)
                    isIn =  Programme.objects.filter(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).exists()

                    if isIn:
                        t = get_template('Admintemplate/enregistrement_Programme.html')
                        html = t.render(Context({'reponse':'Donnee existe deja'}))
                    else :
                        Programme(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).save()
                        t = get_template('Admintemplate/enregistrement_Programme.html')
                        html = t.render(Context({'reponse':'Donnee enregistree'}))
                    return HttpResponse(html)
                else:
                    Programme(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).save()
                    t = get_template('Admintemplate/enregistrement_Programme.html')
                    html = t.render(Context({'reponse':'Erreur dans la Specialite, Domaine ST, specialite={TEL,BDD,ONE,NOSP}'}))
                    return HttpResponse(html)
            else:
                t = get_template('Admintemplate/enregistrement_Programme.html')
                html = t.render(Context({'reponse':'Erreur dans la Mention, Domaine  S&T Mention={SI}'}))
                return HttpResponse(html)


        if Domaine.__eq__("E&G"):
            if Mention.__eq__("E&G"):
                if Specialite.__eq__("SdE") or Specialite.__eq__("SC") or Specialite.__eq__("NOSP") :

                    if not (Langue.__eq__("Creole") or  Langue.__eq__("Francais") or   Langue.__eq__("Anglais") ):
                        t = get_template('Admintemplate/enregistrement_Programme.html')
                        html = t.render(Context({'reponse':'Erreur dans la Langue, Langue={Creole,Francais,Anglais}'}))
                        return HttpResponse(html)
                    isIn =  Programme.objects.filter(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).exists()

                    if isIn:
                        t = get_template('Admintemplate/enregistrement_Programme.html')
                        html = t.render(Context({'reponse':'Donnee existe deja'}))
                    else :
                        Programme(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).save()
                        t = get_template('Admintemplate/enregistrement_Programme.html')
                        html = t.render(Context({'reponse':'Donnee enregistree'}))
                    return HttpResponse(html)
                else:
                    t = get_template('Admintemplate/enregistrement_Programme.html')
                    html = t.render(Context({'reponse':'Erreur dans la Specialite, Domaine  E&G, Specialite={SdE,SC,NOSP}'}))
                    return HttpResponse(html)
            else:
                t = get_template('Admintemplate/enregistrement_Programme.html')
                html = t.render(Context({'reponse':'Erreur dans la Mention, Domaine  E&G Mention={E&G}'}))
                return HttpResponse(html)


        if not ( Domaine.__eq__("ST") or Domaine.__eq__("E&G") ) :
            t = get_template('Admintemplate/enregistrement_Programme.html')
            html = t.render(Context({'reponse':"Erreur dans le Domaine, Domaine n'existe pas   Domaine={ST,E&G}"}))
            return HttpResponse(html)


    except Exception, e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)



"""
 modification Programme

"""


def admin_modification_Programme (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_Programme.html')
        item_list = Programme.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_modification_Programme_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/modification_Programme.html')
        item_list = Programme.objects.all()
        et = Programme.objects.get(id=ids)
        html = t.render(Context({'Et2': et, 'item_list': item_list }))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_modification_Programme_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_Programme.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            Domaine= request.GET['Domaine']
            Mention= request.GET['Mention']
            Specialite= request.GET['Specialite']
            Type= request.GET['Type']
            Langue= request.GET['Langue']
            nc = Programme.objects.get(id=id)

            if Domaine.__eq__("ST"):
                if Mention.__eq__("SI"):
                    if Specialite.__eq__("TEL") or Specialite.__eq__("BDD") or Specialite.__eq__("ONE") or Specialite.__eq__("NOSP"):

                        if not (Langue.__eq__("Creole") or  Langue.__eq__("Francais") or   Langue.__eq__("Anglais") ):
                            t = get_template('Admintemplate/modification_Programme.html')
                            item_list = Programme.objects.all()
                            html = t.render(Context({'item_list': item_list, 'succes':'Erreur dans la Langue, Langue={Creole,Francais,Anglais}'}))
                            return HttpResponse(html)
                        isIn =  Programme.objects.filter(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).exists()

                        if isIn:
                            t = get_template('Admintemplate/modification_Programme.html')
                            item_list = Programme.objects.all()
                            html = t.render(Context({'item_list': item_list, 'succes':'Donnee existe deja'}))
                        else :
                            nc.Domaine = Domaine
                            nc.Mention = Mention
                            nc.Specialite = Specialite
                            nc.TypeCours = Type
                            nc.Langue = Langue
                            nc.save()
                            item_list = Programme.objects.all()
                            t = get_template('Admintemplate/modification_Programme.html')
                            html = t.render(Context({'item_list': item_list, 'succes': "id: {} L'Programme {}-{}-{}-{}-{} a ete modifier ".format(nc.id,nc.Domaine,nc.Mention,nc.Specialite,nc.TypeCours,nc.Langue)}))
                        return HttpResponse(html)

                    else:
                        Programme(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).save()
                        t = get_template('Admintemplate/modification_Programme.html')
                        item_list = Programme.objects.all()
                        html = t.render(Context({'item_list': item_list, 'succes':'Erreur dans la Specialite, Domaine ST, specialite={TEL,BDD,ONE,NOSP}'}))
                        return HttpResponse(html)
                else:
                    t = get_template('Admintemplate/modification_Programme.html')
                    item_list = Programme.objects.all()
                    html = t.render(Context({'item_list': item_list, 'succes':'Erreur dans la Mention, Domaine  S&T Mention={SI}'}))
                    return HttpResponse(html)


            if Domaine.__eq__("E&G"):
                if Mention.__eq__("E&G"):
                    if Specialite.__eq__("SdE") or Specialite.__eq__("SC") or Specialite.__eq__("NOSP") :

                        if not (Langue.__eq__("Creole") or  Langue.__eq__("Francais") or   Langue.__eq__("Anglais") ):
                            t = get_template('Admintemplate/modification_Programme.html')
                            item_list = Programme.objects.all()
                            html = t.render(Context({'item_list': item_list,'succes':'Erreur dans la Langue, Langue={Creole,Francais,Anglais}'}))
                            return HttpResponse(html)
                        isIn =  Programme.objects.filter(Domaine=Domaine, Mention=Mention, Specialite=Specialite, TypeCours=Type, Langue=Langue).exists()

                        if isIn:
                            t = get_template('Admintemplate/modification_Programme.html')
                            item_list = Programme.objects.all()
                            html = t.render(Context({'item_list': item_list, 'succes':'Donnee existe deja'}))
                        else :
                            nc.Domaine = Domaine
                            nc.Mention = Mention
                            nc.Specialite = Specialite
                            nc.TypeCours = Type
                            nc.Langue = Langue
                            nc.save()
                            item_list = Programme.objects.all()
                            t = get_template('Admintemplate/modification_Programme.html')
                            html = t.render(Context({'item_list': item_list, 'succes': "id: {} L'Programme {}-{}-{}-{}-{} a ete modifier ".format(nc.id,nc.Domaine,nc.Mention,nc.Specialite,nc.TypeCours,nc.Langue)}))
                        return HttpResponse(html)
                    else:
                        t = get_template('Admintemplate/modification_Programme.html')
                        item_list = Programme.objects.all()
                        html = t.render(Context({'item_list': item_list, 'succes':'Erreur dans la Specialite, Domaine  E&G, Specialite={SdE,SC,NOSP}'}))
                        return HttpResponse(html)
                else:
                    t = get_template('Admintemplate/modification_Programme.html')
                    item_list = Programme.objects.all()
                    html = t.render(Context({'item_list': item_list, 'succes':'Erreur dans la Mention, Domaine  E&G Mention={E&G}'}))
                    return HttpResponse(html)


            if not ( Domaine.__eq__("ST") or Domaine.__eq__("E&G") ) :
                t = get_template('Admintemplate/modification_Programme.html')
                item_list = Programme.objects.all()
                html = t.render(Context({'item_list': item_list,'succes':"Erreur dans le Domaine, Domaine n'existe pas   Domaine={ST,E&G}"}))
                return HttpResponse(html)




        else:
            item_list = Programme.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


"""
 supression  Programme

"""

def admin_supression_Programme (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_Programme.html')
        item_list = Programme.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Programme_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/supression_Programme.html')
        item_list = Programme.objects.all()
        et = Programme.objects.get(id=ids)
        html = t.render(Context({'Et2': et, 'item_list': item_list }))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Programme_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_Programme.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            nc = Programme.objects.get(id=id)
            #t.render(Context({'succes': "id: {} L'Programme {} a ete modifier ".format(et.Nom, et.id)}))
            mess="L'Programme {}-{}-{}-{}-{} a ete supprime ".format(nc.Domaine,nc.Mention,nc.Specialite,nc.TypeCours,nc.Langue)
            Programme.objects.get(id=id).delete()
            item_list = Programme.objects.all()
            html = t.render(Context({'item_list':item_list, 'succes':mess}) )
        else:
            item_list = Programme.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)









"""
Partie Professeur

"""

"""
 Listing   Professeur

"""


def admin_listing_Professeur (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/Listing_Professeur.html')
        item_list = Professeur.objects.all()


         ##=============================================

        paginator = Paginator(item_list, 5) # Show 25 contacts per page

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


        html = t.render(Context({'item_list': cours_l }))
        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_Show_CV_professeur (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids= request.GET['id']
        t = get_template('Admintemplate/cv.html')
        item_list = Professeur.objects.all()
        et = Professeur.objects.get(id=ids)


        html = t.render(Context({'prof': et}))
        #html = t.render(Context())
        return HttpResponse(html)
    except  Exception as e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)


"""
 Enregistrer  Professeur

"""

def admin_enregistrer_Professeur (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/enregistrement_Professeur.html')
        item_list = Professeur.objects.all()
        html = t.render(Context({'item_list': item_list}))

        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_enregistrer_Professeur_form (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        nom = request.GET['nom']
        prenom = request.GET['prenom']
        NoId = request.GET['NoId']

        ## CV Part

        ad_prof = request.GET['ad_prof']
        sit_act = request.GET['sit_act']
        etablissement = request.GET['etablissement']
        EmploiActuel = request.GET['EmploiActuel']
        Formation = request.GET['Formation']
        EmploisPrecedents = request.GET['EmploisPrecedents']
        Experiencesdenseignement = request.GET['Experiencesdenseignement']
        ExperienceProfessionnelle = request.GET['ExperienceProfessionnelle']
        ResponsabiliteAdministrative =  request.GET['ResponsabiliteAdministrative']



        isIn =  Professeur.objects.filter(Nom=nom,Prenom=prenom,NoIndentite=NoId).exists()

        if isIn:

            t = get_template('Admintemplate/enregistrement_Professeur.html')
            html = t.render(Context({'reponse':'Donnee existe deja'}))
        else :
            isCVin = cv.objects.filter(ad_prof=ad_prof, sit_act= sit_act, etablissement= etablissement, EmploiActuel= EmploiActuel,Formation=Formation,EmploisPrecedents=EmploisPrecedents,Experiencesdenseignement=Experiencesdenseignement,ExperienceProfessionnelle=ExperienceProfessionnelle,ResponsabiliteAdministrative=ResponsabiliteAdministrative).exists()
            if not isCVin :
                cv(ad_prof=ad_prof, sit_act= sit_act, etablissement= etablissement, EmploiActuel= EmploiActuel,Formation=Formation,EmploisPrecedents=EmploisPrecedents,Experiencesdenseignement=Experiencesdenseignement,ExperienceProfessionnelle=ExperienceProfessionnelle,ResponsabiliteAdministrative=ResponsabiliteAdministrative).save()
                CV = cv.objects.get(ad_prof=ad_prof, sit_act= sit_act, etablissement= etablissement, EmploiActuel= EmploiActuel,Formation=Formation,EmploisPrecedents=EmploisPrecedents,Experiencesdenseignement=Experiencesdenseignement,ExperienceProfessionnelle=ExperienceProfessionnelle,ResponsabiliteAdministrative=ResponsabiliteAdministrative)
                Professeur(Nom=nom,Prenom=prenom,NoIndentite=NoId,CV=CV).save()
                t = get_template('Admintemplate/enregistrement_Professeur.html')
                html = t.render(Context({'reponse':'Donnee Professeur enregistree'}))
            else:
                t = get_template('Admintemplate/enregistrement_Professeur.html')
                html = t.render(Context({'reponse':'Donnee CV existe deja'}))

        return HttpResponse(html)


    except Exception, e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)



"""
 modification Professeur

"""


def admin_modification_Professeur (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_Professeur.html')
        item_list = Professeur.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_modification_Professeur_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/modification_Professeur.html')
        item_list = Professeur.objects.all()
        et = Professeur.objects.get(id=ids)
        html = t.render(Context({'Et2': et, 'item_list': item_list }))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_modification_Professeur_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_Professeur.html')

        if not request.GET.has_key('annuler'):
            id= request.GET['id']
            nom = request.GET['nom']
            prenom = request.GET['prenom']
            NoId = request.GET['NoId']

            ## CV Part

            ad_prof = request.GET['ad_prof']
            sit_act = request.GET['sit_act']
            etablissement = request.GET['etablissement']
            EmploiActuel = request.GET['EmploiActuel']
            Formation = request.GET['Formation']
            EmploisPrecedents = request.GET['EmploisPrecedents']
            Experiencesdenseignement = request.GET['Experiencesdenseignement']
            ExperienceProfessionnelle = request.GET['ExperienceProfessionnelle']
            ResponsabiliteAdministrative =  request.GET['ResponsabiliteAdministrative']

            nc = Professeur.objects.get(id=id)
            isIn = False
            if not (nc.Nom.__eq__(nom) and nc.Prenom.__eq__(prenom) and nc.NoIndentite.__eq__(NoId)):
                isIn =  Professeur.objects.filter(Nom=nom,Prenom=prenom,NoIndentite=NoId).exists()

            if isIn:

                t = get_template('Admintemplate/modification_Professeur.html')
                item_list = Professeur.objects.all()
                html = t.render(Context({'item_list': item_list,'succes':'Donnee existe deja'}))
            else :
                CV = cv.objects.get(id=nc.CV.id)
                CV.ad_prof=ad_prof
                CV.sit_act= sit_act
                CV.etablissement= etablissement
                CV.EmploiActuel= EmploiActuel
                CV.Formation=Formation
                CV.EmploisPrecedents=EmploisPrecedents
                CV.Experiencesdenseignement=Experiencesdenseignement
                CV.ExperienceProfessionnelle=ExperienceProfessionnelle
                CV.ResponsabiliteAdministrative=ResponsabiliteAdministrative
                CV.save()
                nc.Nom=nom
                nc.Prenom=prenom
                nc.NoIndentite = NoId
                nc.save()
                item_list = Professeur.objects.all()
                t = get_template('Admintemplate/modification_Professeur.html')
                html = t.render(Context({'item_list': item_list,'succes':'Donnee Professeur modifier'}))


            return HttpResponse(html)



        else:
            item_list = Professeur.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


"""
 supression  Professeur

"""

def admin_supression_Professeur (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_Professeur.html')
        item_list = Professeur.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Professeur_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/supression_Professeur.html')
        item_list = Professeur.objects.all()
        et = Professeur.objects.get(id=ids)
        html = t.render(Context({'Et2': et, 'item_list': item_list }))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Professeur_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_Professeur.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            nc = Professeur.objects.get(id=id)
            #t.render(Context({'succes': "id: {} L'Professeur {} a ete modifier ".format(et.Nom, et.id)}))
            mess="Professeur {} {} de No Identite -{} a ete supprime ".format(nc.Prenom,nc.Prenom,nc.NoIndentite)
            cv.objects.get(id=nc.CV.id).delete()
            #Professeur.objects.get(id=id).delete()

            item_list = Professeur.objects.all()
            html = t.render(Context({'item_list':item_list, 'succes':mess}) )
        else:
            item_list = Professeur.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)



"""
Partie Cours

"""

"""
 Listing   Cours

"""


def admin_listing_Cours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/Listing_Cours.html')
        item_list = Cours.objects.all()

        ##=============================================

        paginator = Paginator(item_list, 5) # Show 25 contacts per page

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



        html = t.render(Context({'item_list':  cours_l}))
        #html = t.render(Context())
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


def admin_Show_CV_Cours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids= request.GET['id']
        t = get_template('Admintemplate/cours.html')
        item_list = Cours.objects.all()
        et = Cours.objects.get(id=ids)


        html = t.render(Context({'item': et}))
        #html = t.render(Context())
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


"""
 Enregistrer  Cours

"""

# def admin_enregistrer_Cours (request):
#     try:
#         t = get_template('Admintemplate/enregistrement_Cours.html')
#         #item_list = Cours.objects.all()
#         list_IDcours = NomCours.objects.all()
#         list_IDprogramme = Programme.objects.all()
#         list_IDcours2 =  NomCours.objects.all()
#         list_IDprofesseur = Professeur.objects.all()
#         list_Cours = Cours.objects.all()
#         html = t.render(Context({'list_IDcours':list_IDcours, 'list_IDprogramme':list_IDprogramme, 'list_IDcours2': list_IDcours2, 'list_IDprofesseur':list_IDprofesseur, 'list_Cours':list_Cours}))
#
#         #html = t.render(Context())
#         return HttpResponse(html)
#     except :
#         t = get_template('404Error.html')
#         html = t.render(Context({'info': 'Erreur dans la page '}))
#         return HttpResponse(html)
#
#
# def admin_enregistrer_Cours_form (request):
#     try:
#         IDcours = request.GET['IDcours']
#         IDprogramme = request.GET['IDprogramme']
#         Titre = request.GET['Titre']
#         Credits = request.GET['Credits']
#         IDprofesseur =  request.GET['IDprofesseur']
#         PubliqueCible =  request.GET['PubliqueCible'] # multiple
#         Prerequis = request.GET['Prerequis'] # multiple
#         Objectif =  request.GET['Objectif']
#         Description =  request.GET['Description']
#         Plan =  request.GET['Plan']
#         Format =  request.GET['Format']
#         Ressource =  request.GET['Ressource']
#         Evaluation =  request.GET['Evaluation']
#
#
#         isIn = Cours.objects.filter(IDcours=IDcours,IDprogramme=IDprogramme,Titre = Titre,Credits=Credits,IDprofesseur=IDprofesseur,PubliqueCible=PubliqueCible,Prerequis=Prerequis,
#                                     Objectif=Objectif, Description= Description,Plan=Plan,Format=Format,Ressource=Ressource,Evaluation=Evaluation).exists()
#
#         if isIn:
#             t = get_template('Admintemplate/enregistrement_Cours.html')
#             #item_list = Cours.objects.all()
#             list_IDcours = NomCours.objects.all()
#             list_IDprogramme = Programme.objects.all()
#             list_IDcours2 = NomCours.objects.all()
#             list_IDprofesseur = Professeur.objects.all()
#             list_Cours = Cours.objects.all()
#             html = t.render(Context({'reponse':'Donnee existe deja','list_IDcours':list_IDcours, 'list_IDprogramme':list_IDprogramme, 'list_IDcours2': list_IDcours2, 'list_IDprofesseur':list_IDprofesseur, 'list_Cours':list_Cours}))
#
#         else :
#
#             nCours = NomCours.objects.get(id=IDcours)
#             progr = Programme.objects.get(id=IDprogramme)
#             prof = Professeur.objects.get(id=IDprofesseur)
#
#             Cours(IDcours=nCours, IDprogramme=progr, Titre=Titre, Credits=Credits, IDprofesseur=prof, PubliqueCible=PubliqueCible,Prerequis=Prerequis,
#             Objectif=Objectif, Description=Description, Plan=Plan, Format=Format, Ressource=Ressource, Evaluation=Evaluation).save()
#
#             t = get_template('Admintemplate/enregistrement_Cours.html')
#             html = t.render(Context({'reponse':'Donnee Cours enregistree'}))
#
#
#         return HttpResponse(html)
#
#
#     except Exception, e:
#         t = get_template('404Error.html')
#         html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
#         return HttpResponse(html)
#

from django.shortcuts import render_to_response, HttpResponseRedirect, HttpResponse


def admin_enregistrer_Cours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        if request.method == 'POST': # If the form has been submitted...
            adminCours = AdminCours(request.POST) # A form bound to the POST data
            if adminCours.is_valid(): # All validation rules pass

                IDcours = request.POST['IDcours']
                IDprogramme = request.POST['IDprogramme']
                Titre = request.POST['Titre']
                Credits = request.POST['Credits']
                IDprofesseur =  request.POST['IDprofesseur']
                PubliqueCible =  request.POST['PubliqueCible'] # multiple
                #Prerequis = request.POST['Prerequis'] # multiple

                if Credits.isdigit() :
                    cred = int(Credits)
                    if cred > 4 :
                        t = get_template('404Error.html')
                        html = t.render(Context({'info': 'Erreur dans la page '}))
                        return HttpResponse(html)
                    if cred < 1 :
                        t = get_template('404Error.html')
                        html = t.render(Context({'info': 'Erreur dans la page '}))
                        return HttpResponse(html)
                if not  Credits.isdigit() :
                    t = get_template('404Error.html')
                    html = t.render(Context({'info': 'Erreur dans la page '}))
                    return HttpResponse(html)




                isIn = Cours.objects.filter(IDcours=IDcours,IDprogramme=IDprogramme,Titre = Titre,Credits=Credits,IDprofesseur=IDprofesseur ).exists()

                if not isIn:
                    adminCours.save()
                adminCours = AdminCours()
                return render_to_response('Admintemplate/enregistrement_Cours2.html', {'adminCours': adminCours}, context_instance=RequestContext(request)) # Redirect after POST
        else:
            adminCours = AdminCours() # An unbound form
        return render_to_response('Admintemplate/enregistrement_Cours2.html', {'adminCours': adminCours} ,context_instance=RequestContext(request))


    except Exception, e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)





def admin_enregistrer_Cours_form (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        IDcours = request.GET['IDcours']
        IDprogramme = request.GET['IDprogramme']
        Titre = request.GET['Titre']
        Credits = request.GET['Credits']
        IDprofesseur =  request.GET['IDprofesseur']
        PubliqueCible =  request.GET['PubliqueCible'] # multiple
        Prerequis = request.GET['Prerequis'] # multiple
        Objectif =  request.GET['Objectif']
        Description =  request.GET['Description']
        Plan =  request.GET['Plan']
        Format =  request.GET['Format']
        Ressource =  request.GET['Ressource']
        Evaluation =  request.GET['Evaluation']


        isIn = Cours.objects.filter(IDcours=IDcours,IDprogramme=IDprogramme,Titre = Titre,Credits=Credits,IDprofesseur=IDprofesseur,PubliqueCible=PubliqueCible,Prerequis=Prerequis,
                                    Objectif=Objectif, Description= Description,Plan=Plan,Format=Format,Ressource=Ressource,Evaluation=Evaluation).exists()

        if isIn:
            t = get_template('Admintemplate/enregistrement_Cours.html')
            #item_list = Cours.objects.all()
            list_IDcours = NomCours.objects.all()
            list_IDprogramme = Programme.objects.all()
            list_IDcours2 = NomCours.objects.all()
            list_IDprofesseur = Professeur.objects.all()
            list_Cours = Cours.objects.all()
            html = t.render(Context({'reponse':'Donnee existe deja','list_IDcours':list_IDcours, 'list_IDprogramme':list_IDprogramme, 'list_IDcours2': list_IDcours2, 'list_IDprofesseur':list_IDprofesseur, 'list_Cours':list_Cours}))

        else :

            nCours = NomCours.objects.get(id=IDcours)
            progr = Programme.objects.get(id=IDprogramme)
            prof = Professeur.objects.get(id=IDprofesseur)

            Cours(IDcours=nCours, IDprogramme=progr, Titre=Titre, Credits=Credits, IDprofesseur=prof, PubliqueCible=PubliqueCible,Prerequis=Prerequis,
            Objectif=Objectif, Description=Description, Plan=Plan, Format=Format, Ressource=Ressource, Evaluation=Evaluation).save()

            t = get_template('Admintemplate/enregistrement_Cours.html')
            html = t.render(Context({'reponse':'Donnee Cours enregistree'}))


        return HttpResponse(html)


    except Exception, e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)





"""
 modification Cours

"""


def admin_modification_Cours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")



            if request.method == 'POST': # If the form has been submitted...
                 if not request.POST.has_key('annuler'):
                    id = request.POST['id']
                    et = Cours.objects.get(id=id)
                    adminCours = AdminCours(request.POST,instance=et) # A form bound to the POST data
                    if adminCours.is_valid(): # All validation rules pass


                        adminCours.save()
                        adminCours = AdminCours()
                        item_list = Cours.objects.all()
                        return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list,'adminCours': adminCours}, context_instance=RequestContext(request)) # Redirect after POST
                    item_list = Cours.objects.all()
                    return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list} ,context_instance=RequestContext(request))

                 else:
                     item_list = Cours.objects.all()
                     return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list} ,context_instance=RequestContext(request))
            else:
                item_list = Cours.objects.all()
                return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list} ,context_instance=RequestContext(request))

    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)


def admin_modification_Cours_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        item_list = Cours.objects.all()
        et = Cours.objects.get(id=ids)
        adminCours = AdminCours(instance=et)
        return render_to_response('Admintemplate/modification_Cours.html', {'Et2': et, 'item_list': item_list,'adminCours': adminCours}, context_instance=RequestContext(request))
        #return render_to_response('Admintemplate/modification_Cours.html', {'item_list': item_list,'succes':'new page load'} ,context_instance=RequestContext(request))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_modification_Cours_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/modification_Cours.html')

        if not request.POST.has_key('annuler'):
            id= request.POST['id']
            nom = request.POST['nom']
            prenom = request.POST['prenom']
            NoId = request.POST['NoId']

            ## CV Part

            ad_prof = request.POST['ad_prof']
            sit_act = request.POST['sit_act']
            etablissement = request.POST['etablissement']
            EmploiActuel = request.POST['EmploiActuel']
            Formation = request.POST['Formation']
            EmploisPrecedents = request.POST['EmploisPrecedents']
            Experiencesdenseignement = request.POST['Experiencesdenseignement']
            ExperienceProfessionnelle = request.POST['ExperienceProfessionnelle']
            ResponsabiliteAdministrative =  request.POST['ResponsabiliteAdministrative']

            nc = Cours.objects.get(id=id)
            isIn = False
            if not (nc.Nom.__eq__(nom) and nc.Prenom.__eq__(prenom) and nc.NoIndentite.__eq__(NoId)):
                isIn =  Cours.objects.filter(Nom=nom,Prenom=prenom,NoIndentite=NoId).exists()

            if isIn:

                t = get_template('Admintemplate/modification_Cours.html')
                item_list = Cours.objects.all()
                html = t.render(Context({'item_list': item_list,'succes':'Donnee existe deja'}))
            else :
                CV = cv.objects.get(id=nc.CV.id)
                CV.ad_prof=ad_prof
                CV.sit_act= sit_act
                CV.etablissement= etablissement
                CV.EmploiActuel= EmploiActuel
                CV.Formation=Formation
                CV.EmploisPrecedents=EmploisPrecedents
                CV.Experiencesdenseignement=Experiencesdenseignement
                CV.ExperienceProfessionnelle=ExperienceProfessionnelle
                CV.ResponsabiliteAdministrative=ResponsabiliteAdministrative
                CV.save()
                nc.Nom=nom
                nc.Prenom=prenom
                nc.NoIndentite = NoId
                nc.save()
                item_list = Cours.objects.all()
                t = get_template('Admintemplate/modification_Cours.html')
                html = t.render(Context({'item_list': item_list,'succes':'Donnee Cours modifier'}))


            return HttpResponse(html)



        else:
            item_list = Cours.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page >>'+e.__str__()}))
        return HttpResponse(html)


"""
 supression  Cours

"""

def admin_supression_Cours (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_Cours.html')
        item_list = Cours.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Cours_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        ids = request.GET['ids']
        t = get_template('Admintemplate/supression_Cours.html')
        item_list = Cours.objects.all()
        et = Cours.objects.get(id=ids)
        html = t.render(Context({'Et2': et, 'item_list': item_list }))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Cours_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")
            
        t = get_template('Admintemplate/supression_Cours.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            nc = Cours.objects.get(id=id)
            #t.render(Context({'succes': "id: {} L'Cours {} a ete modifier ".format(et.Nom, et.id)}))
            mess="Cours {}   a ete supprime ".format(nc.Titre)
            Cours.objects.get(id=id).delete()
            #Cours.objects.get(id=id).delete()

            item_list = Cours.objects.all()
            html = t.render(Context({'item_list':item_list, 'succes':mess}) )
        else:
            item_list = Cours.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)




"""
Partie Utilisateur

"""

"""
 Ajouter Ulilisateur

"""


def admin_utilisateur_ajouter (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")



            if request.method == 'POST': # If the form has been submitted...

                user = request.POST['User']
                Password = request.POST['Password']
                PasswordC =request.POST['PasswordC']
                Status =request.POST['Status']
                ids =request.POST['ids']
                found = User.objects.filter(User=user).exists()
                if Password.__eq__(PasswordC) :
                    if not  found:

                        User(User=user,Password= Password,Status = Status, ids=ids).save()
                        item_list = Professeur.objects.all()
                        return render_to_response('Admintemplate/ajouter_utilisateur.html', {'item_list': item_list, 'success':"User add"}, context_instance=RequestContext(request)) # Redirect after POST
                    else:
                        item_list = Professeur.objects.all()
                        return render_to_response('Admintemplate/ajouter_utilisateur.html', {'item_list': item_list,'success':"User already exist"} ,context_instance=RequestContext(request))
                else:
                    item_list = Professeur.objects.all()
                    return render_to_response('Admintemplate/ajouter_utilisateur.html', {'item_list': item_list,'success':"Password Doesn't match"} ,context_instance=RequestContext(request))


            else:
                item_list = Professeur.objects.all()
                return render_to_response('Admintemplate/ajouter_utilisateur.html', {'item_list': item_list} ,context_instance=RequestContext(request))

    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)

""""

Listing Utilisateur

"""


def admin_listing_utilisateur (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")

        t = get_template('Admintemplate/Listing_utilisateur.html')
        item_list = User.objects.all()

         ##=============================================

        paginator = Paginator(item_list, 5) # Show 25 contacts per page

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

        html = t.render(Context({'item_list':  cours_l}))
        #html = t.render(Context())
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page'}))
        return HttpResponse(html)


"""

Changer Mot de pass

"""


def admin_utilisateur_changer_password (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")



            if request.method == 'POST': # If the form has been submitted...

                id = request.POST['id']
                Password = request.POST['Password']
                PasswordC =request.POST['PasswordC']
                userSave= User.objects.get(id=id)
                if Password.__eq__(PasswordC) :
                    userSave.Password = Password

                    userSave.save()


                    item_list = User.objects.all()
                    return render_to_response('Admintemplate/changer_password.html', {'item_list': item_list, 'success':"User add"}, context_instance=RequestContext(request)) # Redirect after POST
                else:
                    item_list = User.objects.all()
                    return render_to_response('Admintemplate/changer_password.html', {'item_list': item_list,'success':"Password Doesn't match"} ,context_instance=RequestContext(request))


            else:
                item_list = User.objects.all()
                return render_to_response('Admintemplate/changer_password.html', {'item_list': item_list} ,context_instance=RequestContext(request))

    except Exception , e:
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '+e.__str__()}))
        return HttpResponse(html)


"""""
Suppression Utilisateur

"""


def admin_supression_Utilisateur (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")

        t = get_template('Admintemplate/supression_utilisateur.html')
        item_list = User.objects.all()
        html = t.render(Context({'item_list': item_list}))
        return HttpResponse(html)

    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)


def admin_supression_Utilisateur_getInfo (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")

        ids = request.GET['ids']
        t = get_template('Admintemplate/supression_utilisateur.html')
        item_list = User.objects.all()
        et = User.objects.get(id=ids)
        html = t.render(Context({'item_list': item_list, 'Et': et}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)

def admin_supression_Utilisateur_Update (request):
    try:
        if 'User' not in request.session :
            return redirect("/gestionCours/admin_login/")
        else:
            if not request.session['Status'].__eq__("administration"):
                return redirect("/gestionCours/admin_login/")

        t = get_template('Admintemplate/supression_utilisateur.html')

        if not request.GET.has_key('annuler'):
            id = request.GET['id']
            et = User.objects.get(id=id)
            #t.render(Context({'succes': "id: {} L'etablissement {} a ete modifier ".format(et.Nom, et.id)}))

            t.render(Context({'succes': "L'etablissement {} a ete supprime ".format(et.User)}))
            User.objects.get(id=id).delete()
            item_list = User.objects.all()
            html = t.render(Context({'item_list':item_list}) )
        else:
            item_list = User.objects.all()
            html= t.render(Context({'item_list': item_list, 'succes': "Annuler"}))
            #= t.render(Context({'succes': "Annuler"}))
        return HttpResponse(html)
    except :
        t = get_template('404Error.html')
        html = t.render(Context({'info': 'Erreur dans la page '}))
        return HttpResponse(html)






