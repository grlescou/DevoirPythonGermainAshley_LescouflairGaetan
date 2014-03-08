
from DjApp.models import Etablissement


def enregistrer (Etablissement):
    Etablissement.save()


def  selectAll ():
    return Etablissement.objects.all()


def selectEtablissemntWithNom (nom):
    return Etablissement.objects.filter(Nom=nom)


def findEtablissement(nom):
    try:
        p = Etablissement.objects.get(name='Apress')
    except Etablissement.DoesNotExist:
        print "Apress isn't in the database yet."
        return None
    else:
        print "Apress is in the database."
        return p

def oderListingEtablissement (by):
    return Etablissement.objects.order_by(by)