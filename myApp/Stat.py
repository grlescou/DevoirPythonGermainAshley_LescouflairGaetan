
from DjApp.models import Etablissement, NomCours, Programme, Professeur, cv , Cours , AdminCours, User, UserForm


class Stat (object):

# IDprogramme__Specialite
# E&G
# SI

    def  getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention (self,dom,sem,niv):
        ETCS=0
        listCours = Cours.objects.filter(IDprogramme__Mention=dom ,IDcours__Semestre=sem,IDcours__Grade=niv)
        for kour in listCours :
            ETCS += int( kour.Credits )

        return ETCS



    def getETCS_S1__by_Year_SI (self):
        ETCS_P= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","Propedeutique")
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","M2")

        return ["S1",ETCS_P,ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]





    def getETCS_S2__by_Year_SI (self):
        ETCS_P= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","Propedeutique")
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","M2")

        return ["S2",ETCS_P,ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]


    def getETCS_nS1__by_Year_SI (self):
        ETCS_P= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","Propedeutique")
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","M2")

        return [ETCS_P,ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]





    def getETCS_nS2__by_Year_SI (self):
        ETCS_P= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","Propedeutique")
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","M2")

        return [ETCS_P,ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]



    def getETCS__by__Licence(self):
        listS1 = self.getETCS_nS1__by_Year_SI()
        listS2 = self.getETCS_nS2__by_Year_SI()

        T=0
        for i in range(1,4):
            T += listS1[i]+listS2[i]

        return T

    def getETCS__by__M1(self):
        listS1 = self.getETCS_nS1__by_Year_SI()
        listS2 = self.getETCS_nS2__by_Year_SI()

        T=0
        for i in range(4,6):
            T += listS1[i]+listS2[i]

        return T


    def getETCS_S1__by_Year_EG (self):
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","M2")

        return ["S1",ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]





    def getETCS_S2__by_Year_EG (self):
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","M2")

        return ["S2",ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]


    def getETCS_nS1__by_Year_EG (self):
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","M2")

        return [ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]





    def getETCS_nS2__by_Year_EG (self):
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","M2")

        return [ETCS_L1,ETCS_L2,ETCS_L3,ETCS_M1,ETCS_M2]



    def getETCS__by__Licence_EG(self):
        listS1 = self.getETCS_nS1__by_Year_EG()
        listS2 = self.getETCS_nS2__by_Year_EG()

        T=0
        for i in range(0,3):
            T += listS1[i]+listS2[i]

        return T

    def getETCS__by__M_EG(self):
        listS1 = self.getETCS_nS1__by_Year_EG()
        listS2 = self.getETCS_nS2__by_Year_EG()

        T=0
        for i in range(3,5):
            T += listS1[i]+listS2[i]

        return T


    def VolumeECTS_Diplome(self):
        list_SI =["Sciences&Tech",self.getETCS__by__Licence(),self.getETCS__by__M1()]
        list_EG=["Economi&Gestion",self.getETCS__by__Licence_EG(),self.getETCS__by__M_EG()]

        return (list_SI, list_EG)



    def getHour_S1__by_Year_SI (self):
        ETCS_P= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","Propedeutique")
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S1","M2")

        return ["S1",ETCS_P*30,ETCS_L1*30,ETCS_L2*30,ETCS_L3*30,ETCS_M1*30,ETCS_M2*30]





    def getHour_S2__by_Year_SI (self):
        ETCS_P= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","Propedeutique")
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("SI","S2","M2")

        return ["S2",ETCS_P*30,ETCS_L1*30,ETCS_L2*30,ETCS_L3*30,ETCS_M1*30,ETCS_M2*30]




    def getHour_S1__by_Year_EG (self):
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S1","M2")

        return ["S1",ETCS_L1*30,ETCS_L2*30,ETCS_L3*30,ETCS_M1*30,ETCS_M2*30]





    def getHour_S2__by_Year_EG (self):
        ETCS_L1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L1")
        ETCS_L2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L2")
        ETCS_L3= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","L3")
        ETCS_M1= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","M1")
        ETCS_M2= self.getCours_ECTS_ByIDcours__Semestre_IDcours__Grade_IDprogramme__Mention("E&G","S2","M2")

        return ["S2",ETCS_L1*30,ETCS_L2*30,ETCS_L3*30,ETCS_M1*30,ETCS_M2*30]





    def VolumeHour_Diplome(self):
        list_SI =["Sciences&Tech",self.getETCS__by__Licence()*30,self.getETCS__by__M1()*30]
        list_EG=["Economi&Gestion",self.getETCS__by__Licence_EG()*30,self.getETCS__by__M_EG()*30]

        return (list_SI,list_EG)