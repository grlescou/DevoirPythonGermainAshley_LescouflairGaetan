
from django.db import models
from django.forms import ModelForm
from  django import forms
class Etablissement (models.Model):
    Nom = models.CharField(max_length=250)
    Lieu = models.CharField(max_length=300)

    def __unicode__(self):
        return self.Nom




class NomCours (models.Model):
    CodeEtablissement = models.ForeignKey(Etablissement)
    Grade = models.CharField(max_length=20)
    Semestre = models.CharField(max_length=40)
    Nom = models.CharField(max_length=200)

    def __unicode__(self):
        return u'%s-%s-%s-%s' % (self.CodeEtablissement, self.Grade, self.Semestre, self.Nom)


class Programme (models.Model):
    Domaine = models.CharField(max_length=200)
    Mention = models.CharField(max_length=100)
    Specialite = models.CharField(max_length=100)
    TypeCours = models.CharField(max_length=20)
    Langue = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s-%s-%s-%s-%s' % (self.Domaine, self.Mention, self.Specialite, self.TypeCours,self.Langue)

class cv (models.Model):
    ad_prof = models.CharField(max_length=500)
    sit_act = models.CharField(max_length=500)
    etablissement = models.CharField(max_length=500)
    EmploiActuel = models.TextField()
    Formation = models.TextField()
    EmploisPrecedents = models.TextField()
    Experiencesdenseignement = models.TextField()
    ExperienceProfessionnelle = models.TextField()
    ResponsabiliteAdministrative = models.TextField()




class Professeur (models.Model):
    Nom = models.CharField(max_length=200)
    Prenom = models.CharField(max_length=200)
    NoIndentite = models.CharField(max_length=100)
    CV = models.ForeignKey(cv)

    def __unicode__(self):
        return u'%s %s' % (self.Nom, self.Prenom)



class Cours (models.Model):
    IDcours = models.ForeignKey(NomCours)
    IDprogramme = models.ForeignKey(Programme)
    Titre = models.CharField(max_length=100)
    Credits = models.CharField(max_length=100)
    IDprofesseur = models.ForeignKey(Professeur)
    PubliqueCible = models.CharField(max_length=100)
    Prerequis = models.ManyToManyField('self', symmetrical=False, null=True, blank=True)
    Objectif = models.TextField()
    Description = models.TextField()
    Plan = models.TextField()
    Format = models.CharField(max_length=400)
    Ressource = models.TextField()
    Evaluation = models.CharField(max_length=400)

    def __unicode__(self):
        return self.Titre




class AdminCours(ModelForm):
    class Meta:
        model = Cours
        fields = ('IDcours', 'IDprogramme','Titre','Credits','IDprofesseur','PubliqueCible','Prerequis')


class AdminProfesseur(ModelForm):

    class Meta:
        model = Cours
        fields = ('Objectif', 'Description','Plan','Format','Ressource','Evaluation')